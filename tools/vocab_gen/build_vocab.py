"""產生單字區（vocab/）的單字卡、投影片、測驗頁，並輸出錄音清單 audio_jobs.json。

每個單元一個資料檔（例如 w2000_u01.py：UNIT + QUIZ），在下面 UNITS 加上即可。
執行：python tools/vocab_gen/build_vocab.py
錄音：$env:KOKORO_DIR=...; python tools/grammar2_gen/tts_mp3.py tools/vocab_gen/audio_jobs.json
輸出：vocab/<book>/uNN.html（單字卡）、uNN-slides.html、uNN-quiz.html、audio/uNN/（w-NN 單字、e-NN 例句、slide-NN 投影片）
"""
import html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
C2 = os.path.join(REPO, 'tools', 'course2_gen')
sys.path.insert(0, C2)
from sl import ex, card, row, ul, cards, two, div, note, lead, qas, table, top5, section  # noqa: E402

sys.path.insert(0, HERE)
import w2000_u01  # noqa: E402
import w2000_u02  # noqa: E402
UNITS = (w2000_u01, w2000_u02)   # 新單元做好後加在這裡

BOOKS = {'w2000': '主題 2000 字', 'wordup': 'WORD UP 單字複習'}   # wordup：只用 WORD UP 的英文字表，內容自編
E = html.escape


def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(s)


# ---------------- 單字卡 ----------------
CARDS_TPL = '''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>單字區｜{book} Unit {no} {en} {zh}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Kalam:wght@400;700&family=Noto+Sans+TC:wght@400;500;700;900&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../grammar2/grammar.css?v=20261102">
<link rel="stylesheet" href="../vocab.css?v=20261104e">
</head>
<body>
<div class="wrap">
  <div class="top-links">
    <a class="home-link" href="../index.html">← 單字區目錄</a>
  </div>
  <div class="eyebrow">VOCABULARY · {bookup} UNIT {no}</div>
  <h1>{en}．{zh}</h1>
  <div class="subtitle">{intro}</div>

  <div class="unit-btns"><a class="u-slides" href="{tag}-slides.html">📊 投影片</a><a class="u-quiz" href="{tag}-quiz.html">📝 單元測驗（計點數）</a></div>

  <div class="vc-tools">
    <span>共 <b>{n}</b> 個單字．點 🔊 聽發音</span>
    <span>
      <button class="btn" type="button" data-hide="zh">🙈 遮中文</button>
      <button class="btn" type="button" data-hide="en">🙈 遮英文</button>
      <button class="btn alt" type="button" data-play-all>▶ 全部播放</button>
    </span>
  </div>

  <div class="vc-grid" id="cards">
{cards}
  </div>
{focus}
  <div class="pager">
    <a href="../index.html"><small>BACK</small>← 單字區目錄</a>
    <a class="next" href="{tag}-quiz.html"><small>NEXT</small>📝 單元測驗 →</a>
  </div>
</div>
<script src="../vocab.js?v=20261104e"></script>
</body>
</html>
'''


CUR = {}   # build() 設定目前的 book，photo() 用來找照片


def photo(tag, w):
    """有照片（vocab/<book>/img/uNN/<單字>.jpg）就回傳相對路徑，沒有就回傳 None（改用 emoji）。"""
    rel = 'img/%s/%s.jpg' % (tag, w['w'])
    return rel if os.path.exists(os.path.join(REPO, 'vocab', CUR['book'], rel)) else None


def card_html(i, w, tag):
    n = '%02d' % (i + 1)
    noteh = '<div class="vc-note">%s</div>' % E(w['note']) if w.get('note') else ''
    ph = photo(tag, w)
    if ph:
        pic = '<img class="vc-photo" src="%s" alt="%s" loading="lazy">' % (ph, E(w['w'], quote=True))
    else:
        pic = '<span class="vc-pic" aria-hidden="true">%s</span>' % w['pic'] if w.get('pic') else ''
    return ('    <div class="vc-card">%s\n'
            '      <div class="vc-head"><span class="vc-num">%d</span>'
            '<span class="vc-word">%s</span>'
            '<button class="vc-say" type="button" data-src="audio/%s/w-%s.mp3" data-say="%s" aria-label="唸單字">🔊</button>'
            '<span class="vc-pos">%s</span></div>\n'
            '      <div class="vc-zh">%s</div>%s\n'
            '      <div class="vc-ex"><span class="vc-en">%s</span>'
            '<button class="vc-say sm" type="button" data-src="audio/%s/e-%s.mp3" data-say="%s" aria-label="唸例句">🔊</button>'
            '<span class="vc-exzh">%s</span></div>\n'
            '    </div>' % (pic, i + 1, E(w['w']), tag, n, E(w['w'], quote=True), E(w['pos']), E(w['zh']), noteh,
                           E(w['ex']), tag, n, E(w['ex'], quote=True), E(w['exzh'])))


def focus_items(u):
    """重點整理：舊格式 (標題, [(單數, 複數)…]) 當成複數表；新格式是 dict(title, head, rows, note)。空白欄位不顯示。"""
    out = []
    for f in u.get('focus', []):
        if isinstance(f, tuple):
            title, pairs = f
            f = {'title': title, 'head': ('單數', '複數'), 'rows': pairs, 'plural': True,
                 'note': '不規則複數一定要背；其他字多半加 -s，子音 + y 改 -ies（baby → babies）。'}
        cols = [i for i, h in enumerate(f['head']) if h]
        out.append(dict(f, head=[f['head'][i] for i in cols], rows=[[r[i] for i in cols] for r in f['rows']]))
    return out


def focus_html(u):
    out = []
    for f in focus_items(u):
        th = ''.join('<th>%s</th>' % E(h) for h in f['head'])
        rows = ''.join('<tr>%s</tr>' % ''.join('<td class="en">%s</td>' % E(c) for c in r) for r in f['rows'])
        nt = '<div class="tip">%s</div>' % E(f['note']) if f.get('note') else ''
        out.append('<section class="part"><div class="part-no">FOCUS</div><h2>%s</h2>'
                   '<div class="tbl-wrap"><table class="gt"><tr>%s</tr>%s</table></div>%s</section>'
                   % (E(f['title']), th, rows, nt))
    return '\n'.join(out)


# ---------------- 投影片 ----------------
PIC_CSS = '''
.pg{display:grid;grid-template-columns:repeat(4,1fr);gap:calc(var(--u)*1.1)}
.pc{background:#fff;border:1px solid var(--line);border-radius:calc(var(--u)*1);padding:calc(var(--u)*.6) calc(var(--u)*.9);display:flex;flex-direction:column;gap:calc(var(--u)*.2)}
.pc .pp{font-size:calc(var(--u)*5);line-height:1.1;text-align:center}
.pc img.pp{width:100%;height:calc(var(--u)*15);object-fit:cover;object-position:50% 35%;border-radius:calc(var(--u)*.6);display:block}
.pc .pw{font-family:Georgia,serif;font-size:calc(var(--u)*2.3);font-weight:700;color:var(--deep);text-align:center}
.pc .pz{font-size:calc(var(--u)*1.35);text-align:center;color:var(--ink)}
.pc .pz small{color:var(--ink-soft);font-size:.85em;margin-left:.3em}
.pc .pe{font-size:calc(var(--u)*1.3);color:var(--ink-soft);background:var(--paper-2);border-radius:calc(var(--u)*.6);padding:calc(var(--u)*.4) calc(var(--u)*.7);margin-top:auto}
@media (max-width:760px){.pg{grid-template-columns:1fr 1fr}.pc .pp{font-size:40px}.pc img.pp{height:110px}.pc .pw{font-size:20px}.pc .pz{font-size:14px}.pc .pe{font-size:13px}}
'''


def pic_grid(grp, tag):
    """每個字一張圖卡：照片（沒有就用 emoji）、單字 🔊、詞性中文、例句 🔊。"""
    from sl import btn, _say
    out = []
    for w in grp:
        ph = photo(tag, w)
        pic = ('<img class="pp" src="%s" alt="%s">' % (ph, E(w['w'], quote=True)) if ph
               else '<div class="pp">%s</div>' % w.get('pic', ''))
        out.append('<div class="pc">%s<div class="pw">%s %s</div>'
                   '<div class="pz">%s<small>%s</small></div>'
                   '<div class="pe">%s %s<br>%s</div></div>'
                   % (pic, E(w['w']), btn(w['w']), E(w['zh']), E(w['pos']),
                      E(w['ex']), btn(_say(E(w['ex']))), E(w['exzh'])))
    return '<div class="pg">%s</div>' % ''.join(out)


def slides(u, tag, book_name):
    ws = u['words']
    S = []
    S.append(section('本單元單字一覽', lead(u['intro']) + '<div class="chips">%s</div>'
                     % ''.join('<span class="chip">%s</span>' % E(w['w']) for w in ws) +
                     note('每個字都有 🔊，先聽發音、跟著唸，再看例句。')))
    per = 4
    for k in range(0, len(ws), per):
        grp = ws[k:k + per]
        S.append(section('單字 %d–%d' % (k + 1, k + len(grp)), pic_grid(grp, tag)))
    for f in focus_items(u):
        if f.get('plural'):
            body = table(f['head'] + ['例句'], [[a, '<b>%s</b>' % b, ('two %s' % b, '%s 的複數' % a)] for a, b in f['rows']],
                         audio_col=2)
        else:
            body = table(f['head'], [[E(c) for c in r] for r in f['rows']])
        S.append(section(f['title'], body + (note(E(f['note'])) if f.get('note') else '')))
    step = max(1, len(ws) // 16)
    sample = ws[::step][:16]   # 字多時平均抽 16 個
    S.append(section('快問快答：中文 → 英文', qas([(w['zh'], w['w']) for w in sample[:8]])))
    S.append(section('快問快答：英文 → 中文', qas([(w['w'], w['zh']) for w in sample[8:16]])))
    S.append(section('學完了！接下來', two(card('複習方法', ul([
        '回到「📗 單字卡」，按「遮中文」自己考自己',
        '再按「遮英文」，看中文說出英文',
        '每個例句跟著 🔊 唸一次']), sub='review'),
        card('準備好了', ul(['按右上角「📝 前往測驗」', '測驗錯的題目要訂正到全對', '訂正完成補送 1 點']), 'o'))))

    head = read(os.path.join(C2, 'slides_head.html'))
    tail = read(os.path.join(C2, 'slides_tail.html'))
    reps = [
        ('第二期 WEEK 14 投影片｜分詞構句、連接詞與轉折語', '單字區 %s Unit %d 投影片｜%s %s' % (book_name, u['no'], u['en'], u['zh'])),
        ('<div class="eyebrow">WEEK 14 · SLIDES</div>', '<div class="eyebrow">VOCABULARY UNIT %d · SLIDES</div>' % u['no']),
        ('<h1 class="page">分詞構句、連接詞與轉折語</h1>', '<h1 class="page">%s %s</h1>' % (u['en'], u['zh'])),
        ('<a class="home-link" href="../index.html">🏠 回總目錄</a>',
         '<a class="home-link" href="../index.html">← 單字區目錄</a>\n    <a class="home-link" href="%s.html">📗 單字卡</a>' % tag),
        ('<a class="quiz-link" href="quiz.html">📝 前往測驗</a>', '<a class="quiz-link" href="%s-quiz.html">📝 前往測驗</a>' % tag),
    ]
    for a, b in reps:
        assert a in head, a
        head = head.replace(a, b)
    head = head.replace('</style>', PIC_CSS + '</style>', 1)
    tail = tail.replace("new Audio('audio/slide-'", "new Audio('audio/%s/slide-'" % tag)
    title = ('<section class="s dark title"><div class="week">UNIT %d · VOCABULARY</div><h1 class="big">%s</h1>'
             '<div class="en-sub">%s</div><div class="venn"><span class="c1">%d 個單字</span><span class="c2">聽・唸・用</span></div></section>'
             % (u['no'], u['zh'], u['en'], len(ws)))
    body = '\n'.join([title] + S)
    says = [html.unescape(m) for m in re.findall(r'class="sentence-btn" type="button" data-say="([^"]*)"', body)]
    return head + body + tail, says


# ---------------- 測驗 ----------------
QUIZ_TPL = '''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>單字區｜{book} Unit {no} {en} 測驗</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Kalam:wght@400;700&family=Noto+Sans+TC:wght@400;500;700;900&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../grammar2/grammar.css?v=20261102">
</head>
<body>
<div class="wrap">
  <div class="top-links">
    <a class="home-link" href="{tag}.html">← 單字卡</a>
    <a class="home-link" href="../index.html">單字區目錄</a>
  </div>
  <div class="eyebrow">VOCABULARY QUIZ · {bookup} UNIT {no}</div>
  <h1>{en} {zh}．單元測驗</h1>
  <div class="subtitle">看中文選英文 → 看英文選中文 → 拼字 → 例句填空。全部作答才能送出，錯題要訂正到全對。</div>
  <section class="part">
    <div id="gquiz"></div>
  </section>
</div>
<script>
window.GQUIZ = {data};
</script>
<script src="../../grammar2/gquiz.js?v=20261104e"></script>
<script src="../../points.js"></script>
</body>
</html>
'''


def build(mod):
    u, quiz = mod.UNIT, mod.QUIZ
    book, no = u['book'], u['no']
    CUR['book'] = book
    tag = 'u%02d' % no
    out = os.path.join(REPO, 'vocab', book)
    book_name = BOOKS[book]
    fmt = dict(book=book_name, bookup=book_name, no=no, en=E(u['en']), zh=E(u['zh']), intro=E(u['intro']), tag=tag,
               n=len(u['words']))
    write(os.path.join(out, tag + '.html'), CARDS_TPL.format(
        cards='\n'.join(card_html(i, w, tag) for i, w in enumerate(u['words'])), focus=focus_html(u), **fmt))
    page, says = slides(u, tag, book_name)
    write(os.path.join(out, tag + '-slides.html'), page)
    data = {'label': 'Vocab %s U%d' % (book.upper(), no), 'title': '單字區 %s Unit %d %s' % (book_name, no, u['zh']),
            'back': tag + '.html', 'sections': quiz}
    write(os.path.join(out, tag + '-quiz.html'), QUIZ_TPL.format(data=json.dumps(data, ensure_ascii=False, indent=1), **fmt))
    adir = os.path.join(out, 'audio', tag)
    jobs = []
    for i, w in enumerate(u['words']):
        jobs.append([w['w'], os.path.join(adir, 'w-%02d.mp3' % (i + 1))])
        jobs.append([w['ex'], os.path.join(adir, 'e-%02d.mp3' % (i + 1))])
    jobs += [[s, os.path.join(adir, 'slide-%02d.mp3' % (i + 1))] for i, s in enumerate(says)]
    return jobs


if __name__ == '__main__':
    jobs = []
    for m in UNITS:
        j = build(m)
        print('%s Unit %d：%d 個音檔' % (m.UNIT['book'], m.UNIT['no'], len(j)))
        jobs += j
    with open(os.path.join(HERE, 'audio_jobs.json'), 'w', encoding='utf-8') as f:
        json.dump(jobs, f, ensure_ascii=False, indent=0)
