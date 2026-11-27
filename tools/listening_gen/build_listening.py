"""聽力訓練（listening/）：多益聽力四部分題型，分 初級／中級／中高級。

資料檔：tools/listening_gen/lt_<回>.py（b01、b02…＝初級；之後 m01…＝中級、h01…＝中高級），內容自編。
用法：
  $env:KOKORO_DIR='C:\\Users\\jenlin2002\\kokoro-models'
  python tools/listening_gen/build_listening.py [b01 b02 …]
  （不指定就全部重做。錄音直接在這裡做：每句先錄成快取，再接成每回一個 audio/<回>/all.mp3，頁面用 #t=開始,結束 播放）
產生：listening/<回>.html（測驗）、listening/<回>-dict.html（聽寫）、listening/index.html（目錄）。
頁面行為：listening/lt.js（播放、聽幾次的限制、重聽速度、聽寫），作答／送出／訂正／計點用 grammar2/gquiz.js。
錄音快取在 %LOCALAPPDATA%\\listening_tts（不在 repo；換電腦會重錄，內容一樣）。
"""
import hashlib, html, importlib, json, os, re, sys
import numpy as np
import soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(REPO, 'listening')
CACHE = os.path.join(os.environ.get('LOCALAPPDATA', HERE), 'listening_tts')
sys.path.insert(0, HERE)
E = html.escape
V = '20261125a'          # lt.js／listening.css 的快取版本（改了要一起改）
GQ = '20261125a'         # gquiz.js 的快取版本
SR = 24000
LEVELS = {
    'b': {'name': '初級', 'en': 'BASIC', 'who': '國小高年級～國中', 'speed': 0.85, 'plays': 2,
          'toeic': '多益聽力約 150–250 分', 'desc': '國中 2000 字以內，慢一點的語速，每題可以聽 2 次。'},
    'm': {'name': '中級', 'en': 'INTERMEDIATE', 'who': '高中', 'speed': 0.95, 'plays': 1,
          'toeic': '多益聽力約 250–350 分', 'desc': '高中 4500 字＋生活、職場常用語，正常語速，每題聽 1 次。'},
    'h': {'name': '中高級', 'en': 'UPPER-INTERMEDIATE', 'who': '高中進階、大學、社會人士', 'speed': 1.0, 'plays': 1,
          'toeic': '多益聽力約 350–450 分', 'desc': '多益常考職場字彙，正常到稍快，混入英國腔、澳洲腔，每題聽 1 次。'},
}
VOICE = {'W': 'af_heart', 'M': 'am_michael', 'N': 'am_fenrir', 'A': 'af_bella', 'BW': 'bf_emma', 'BM': 'bm_george'}   # 女、男、題號旁白、廣播
LET = 'ABCD'
UNITS = {n[3:-3]: n[:-3] for n in sorted(os.listdir(HERE)) if re.fullmatch(r'lt_[bmh]\d\d\.py', n)}

_k = None


def tts(text, voice, speed):
    """錄一句（有快取）→ float32 陣列，音量拉到一致（平均約 -16 dB、最大不超過 -1 dB）"""
    global _k
    os.makedirs(CACHE, exist_ok=True)
    h = hashlib.sha1(('%s|%s|%.2f' % (voice, text, speed)).encode('utf-8')).hexdigest()[:16]
    f = os.path.join(CACHE, h + '.wav')
    if not os.path.exists(f):
        if _k is None:
            from kokoro_onnx import Kokoro
            md = os.environ.get('KOKORO_DIR', r'C:\Users\jenlin2002\kokoro-models')
            _k = Kokoro(os.path.join(md, 'kokoro-v1.0.int8.onnx'), os.path.join(md, 'voices-v1.0.bin'))
        d, sr = _k.create(text, voice=voice, speed=speed, lang='en-us')
        assert sr == SR
        sf.write(f, d, SR)
        print('  錄音', voice, text[:50], flush=True)
    d = sf.read(f, dtype='float32')[0]
    rms = float(np.sqrt((d * d).mean())) or 1e-6
    peak = float(np.abs(d).max()) or 1e-6
    g = min(10 ** (-16 / 20) / rms, 10 ** (-1 / 20) / peak)
    return d * g


class Track:
    """把一回的所有句子接成一條音軌，記下每句的時間"""
    def __init__(self, speed):
        self.parts, self.pos, self.speed = [], 0.0, speed

    def gap(self, sec):
        self.parts.append(np.zeros(int(sec * SR), dtype='float32')); self.pos += sec

    def add(self, text, voice):
        d = tts(text, VOICE.get(voice, voice), self.speed)
        a = self.pos
        self.parts.append(d); self.pos += len(d) / SR
        return [a, self.pos]

    def write(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        sf.write(path, np.concatenate(self.parts), SR, format='MP3', bitrate_mode='CONSTANT', compression_level=0.6)


def T(seg):            # 時間 → data-t（前後多留一點）
    return '%.2f,%.2f' % (max(0, seg[0] - 0.05), seg[1] + 0.12)


def play_btn(qid, seg):
    return '<button type="button" class="lt-play" data-id="%s" data-t="%s">▶ 播放</button>' % (qid, T(seg))


def say(seg):
    return '<button type="button" class="lt-say" data-t="%s" title="重聽這一句">🔊</button>' % T(seg)


def line(seg, en, zh, tag='', ok=False):
    return '<div class="lt-line%s">%s %s<span class="en">%s</span><span class="zh">%s</span></div>' % (
        ' ok' if ok else '', say(seg), ('<b class="lt-tag">%s</b>' % tag) if tag else '', E(en), E(zh))


def build_unit(m):
    u = m.UNIT; lv = LEVELS[u['level']]; uid = u['id']
    tr = Track(lv['speed'])
    tr.gap(0.5)
    secs, dict_items = [], []
    n = 0

    def number(k):
        s = tr.add('Number %d.' % k, 'N'); tr.gap(0.6); return s

    # 第一部分 看照片
    items = []
    for it in u['p1']:
        n += 1; a = number(n); segs = []
        for k, (en, zh) in enumerate(it['opts']):
            l = tr.add(LET[k] + '.', it.get('v', 'M')); tr.gap(0.25)
            s = tr.add(en, it.get('v', 'M')); segs.append([l[0], s[1]]); tr.gap(1.0)
            if k == it['answer']:
                dict_items.append({'t': T(s), 'en': en, 'zh': zh})
        tr.gap(0.8)
        q = ('<span class="lt-hideopts"></span><span class="lt-sr">[看照片 %s]</span>%s'
             '<img class="lt-photo" src="img/%s.jpg" alt="照片 %d">') % (it['img'], play_btn('q%d' % n, [a[0], segs[-1][1]]), it['img'], n)
        exp = '<div class="lt-tr"><div class="lt-trh">📝 聽力原文</div>' + ''.join(
            line(segs[k], en, zh, LET[k] + '.', k == it['answer']) for k, (en, zh) in enumerate(it['opts'])) + \
            '<div class="lt-tip">💡 %s</div></div>' % E(it['tip'])
        items.append({'type': 'mc', 'q': q, 'opts': [en for en, _ in it['opts']], 'answer': it['answer'], 'exp': exp})
    secs.append({'title': 'Part 1　看照片選描述（%d 題）' % len(items),
                 'note': '按「▶ 播放」會聽到 %s句子（不印出來），選出最符合照片的句子。' % (
                     'A、B、C、D 四個' if len(u['p1'][0]['opts']) == 4 else 'A、B、C 三個'), 'items': items})

    # 第二部分 問答
    items = []
    for it in u['p2']:
        n += 1; a = number(n)
        qv, av = it.get('v', ('W', 'M'))      # 中高級可用 'v': ('BW', 'M') 之類換成英國腔（問句、回答）
        qs = tr.add(it['q'][0], qv); tr.gap(1.0)
        dict_items.append({'t': T(qs), 'en': it['q'][0], 'zh': it['q'][1]})
        segs = []
        for k, (en, zh) in enumerate(it['opts']):
            l = tr.add(LET[k] + '.', av); tr.gap(0.25)
            s = tr.add(en, av); segs.append([l[0], s[1]]); tr.gap(1.0)
        tr.gap(0.8)
        q = '<span class="lt-hideopts"></span><span class="lt-sr">[問答]</span>%s <span class="lt-cue">聽問句，選出最適當的回答</span>' % play_btn('q%d' % n, [a[0], segs[-1][1]])
        exp = '<div class="lt-tr"><div class="lt-trh">📝 聽力原文</div>' + line(qs, it['q'][0], it['q'][1], '問') + ''.join(
            line(segs[k], en, zh, LET[k] + '.', k == it['answer']) for k, (en, zh) in enumerate(it['opts'])) + \
            '<div class="lt-tip">💡 %s</div></div>' % E(it['tip'])
        items.append({'type': 'mc', 'q': q, 'opts': [en for en, _ in it['opts']], 'answer': it['answer'], 'exp': exp})
    secs.append({'title': 'Part 2　問答（%d 題）' % len(items),
                 'note': '先聽到一個問句，再聽到 A、B、C 三個回答（都不印出來），選出最適當的回答。', 'items': items})

    # 第三部分 對話
    items = []
    for it in u['p3']:
        n += 1; a = number(n); segs = []
        for who, en, zh in it['lines']:
            segs.append(tr.add(en, who)); tr.gap(0.5)
        tr.gap(0.4)
        qs = tr.add(it['q'][0], 'N'); tr.gap(1.5)
        q = '%s <span class="lt-cue">聽對話，回答問題</span><div class="lt-qtext">%s</div>' % (play_btn('q%d' % n, [a[0], qs[1]]), E(it['q'][0]))
        exp = '<div class="lt-tr"><div class="lt-trh">📝 對話原文</div>' + ''.join(
            line(s, en, zh, '👩' if who in ('W', 'BW') else '👨') for s, (who, en, zh) in zip(segs, it['lines'])) + \
            line(qs, it['q'][0], it['q'][1], '問') + \
            '<div class="lt-opzh">選項：' + '　'.join('(%s) %s' % (LET[k], E(zh)) for k, (_, zh) in enumerate(it['opts'])) + '</div>' + \
            '<div class="lt-tip">💡 %s</div></div>' % E(it['tip'])
        items.append({'type': 'mc', 'q': q, 'opts': [en for en, _ in it['opts']], 'answer': it['answer'], 'exp': exp})
    secs.append({'title': 'Part 3　簡短對話（%d 題）' % len(items),
                 'note': '聽一段對話，回答畫面上的問題（問題也會唸出來）。👩＝女生、👨＝男生。', 'items': items})

    # 第四部分 獨白
    items = []
    for it in u['p4']:
        n += 1; a = number(n); segs = []
        voice = {'W': 'A', 'M': 'M'}.get(it['voice'], it['voice'])
        for en, zh in it['lines']:
            segs.append(tr.add(en, voice)); tr.gap(0.35)
        tr.gap(0.5)
        qs = tr.add(it['q'][0], 'N'); tr.gap(1.5)
        q = '%s <span class="lt-cue">%s</span><div class="lt-qtext">%s</div>' % (
            play_btn('q%d' % n, [a[0], qs[1]]), E(it['kind'][1] + '｜' + it['kind'][0]), E(it['q'][0]))
        exp = '<div class="lt-tr"><div class="lt-trh">📝 原文（%s）</div>' % E(it['kind'][1]) + ''.join(
            line(s, en, zh) for s, (en, zh) in zip(segs, it['lines'])) + line(qs, it['q'][0], it['q'][1], '問') + \
            '<div class="lt-opzh">選項：' + '　'.join('(%s) %s' % (LET[k], E(zh)) for k, (_, zh) in enumerate(it['opts'])) + '</div>' + \
            '<div class="lt-tip">💡 %s</div></div>' % E(it['tip'])
        items.append({'type': 'mc', 'q': q, 'opts': [en for en, _ in it['opts']], 'answer': it['answer'], 'exp': exp})
    secs.append({'title': 'Part 4　簡短獨白（%d 題）' % len(items),
                 'note': '聽一段廣播、留言或說明，回答畫面上的問題（問題也會唸出來）。', 'items': items})

    tr.write(os.path.join(OUT, 'audio', uid, 'all.mp3'))
    label = 'Listening %s' % uid.upper()
    title = '聽力訓練 %s' % u['title']
    links = ('<a class="btn" href="%s-dict.html">✍️ 聽寫練習</a> <a class="btn" href="index.html">聽力訓練目錄</a>' % uid)
    cfg = {'label': label, 'title': title, 'back': 'index.html', 'mode': '聽力測驗', 'links': links, 'sections': secs}
    head = page_head('聽力訓練｜%s' % u['title'])
    h = head + '''  <div class="top-links">
    <a class="home-link" href="index.html">← 聽力訓練目錄</a>
  </div>
  <div class="eyebrow">LISTENING · %s · TEST %d</div>
  <h1>%s <span class="zh">%s</span></h1>
  <div class="subtitle">多益聽力題型・%d 題・%s</div>
  <section class="part lt-rules">
    <ul>
      <li>每一題按 <b>▶ 播放</b>，作答時每題最多聽 <b>%d 次</b>。第一、二部分的選項不印出來，要用聽的。</li>
      <li>全部作答才能送出；送出後看 <b>聽力原文＋中文</b>，每一句都能按 🔊 重聽，也可以改成慢速。</li>
      <li>錯的題目要訂正（訂正時可以一直重聽），全部訂正完再補送 1 點。</li>
    </ul>
    <div class="lt-speed">重聽速度：<button type="button" data-rate="1">一般</button><button type="button" data-rate="0.75">🐢 慢速</button></div>
  </section>
  <section class="part lt-quiz"><div id="gquiz"></div></section>
</div>
<script>
window.LT = %s;
window.GQUIZ = %s;
</script>
<script src="lt.js?v=%s"></script>
<script src="../grammar2/gquiz.js?v=%s"></script>
<script src="../points.js"></script>
</body>
</html>
''' % (lv['en'], u['no'], E(lv['name']), E('第 %d 回｜%s' % (u['no'], u['theme'])), n, E(lv['toeic']), lv['plays'],
       json.dumps({'audio': 'audio/%s/all.mp3' % uid, 'plays': lv['plays']}),
       json.dumps(cfg, ensure_ascii=False, indent=1), V, GQ)
    open(os.path.join(OUT, uid + '.html'), 'w', encoding='utf-8', newline='\n').write(h)

    # 聽寫
    h = page_head('聽力訓練｜%s 聽寫' % u['title']) + '''  <div class="top-links">
    <a class="home-link" href="index.html">← 聽力訓練目錄</a>
    <a class="home-link" href="%s.html">%s 測驗</a>
  </div>
  <div class="eyebrow">LISTENING · %s · DICTATION %d</div>
  <h1>%s <span class="zh">聽寫練習</span></h1>
  <div class="subtitle">聽一句、寫一句：把聽到的英文打出來，按「對答案」看哪些字聽對了（自我練習，不計點數）</div>
  <section class="part">
    <div class="lt-speed">播放速度：<button type="button" data-rate="1">一般</button><button type="button" data-rate="0.75">🐢 慢速</button></div>
    <div id="ltDict"></div>
  </section>
</div>
<script>
window.LT = %s;
window.LTD = %s;
</script>
<script src="lt.js?v=%s"></script>
<script src="/dict/dict.js?v=20261118a" defer></script>
</body>
</html>
''' % (uid, E(u['title']), lv['en'], u['no'], E(u['title']),
       json.dumps({'audio': 'audio/%s/all.mp3' % uid, 'plays': 0}), json.dumps(dict_items, ensure_ascii=False, indent=0), V)
    open(os.path.join(OUT, uid + '-dict.html'), 'w', encoding='utf-8', newline='\n').write(h)
    print('%s：%d 題、聽寫 %d 句、音檔 %.0f 秒' % (uid, n, len(dict_items), tr.pos))


def page_head(title):
    return '''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%s</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Kalam:wght@400;700&family=Noto+Sans+TC:wght@400;500;700;900&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../grammar2/grammar.css?v=20261102">
<link rel="stylesheet" href="listening.css?v=%s">
</head>
<body>
<div class="wrap">
''' % (E(title), V)


PLANNED = {'b': 10, 'm': 10, 'h': 10}     # 每級預計幾回（還沒做的顯示「製作中」）


def index_page():
    mods = [importlib.import_module(UNITS[k]) for k in sorted(UNITS)]
    h = page_head('聽力訓練｜Listening Hub') + '''  <div class="top-links">
    <a class="home-link" href="/">← 成長學習館</a>
  </div>
  <div class="eyebrow">LISTENING HUB</div>
  <h1>聽力訓練 <span class="zh">Listening Hub</span></h1>
  <div class="subtitle">照多益聽力的四種題型練習，分初級、中級、中高級，從國小、國中到大人都能用</div>
  <section class="part">
    <h2>四種題型</h2>
    <ol class="lt-how">
      <li><b>Part 1 看照片選描述</b>：看一張照片，聽 A、B、C 三個句子，選出最符合的。</li>
      <li><b>Part 2 問答</b>：聽一個問句和三個回答，選出最適當的回答。</li>
      <li><b>Part 3 簡短對話</b>：聽兩個人的對話，回答問題。</li>
      <li><b>Part 4 簡短獨白</b>：聽廣播、留言、說明，回答問題。</li>
    </ol>
    <p>每回 20 題，大約 10 分鐘。送出後對答案，可以看原文和中文、每句重聽、改成慢速；錯題要訂正。每回另有<b>聽寫練習</b>。</p>
  </section>
'''
    for lv, L in LEVELS.items():
        done = [m for m in mods if m.UNIT['level'] == lv]
        h += '  <section class="part lt-level lv-%s">\n    <div class="part-no">%s</div><h2>%s <span class="lt-who">%s</span></h2>\n' % (lv, L['en'], E(L['name']), E(L['who']))
        h += '    <p class="lt-ldesc">%s（%s）</p>\n    <div class="lt-grid">\n' % (E(L['desc']), E(L['toeic']))
        for m in done:
            u = m.UNIT
            h += ('      <div class="lt-card"><div class="lc-no">TEST %d</div><div class="lc-t">第 %d 回</div><div class="lc-d">%s</div>'
                  '<div class="lc-links"><a class="btn alt" href="%s.html">開始測驗</a> <a class="btn" href="%s-dict.html">聽寫</a></div>'
                  '<div class="lc-st" data-id="%s"></div></div>\n') % (u['no'], u['no'], E(u['theme']), u['id'], u['id'], u['id'])
        for k in range(len(done) + 1, PLANNED[lv] + 1):
            h += '      <div class="lt-card soon"><div class="lc-no">TEST %d</div><div class="lc-t">第 %d 回</div><span class="lc-tag">製作中</span></div>\n' % (k, k)
        h += '    </div>\n  </section>\n'
    h += '''</div>
<script src="lt.js?v=%s"></script>
<script src="../points.js"></script>
</body>
</html>
''' % V
    open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8', newline='\n').write(h)


if __name__ == '__main__':
    only = sys.argv[1:] or sorted(UNITS)
    for k in only:
        build_unit(importlib.import_module(UNITS[k]))
    index_page()
