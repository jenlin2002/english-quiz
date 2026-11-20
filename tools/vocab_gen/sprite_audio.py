"""把一個單元的許多小 mp3 合併成一個 all.mp3（音檔精靈），頁面的 data-src 改成「all.mp3#t=開始,結束」。

用法：python tools/vocab_gen/sprite_audio.py vocab/w2000 u14 [--delete] [--level=0.6]
  - 讀 <book>/<uNN>.html、<uNN>-slides.html 裡所有 data-src="audio/uNN/xxx.mp3"（照出現順序、不重複）
  - 解碼後接起來，每段之間插入 GAP 秒靜音，用固定位元率重新壓成 audio/uNN/all.mp3
  - 頁面的 data-src 改成 audio/uNN/all.mp3#t=開始,結束（瀏覽器的 media fragment；播放程式另外用 timeupdate 保險停住）
  - --delete：刪掉已合併、頁面不再用到的小 mp3（不加就保留原檔，可隨時還原）
  - --level：壓縮程度 0～1（越小位元率越高、檔案越大）
已經改過的頁面再跑一次：會先把 #t= 還原成原檔名（記在 all.json）再重做。
"""
import json, os, re, sys
import numpy as np
import soundfile as sf

GAP = 0.6        # 每段之間的靜音（秒）：避免停太慢聽到下一句的開頭
LEAD = 0.05      # 每段開頭往前多留一點
TAIL = 0.10      # 每段結尾往後多留一點
SR = 24000
CLIP_STOP = ("  const clip = /#t=[\\d.]+,([\\d.]+)/.exec(a.src);\n"
             "  if(clip){ const end = +clip[1]; a.addEventListener('timeupdate', () => { if(a.currentTime >= end){ a.pause(); btn.classList.remove('playing'); } }); }\n")


def main(book, tag, delete=False, level=0.6):
    adir = os.path.join(book, 'audio', tag)
    pages = [p for p in (os.path.join(book, tag + '.html'), os.path.join(book, tag + '-slides.html')) if os.path.exists(p)]
    mapfile = os.path.join(adir, 'all.json')
    old = json.load(open(mapfile, encoding='utf-8')) if os.path.exists(mapfile) else {}
    back = {v: k for k, v in old.items()}          # "all.mp3#t=..." -> 原檔名
    texts = {}
    for p in pages:
        t = open(p, encoding='utf-8').read()
        t = re.sub(r'data-src="(audio/%s/all\.mp3#t=[^"]+)"' % tag, lambda m: 'data-src="%s"' % back.get(m.group(1), m.group(1)), t)
        texts[p] = t
    order = []
    for t in texts.values():
        for s in re.findall(r'data-src="(audio/%s/[^"#]+\.mp3)"' % tag, t):
            if s not in order and os.path.exists(os.path.join(book, s)):
                order.append(s)
    if not order:
        print('沒有可合併的音檔'); return
    parts, pos, mp = [], 0.0, {}
    gap = np.zeros(int(GAP * SR), dtype='float32')
    for s in order:
        d, sr = sf.read(os.path.join(book, s), dtype='float32')
        if d.ndim > 1: d = d.mean(axis=1)
        assert sr == SR, (s, sr)
        parts += [d, gap]
        dur = len(d) / SR
        mp[s] = 'audio/%s/all.mp3#t=%.2f,%.2f' % (tag, max(0, pos - LEAD), pos + dur + TAIL)
        pos += dur + GAP
    out = os.path.join(adir, 'all.mp3')
    sf.write(out, np.concatenate(parts), SR, format='MP3', bitrate_mode='CONSTANT', compression_level=level)
    for p, t in texts.items():
        t = re.sub(r'data-src="(audio/%s/[^"#]+\.mp3)"' % tag, lambda m: 'data-src="%s"' % mp.get(m.group(1), m.group(1)), t)
        if p.endswith('-slides.html') and CLIP_STOP not in t:   # 投影片的播放程式：播到 #t 結尾就停
            t = t.replace("  a.addEventListener('error', fb);\n", "  a.addEventListener('error', fb);\n" + CLIP_STOP, 1)
        open(p, 'w', encoding='utf-8', newline='\n').write(t)
    json.dump(mp, open(mapfile, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    info = sf.info(out)
    size = os.path.getsize(out)
    print('%s：%d 個音檔 → all.mp3（%.1f 秒、%d KB、約 %.0f kbps）' % (tag, len(order), info.duration, size // 1024, size * 8 / info.duration / 1000))
    if delete:
        for s in order:
            os.remove(os.path.join(book, s))
        print('已刪除 %d 個小檔' % len(order))


if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if not x.startswith('--')]
    lv = next((float(x.split('=')[1]) for x in sys.argv if x.startswith('--level=')), 0.6)
    main(a[0], a[1], '--delete' in sys.argv, lv)
