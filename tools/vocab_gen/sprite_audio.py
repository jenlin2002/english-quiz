"""音檔合併（音檔精靈）：把一個單元的許多小 mp3 合併成一個 all.mp3，頁面的 data-src 改成「all.mp3#t=開始,結束」。
目的：Cloudflare Pages 一個網站最多 20000 個檔案，合併後每個單元只剩 all.mp3＋all.json 兩個檔。

用法：
  python tools/vocab_gen/sprite_audio.py --all [--delete]          整個英文測驗系統（單字區、文法區投影片、第二期投影片）
  python tools/vocab_gen/sprite_audio.py vocab/w2000 u14 [--delete] 單字區一個單元（uNN.html＋uNN-slides.html，音檔 audio/uNN/）
  python tools/vocab_gen/sprite_audio.py grammar2 u05-slides.html audio/u05 [--delete]   任一頁面：資料夾、頁面、音檔前綴
  python tools/vocab_gen/sprite_audio.py course2/w03 slides.html audio [--delete]
  --delete：合併並比對通過後，刪掉已合併的小 mp3（不加就保留，可隨時還原）
  --level=0.6：壓縮程度 0～1（越小位元率越高；0.6 約 64 kbps，比原本約 43 kbps 高）

做法：
  - 投影片按鈕沒有 data-src 的（第 N 顆按鈕播 slide-NN.mp3），先補上 data-src，播放程式改成先用 data-src。
  - 解碼後接起來，每段之間插 GAP 秒靜音，用固定位元率壓成 <前綴>/all.mp3；對照表 <前綴>/all.json（原檔名 → all.mp3#t=）。
  - 合併後解碼 all.mp3 逐段和原檔比對響度起伏，相似度低於 0.8 就不刪小檔、印出警告。
  - 播放程式：投影片自動插入「播到 #t 結尾就停」；單字卡用 vocab/vocab.js（已內建）。
重新產生頁面後（build_vocab.py、build_lala.py、build_slides.py…）要再跑一次這個工具：
  頁面上的原檔名會照 all.json 換回 #t=；已刪掉的小檔會從舊的 all.mp3 切回來，新錄的小檔一起合併。
"""
import glob, json, os, re, sys
import numpy as np
import soundfile as sf

GAP = 0.6        # 每段之間的靜音（秒）：瀏覽器停得慢一點也不會聽到下一句
LEAD = 0.05      # 每段開頭往前多留一點
TAIL = 0.10      # 每段結尾往後多留一點
SR = 24000
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CLIP_STOP = ("  const clip = /#t=[\\d.]+,([\\d.]+)/.exec(a.src);\n"
             "  if(clip){ const end = +clip[1]; a.addEventListener('timeupdate', () => { if(a.currentTime >= end){ a.pause(); btn.classList.remove('playing'); } });"
             " a.addEventListener('pause', () => btn.classList.remove('playing')); }\n")
OLD_CLIP_STOP = ("  if(clip){ const end = +clip[1]; a.addEventListener('timeupdate', () => { if(a.currentTime >= end){ a.pause(); btn.classList.remove('playing'); } }); }\n")
BTN = re.compile(r'<button class="sentence-btn"[^>]*>')


def env(x):
    x = x[: len(x) // 240 * 240].reshape(-1, 240)
    return np.sqrt((x * x).mean(axis=1))


def similar(a, b):
    """響度包絡相似度（a 在 b 裡找最佳位置）"""
    n = len(a); best = -1.0
    if len(b) < n:
        return 0.0
    ea = env(a)
    for lag in range(0, len(b) - n + 1, 48):
        eb = env(b[lag: lag + n])
        m = min(len(ea), len(eb))
        if m < 3 or ea[:m].std() == 0 or eb[:m].std() == 0:
            continue
        best = max(best, float(np.corrcoef(ea[:m], eb[:m])[0, 1]))
    return best


def process(base, pages, prefix, delete=False, level=0.6, quiet=False):
    base = os.path.join(REPO, base)
    adir = os.path.join(base, prefix)
    mapfile = os.path.join(adir, 'all.json')
    old = json.load(open(mapfile, encoding='utf-8')) if os.path.exists(mapfile) else {}
    back = {v: k for k, v in old.items()}
    sp = re.escape(prefix)
    texts = {}
    for p in pages:
        path = os.path.join(base, p)
        if not os.path.exists(path):
            continue
        t = open(path, encoding='utf-8', newline='').read()
        t = re.sub(r'data-src="(%s/all\.mp3#t=[^"]+)"' % sp, lambda m: 'data-src="%s"' % back.get(m.group(1), m.group(1)), t)
        if p.endswith('slides.html'):
            # 第 N 顆按鈕 → slide-NN.mp3（還沒有 data-src 的才補）
            cnt = [0]
            def fill(m):
                cnt[0] += 1
                tag = m.group(0)
                if 'data-src=' in tag:
                    return tag
                s = '%s/slide-%02d.mp3' % (prefix, cnt[0])
                if os.path.exists(os.path.join(base, s)) or s in old:
                    return tag.replace('class="sentence-btn"', 'class="sentence-btn" data-src="%s"' % s, 1)
                return tag
            t = BTN.sub(fill, t)
            t = t.replace("const a = new Audio('audio/", "const a = new Audio(btn.getAttribute('data-src') || 'audio/")
        texts[path] = t
    order = []
    for t in texts.values():
        for s in re.findall(r'data-src="(%s/[^"#/]+\.mp3)"' % sp, t):
            if s not in order and (os.path.exists(os.path.join(base, s)) or s in old):
                order.append(s)
    if not order:
        return None
    oldsprite = None
    clips = []
    for s in order:
        f = os.path.join(base, s)
        if os.path.exists(f):
            d, sr = sf.read(f, dtype='float32')
            if d.ndim > 1:
                d = d.mean(axis=1)
            if sr != SR:
                raise SystemExit('%s 取樣率 %d，不是 %d' % (f, sr, SR))
            clips.append((s, d, True))
        else:                                     # 小檔已刪：從舊的 all.mp3 切回來
            if oldsprite is None:
                oldsprite = sf.read(os.path.join(adir, 'all.mp3'), dtype='float32')[0]
            a, b = map(float, re.search(r'#t=([\d.]+),([\d.]+)', old[s]).groups())
            a = a + (LEAD if a > 0 else 0)
            clips.append((s, oldsprite[int(round(a * SR)): int(round((b - TAIL) * SR))], False))
    if all(not fresh for _, _, fresh in clips) and order == list(old.keys()):
        mp = old                                 # 全部已合併、沒有新音檔：只把頁面換回 #t=
    else:
        parts, pos, mp = [], 0.0, {}
        gap = np.zeros(int(GAP * SR), dtype='float32')
        for s, d, _ in clips:
            parts += [d, gap]
            dur = len(d) / SR
            mp[s] = '%s/all.mp3#t=%.2f,%.2f' % (prefix, max(0, pos - LEAD), pos + dur + TAIL)
            pos += dur + GAP
        sf.write(os.path.join(adir, 'all.mp3'), np.concatenate(parts), SR, format='MP3', bitrate_mode='CONSTANT', compression_level=level)
        json.dump(mp, open(mapfile, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    for path, t in texts.items():
        t = re.sub(r'data-src="(%s/[^"#/]+\.mp3)"' % sp, lambda m: 'data-src="%s"' % mp.get(m.group(1), m.group(1)), t)
        t = t.replace(OLD_CLIP_STOP, CLIP_STOP.split('\n', 1)[1])   # 舊版（只有 timeupdate）換成新版
        if path.endswith('slides.html') and 'const clip = ' not in t:
            t = re.sub(r"(  a\.addEventListener\('error', fb\);\r?\n)", lambda m: m.group(1) + CLIP_STOP, t, count=1)
        open(path, 'w', encoding='utf-8', newline='').write(t)
    # 比對：新合併檔的每一段 vs 原檔
    worst, bad = 1.0, []
    fresh = [(s, d) for s, d, f in clips if f]
    if fresh:
        sprite = sf.read(os.path.join(adir, 'all.mp3'), dtype='float32')[0]
        for s, d in fresh:
            a, b = map(float, re.search(r'#t=([\d.]+),([\d.]+)', mp[s]).groups())
            c = similar(d, sprite[int(a * SR): int(b * SR) + 240])
            worst = min(worst, c)
            if c < 0.8:
                bad.append((s, round(c, 3)))
    rel = os.path.relpath(adir, REPO).replace('\\', '/')
    if not quiet or bad:
        print('%s：%d 段（新 %d）→ all.mp3，最低相似度 %.3f%s' % (rel, len(order), len(fresh), worst, ('  ⚠ 有問題：%s' % bad) if bad else ''))
    removed = 0
    if delete and not bad:
        for s in order:
            f = os.path.join(base, s)
            if os.path.exists(f):
                os.remove(f); removed += 1
    return len(order), removed, bad


def all_units():
    jobs = []
    for book in ('vocab/w2000', 'vocab/w2000p2', 'vocab/lala', 'vocab/wordup'):
        for f in sorted(glob.glob(os.path.join(REPO, book, 'u[0-9][0-9]*.html'))):
            if '-' in os.path.basename(f):
                continue   # 只取單字卡頁（u34a.html 這種拆頁的也算），slides／quiz 跟著單字卡處理
            tag = os.path.basename(f)[:-5]
            jobs.append((book, [tag + '.html', tag + '-slides.html'], 'audio/' + tag))
    for f in sorted(glob.glob(os.path.join(REPO, 'grammar2', 'u[0-9][0-9]-slides.html'))):
        tag = os.path.basename(f)[:3]
        jobs.append(('grammar2', [os.path.basename(f)], 'audio/' + tag))
    for f in sorted(glob.glob(os.path.join(REPO, 'writing', 'u[0-9][0-9].html'))):
        tag = os.path.basename(f)[:3]
        jobs.append(('writing', [tag + '.html'], 'audio/' + tag))
    for f in sorted(glob.glob(os.path.join(REPO, 'course2', '*', 'slides.html'))):
        jobs.append((os.path.relpath(os.path.dirname(f), REPO).replace('\\', '/'), ['slides.html'], 'audio'))
    return jobs


if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if not x.startswith('--')]
    lv = next((float(x.split('=')[1]) for x in sys.argv if x.startswith('--level=')), 0.6)
    dl = '--delete' in sys.argv
    if '--all' in sys.argv:
        n = r = 0; probs = []
        for base, pages, prefix in all_units():
            res = process(base, pages, prefix, dl, lv, quiet=True)
            if res:
                n += res[0]; r += res[1]; probs += res[2]
        print('合計 %d 段音檔；刪除小檔 %d 個；有問題 %d 段 %s' % (n, r, len(probs), probs[:10]))
    elif len(a) == 2:
        process(a[0], [a[1] + '.html', a[1] + '-slides.html'], 'audio/' + a[1], dl, lv)
    else:
        process(a[0], [a[1]], a[2], dl, lv)
