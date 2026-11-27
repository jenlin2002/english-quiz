"""寫作園地（writing/）：產生每個主題的引導頁 uNN.html、造句練習 uNN-quiz.html、目錄 index.html，並輸出錄音清單。

資料檔：tools/writing_gen/wr_uNN.py（UNIT＋QUIZ，內容自編）。新主題做好資料檔就會自動加進來。
用法：
  python tools/writing_gen/build_writing.py [單元號…]          產生頁面，錄音清單寫到 tools/writing_gen/audio_jobs.json
  $env:KOKORO_DIR='C:\\Users\\jenlin2002\\kokoro-models'; python tools/grammar2_gen/tts_mp3.py tools/writing_gen/audio_jobs.json
  python tools/vocab_gen/boost_audio.py writing/audio/uNN
  python tools/vocab_gen/sprite_audio.py writing uNN.html audio/uNN --delete     （合併成 all.mp3，省檔案數）
頁面行為在 writing/writing.js（說說看的麥克風、句型、短文的自動檢查／文法與 AI 建議／送出計點），樣式 writing/writing.css。
"""
import html, importlib, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(REPO, 'writing')
sys.path.insert(0, HERE)
E = html.escape
V = '20261128a'          # writing.js／writing.css 的快取版本（改了要一起改）
GQ = '20261120a'         # gquiz.js 的快取版本（和英文測驗系統其他頁面一致）
VOICE_B = 'am_michael'   # 對話第二個人的聲音
UNITS = [importlib.import_module(n[:-3]) for n in sorted(os.listdir(HERE)) if re.fullmatch(r'wr_u\d\d\.py', n)]

HEAD = '''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Kalam:wght@400;700&family=Noto+Sans+TC:wght@400;500;700;900&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../grammar2/grammar.css?v=20261102">
<link rel="stylesheet" href="writing.css?v={v}">
</head>
<body>
<div class="wrap">
'''


def say(text, src, label='🔊', cls='say'):
    return '<button class="%s" type="button" data-say="%s" data-src="%s" title="播放">%s</button>' % (cls, E(text, True), src, label)


def blanks(frame, key):
    parts = frame.split('____')
    out = E(parts[0])
    for i, p in enumerate(parts[1:]):
        out += '<input class="wr-in" data-key="%s-%d" autocomplete="off" autocapitalize="off" spellcheck="false" data-dict-off>' % (key, i) + E(p)
    return out


def unit_page(m, jobs):
    u = m.UNIT; no = u['no']; tag = 'u%02d' % no; ad = 'audio/' + tag
    w = u['write']
    def a(name, text, voice=None):
        jobs.append([text, os.path.join(OUT, ad, name)] + ([voice] if voice else []))
        return '%s/%s' % (ad, name)
    h = HEAD.format(title='寫作園地｜Unit %d %s %s' % (no, E(u['en']), E(u['zh'])), v=V)
    h += '''  <div class="top-links">
    <a class="home-link" href="index.html">← 寫作園地</a>
  </div>
  <div class="eyebrow">WRITING · UNIT %d</div>
  <h1>%s <span class="zh">%s</span></h1>
  <div class="subtitle">%s</div>
  <nav class="wr-steps">
    <a href="#s1">① 說說看</a><a href="#s2">② 字詞庫</a><a href="#s3">③ 句型練習</a><a href="#s4">④ 造句練習</a><a href="#s5">⑤ 寫短文</a>
  </nav>
''' % (no, E(u['en']), E(u['zh']), E(u['intro']))
    # ① 說說看
    h += '<section class="part" id="s1"><div class="part-no">STEP 1 · LISTEN &amp; SPEAK</div><h2>① 先聽，再說說看</h2>\n'
    h += '<p class="wr-tip">先聽一段對話，再回答下面的問題：按 🎤 用說的（會變成文字），也可以直接打字。說出來的想法，等一下寫短文用得到。</p>\n<div class="wr-dialog">'
    who0 = u['dialog'][0][0]
    for i, (who, line) in enumerate(u['dialog'], 1):
        src = a('d-%02d.mp3' % i, line, None if who == who0 else VOICE_B)
        h += '<div class="wr-line %s"><b>%s</b> %s %s</div>' % ('a' if who == who0 else 'b', E(who), say(line, src), E(line))
    h += '</div>\n<ol class="wr-speak">'
    for i, (q, zh, hint) in enumerate(u['speak'], 1):
        src = a('q-%02d.mp3' % i, q)
        h += ('<li><div class="wr-q">%s <span>%s</span></div><div class="wr-zh">%s</div>'
              '<div class="wr-ans"><input class="wr-in long" data-key="s%d" placeholder="按 🎤 說說看，或直接打字" autocomplete="off" spellcheck="false" data-dict-off>'
              '<button class="mic" type="button" data-for="s%d" title="用說的">🎤</button></div>'
              '<div class="wr-hint">💡 例：%s</div></li>') % (say(q, src), E(q), E(zh), i, i, E(hint))
    h += '</ol></section>\n'
    # ② 字詞庫
    h += '<section class="part" id="s2"><div class="part-no">STEP 2 · WORD BANK</div><h2>② 這個主題的字詞庫</h2>\n'
    h += '<p class="wr-tip">寫短文時至少要用到幾個這裡的字詞（★ 2 個、★★ 3 個）。按 ☆ 可以存成字卡。</p>\n<div class="wr-words">'
    for i, (en, zh, ex, exzh, _rx) in enumerate(u['words'], 1):
        s1 = a('w-%02d.mp3' % i, en.replace('…', '').replace('  ', ' '))
        s2 = a('e-%02d.mp3' % i, ex)
        h += ('<div class="wr-word vc-card" data-en="%s"><div class="ww-head">%s <b class="vc-word">%s</b> <span class="vc-zh">%s</span></div>'
              '<div class="ww-ex">%s <span class="vc-en">%s</span></div><div class="ww-exzh vc-exzh">%s</div></div>') % (
            E(en, True), say(en, s1, cls='say vc-say'), E(en), E(zh), say(ex, s2, cls='say vc-say sm'), E(ex), E(exzh))
    h += '</div></section>\n'
    # ③ 句型練習
    h += '<section class="part" id="s3"><div class="part-no">STEP 3 · SENTENCE FRAMES</div><h2>③ 句型練習：填空造句</h2>\n'
    h += '<p class="wr-tip">用自己的情況把句子填完整（可以按 🎤 用說的）。想不出來就按「看例句」。這些句子可以直接放進你的短文裡。</p>\n<ol class="wr-frames">'
    for i, (f, zh, ex) in enumerate(u['frames'], 1):
        src = a('f-%02d.mp3' % i, ex)
        h += ('<li><div class="wr-frame">%s <button class="mic" type="button" data-for="f%d-0" title="用說的">🎤</button></div><div class="wr-zh">%s</div>'
              '<button class="btn wr-show" type="button">看例句</button><div class="wr-ex" hidden>%s %s</div></li>') % (
            blanks(f, 'f%d' % i), i, E(zh), say(ex, src), E(ex))
    h += '</ol></section>\n'
    # ④ 造句練習（英檢單句寫作）
    nq = sum(len(s['items']) for s in m.QUIZ)
    h += ('<section class="part" id="s4"><div class="part-no">STEP 4 · GEPT SENTENCE WRITING</div><h2>④ 造句練習（英檢題型）</h2>\n'
          '<p>全民英檢初級寫作第一部分的三種題型：<b>句子合併、句子改寫、重組句子</b>，共 %d 題。要自己寫出完整的句子，送出後對答案、錯的要訂正，會計點數。</p>'
          '<p><a class="btn alt big" href="%s-quiz.html">✏️ 開始造句練習</a></p></section>\n') % (nq, tag)
    # ⑤ 寫短文
    m1 = a('m-1.mp3', w['model'][1]); m2 = a('m-2.mp3', w['model'][2])
    targets = [{'en': en, 'rx': rx} for en, zh, ex, exzh, rx in u['words']]
    h += '<section class="part" id="s5"><div class="part-no">STEP 5 · WRITE</div><h2>⑤ 寫一篇短文</h2>\n'
    h += '<div id="wrWrite"></div>'
    h += '<div hidden>%s%s</div></section>\n' % (say(w['model'][1], m1, cls='say wr-m1'), say(w['model'][2], m2, cls='say wr-m2'))
    h += '</div>\n'
    cfg = {'unit': no, 'label': 'Writing U%d' % no, 'title': '寫作園地 Unit %d %s' % (no, u['zh']), 'topic': u['en'],
           'prompt': w['prompt'], 'zh': w['zh'], 'tense': u['tense'], 'qs': w['qs'], 'targets': targets,
           'speakQs': [q for q, _, _ in u['speak']], 'frames': [f for f, _, _ in u['frames']],
           'model': {'1': w['model'][1], '2': w['model'][2]}, 'card': bool(u.get('card'))}
    h += '<script>window.WRITING = %s;</script>\n' % json.dumps(cfg, ensure_ascii=False, indent=0)
    h += '<script src="writing.js?v=%s"></script>\n<script src="../points.js"></script>\n</body>\n</html>\n' % V
    open(os.path.join(OUT, tag + '.html'), 'w', encoding='utf-8', newline='\n').write(h)


def quiz_page(m):
    u = m.UNIT; no = u['no']; tag = 'u%02d' % no
    data = {'label': 'Writing U%d' % no, 'title': '寫作園地 Unit %d %s 造句練習' % (no, u['zh']), 'back': tag + '.html', 'sections': m.QUIZ}
    h = HEAD.format(title='寫作園地｜Unit %d %s 造句練習' % (no, E(u['zh'])), v=V)
    h += '''  <div class="top-links">
    <a class="home-link" href="%s.html">← Unit %d %s</a>
    <a class="home-link" href="index.html">寫作園地</a>
  </div>
  <div class="eyebrow">WRITING · UNIT %d · SENTENCE WRITING</div>
  <h1>%s <span class="zh">造句練習</span></h1>
  <div class="subtitle">句子合併 → 句子改寫 → 重組句子（全民英檢初級寫作題型）。全部作答才能送出，錯題要訂正到全對。</div>
  <section class="part wr-quiz"><div id="gquiz"></div></section>
</div>
<script>
window.GQUIZ = %s;
</script>
<script src="../grammar2/gquiz.js?v=%s"></script>
<script src="../points.js"></script>
</body>
</html>
''' % (tag, no, E(u['zh']), no, E(u['zh']), json.dumps(data, ensure_ascii=False, indent=1), GQ)
    open(os.path.join(OUT, tag + '-quiz.html'), 'w', encoding='utf-8', newline='\n').write(h)


PLANNED = [('My Family', '我的家人'), ('A Day at School', '學校的一天'), ('My Favorite Food', '我最喜歡的食物'),
           ('A Birthday Party', '生日派對'), ('Going Shopping', '去買東西'), ('Asking the Way', '問路'),
           ('Holidays in Taiwan', '臺灣的節日'), ('A Trip', '一次旅行'), ('My Dream', '我的夢想'),
           ('An Invitation Card', '寫邀請卡'), ('Saying Sorry', '寫道歉卡片')]


def index_page():
    h = HEAD.format(title='寫作園地｜Writing Hub', v=V)
    h += '''  <div class="top-links">
    <a class="home-link" href="/">← 成長學習館</a>
  </div>
  <div class="eyebrow">WRITING HUB</div>
  <h1>寫作園地 <span class="zh">Writing Hub</span></h1>
  <div class="subtitle">生活化的主題，先聽、先說，再一步一步寫出來。程度對應全民英檢初級。</div>
  <section class="part">
    <h2>每個主題的五個步驟</h2>
    <ol class="wr-how">
      <li><b>① 說說看</b>：聽一段生活對話，用 🎤 回答問題（說的話會變成文字）。</li>
      <li><b>② 字詞庫</b>：這個主題常用的單字和片語，可以存成字卡。</li>
      <li><b>③ 句型練習</b>：用句型框架填入自己的事情，先寫出幾個好句子。</li>
      <li><b>④ 造句練習</b>：英檢題型（句子合併、改寫、重組），送出對答案、訂正、計點。</li>
      <li><b>⑤ 寫短文</b>：★（30 字以上）或 ★★（50 字以上，英檢段落寫作的長度）。寫完先「檢查我的作文」：自動檢查＋文法拼字＋AI 建議，改好再送出計點；作文會存到試算表給家長看。</li>
    </ol>
  </section>
  <div class="wr-grid">
'''
    for m in UNITS:
        u = m.UNIT; tag = 'u%02d' % u['no']
        h += ('    <div class="wr-unit"><div class="wu-no">UNIT %d</div><div class="wu-t">%s</div><div class="wu-zh">%s</div><div class="wu-d">%s</div>'
              '<div class="wu-links"><a class="btn alt" href="%s.html">開始</a> <a class="btn" href="%s-quiz.html">造句練習</a></div>'
              '<div class="wu-st" data-unit="%s"></div></div>\n') % (u['no'], E(u['en']), E(u['zh']), E(u['intro']), tag, tag, tag)
    done = {m.UNIT['en'] for m in UNITS}
    for i, (en, zh) in enumerate([p for p in PLANNED if p[0] not in done], len(UNITS) + 1):
        h += '    <div class="wr-unit soon"><div class="wu-no">UNIT %d</div><div class="wu-t">%s</div><div class="wu-zh">%s</div><span class="wu-tag">製作中</span></div>\n' % (i, E(en), E(zh))
    h += '''  </div>
</div>
<script src="writing.js?v=%s"></script>
<script src="../points.js"></script>
</body>
</html>
''' % V
    open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8', newline='\n').write(h)


if __name__ == '__main__':
    only = set(int(x) for x in sys.argv[1:])
    jobs = []
    for m in UNITS:
        if only and m.UNIT['no'] not in only:
            continue
        unit_page(m, jobs); quiz_page(m)
        print('寫作園地 Unit %d：引導頁＋造句練習（%d 題）' % (m.UNIT['no'], sum(len(s['items']) for s in m.QUIZ)))
    index_page()
    json.dump(jobs, open(os.path.join(HERE, 'audio_jobs.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print('錄音 %d 句 → tools/writing_gen/audio_jobs.json' % len(jobs))
