"""產生單字區「LaLa Word 一字多義」（vocab/lala/）的單字卡、投影片、測驗頁，並回傳錄音清單。

和 build_vocab.py 的差別：一個字有好幾個意思，每個意思各有詞性、中文、（片語）、例句。
資料檔：tools/vocab_gen/lala_uNN.py（UNIT 的 words 用 W(字, emoji, [S(詞性, 中文, 例句, 例句中文, 片語)…], 變化形)）
用法：python tools/vocab_gen/build_lala.py   → 產生 UNITS 的所有單元，錄音清單寫到 tools/vocab_gen/audio_jobs.json
      錄音：$env:KOKORO_DIR=...; python tools/grammar2_gen/tts_mp3.py tools/vocab_gen/audio_jobs.json
      放大音量：python tools/vocab_gen/boost_audio.py vocab/lala/audio/uNN
音檔：vocab/lala/audio/uNN/w-NN.mp3（單字）、e-NN-K.mp3（第 NN 個字第 K 個意思的例句）；投影片直接用這些音檔（link_slide_audio）。
單字卡沿用 vocab.css／vocab.js（.vc-card、.vc-word、.vc-zh、.vc-en…），所以學習進度、我的字卡、測驗的單字對照都照常運作。
"""
import html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_vocab as BV  # noqa: E402
import link_slide_audio  # noqa: E402
from sl import btn, note, lead, qas, table, section, two, card, ul  # noqa: E402
import lala_u01  # noqa: E402

UNITS = (lala_u01,)   # 新單元做好後加在這裡
BV.BOOKS['lala'] = 'LaLa Word 一字多義'
E = html.escape

LALA_CSS = '''
.vc-card.lala .vs-list{ list-style:none; margin:0; padding:0; display:flex; flex-direction:column; gap:6px; }
.vc-card.lala .vs-head{ display:flex; flex-wrap:wrap; align-items:baseline; gap:6px; margin-bottom:2px; }
.vs-no{ font-family:'Space Mono',monospace; font-size:12px; color:var(--ink-soft); }
.vs-tag{ font-size:11.5px; font-weight:700; color:#fff; background:#5B7C6A; border-radius:4px; padding:0 6px; }
.vs-zh{ font-weight:700; color:#3C3C34; }
.vs-ph{ font-size:12.5px; color:#8A5A12; background:#FBEFD5; border-radius:4px; padding:0 6px; }
.hide-zh .vs-zh, .hide-zh .vs-ph{ color:transparent; background:#D8D0BA; }
'''


def senses_pos(w):
    seen = []
    for s in w['senses']:
        if s['pos'] != '片語' and s['pos'] not in seen:
            seen.append(s['pos'])
    return ' / '.join(seen) or '片語'


def zh_all(w):
    return '；'.join(s['zh'] for s in w['senses'] if s['pos'] != '片語')


def card_html(i, w, tag):
    n = '%02d' % (i + 1)
    ph = BV.photo(tag, w)
    if ph:
        pic = '<img class="vc-photo" src="%s" alt="%s" loading="lazy">' % (ph, E(w['w'], quote=True))
    else:
        pic = '<span class="vc-pic" aria-hidden="true">%s</span>' % w['pic']
    forms = '<div class="vc-note">%s</div>' % E(w['forms']) if w.get('forms') else ''
    lis = []
    for k, s in enumerate(w['senses'], 1):
        phh = ' <span class="vs-ph">%s</span>' % E(s['ph']) if s.get('ph') else ''
        lis.append('<li class="vc-ex"><div class="vs-head"><span class="vs-no">%d</span><span class="vs-tag">%s</span>'
                   '<span class="vs-zh">%s</span>%s</div><span class="vc-en">%s</span>'
                   '<button class="vc-say sm" type="button" data-src="audio/%s/e-%s-%d.mp3" data-say="%s" aria-label="唸例句">🔊</button>'
                   '<span class="vc-exzh">%s</span></li>'
                   % (k, E(s['pos']), E(s['zh']), phh, E(s['ex']), tag, n, k, E(s.get('exsay', s['ex']), quote=True), E(s['exzh'])))
    return ('    <div class="vc-card lala">%s\n'
            '      <div class="vc-head"><span class="vc-num">%d</span><span class="vc-word">%s</span>'
            '<button class="vc-say" type="button" data-src="audio/%s/w-%s.mp3" data-say="%s" aria-label="唸單字">🔊</button>'
            '<span class="vc-pos">%s</span></div>\n'
            '      <div class="vc-zh">%s</div>%s\n'
            '      <ol class="vs-list">%s</ol>\n'
            '    </div>' % (pic, i + 1, E(w['w']), tag, n, E(w['w'], quote=True), E(senses_pos(w)), E(zh_all(w)), forms,
                           ''.join(lis)))


SLIDE_CSS = '''
.lw{display:grid;grid-template-columns:30% 1fr;gap:calc(var(--u)*2);align-items:start}
.lw .lp{font-size:calc(var(--u)*9);text-align:center;line-height:1.1}
.lw img.lp{width:100%;height:auto;aspect-ratio:4/3;object-fit:cover;border-radius:calc(var(--u)*.8);display:block}
.lw .lword{font-family:Georgia,serif;font-size:calc(var(--u)*3.6);font-weight:700;color:var(--deep);text-align:center;margin-top:calc(var(--u)*.6)}
.lw .lforms{font-size:calc(var(--u)*1.2);color:var(--ink-soft);text-align:center}
.ls{display:flex;flex-direction:column;gap:calc(var(--u)*.7)}
.ls .li{background:#fff;border:1px solid var(--line);border-radius:calc(var(--u)*.8);padding:calc(var(--u)*.6) calc(var(--u)*1)}
.ls .lh{font-size:calc(var(--u)*1.6);font-weight:700;color:var(--ink)}
.ls .lh .t{font-size:.75em;color:#fff;background:#5B7C6A;border-radius:calc(var(--u)*.4);padding:0 calc(var(--u)*.5);margin-right:calc(var(--u)*.5)}
.ls .lh .p{font-size:.75em;font-weight:500;color:#8A5A12;background:#FBEFD5;border-radius:calc(var(--u)*.4);padding:0 calc(var(--u)*.5);margin-left:calc(var(--u)*.5)}
.ls .le{font-size:calc(var(--u)*1.45);color:var(--ink);margin-top:calc(var(--u)*.2)}
.ls .lz{font-size:calc(var(--u)*1.25);color:var(--ink-soft)}
@media (max-width:760px){.lw{grid-template-columns:1fr}.lw .lp{font-size:56px}.lw .lword{font-size:28px}.ls .lh{font-size:16px}.ls .le{font-size:15px}.ls .lz{font-size:13px}}
'''


def word_slide(i, w, tag):
    ph = BV.photo(tag, w)
    pic = ('<img class="lp" src="%s" alt="%s">' % (ph, E(w['w'], quote=True)) if ph
           else '<div class="lp">%s</div>' % w['pic'])
    left = '<div>%s<div class="lword">%s %s</div>%s</div>' % (
        pic, E(w['w']), btn(w['w']), '<div class="lforms">%s</div>' % E(w['forms']) if w.get('forms') else '')
    items = []
    for s in w['senses']:
        p = '<span class="p">%s</span>' % E(s['ph']) if s.get('ph') else ''
        items.append('<div class="li"><div class="lh"><span class="t">%s</span>%s%s</div>'
                     '<div class="le">%s %s</div><div class="lz">%s</div></div>'
                     % (E(s['pos']), E(s['zh']), p, E(s['ex']), btn(s.get('exsay', s['ex'])), E(s['exzh'])))
    kind = '主題單字' if w.get('key') else '更多單字'
    return section('%d. %s　<small>%s．%d 個意思</small>' % (i + 1, E(w['w']), kind, len(w['senses'])),
                   '<div class="lw">%s<div class="ls">%s</div></div>' % (left, ''.join(items)))


def slides(u, tag):
    ws = u['words']
    S = [section('本單元單字一覽', lead(E(u['intro'])) + '<div class="chips">%s</div>'
                 % ''.join('<span class="chip">%s</span>' % E(w['w']) for w in ws) +
                 note('每個字先聽 🔊，再一個意思一個意思看例句。'))]
    S += [word_slide(i, w, tag) for i, w in enumerate(ws)]
    for f in BV.focus_items(u):
        body = table(f['head'], [[E(c) for c in r] for r in f['rows']])
        S.append(section(f['title'], body + (note(E(f['note'])) if f.get('note') else '')))
    # 快問快答：看例句猜意思（每個字挑一個「容易忽略」的意思＝第 2 個以後）
    picks = [(w, w['senses'][-1] if len(w['senses']) > 1 else w['senses'][0]) for w in ws]
    picks = picks[::max(1, len(picks) // 16)][:16]
    half = 8 if len(picks) > 8 else (len(picks) + 1) // 2
    S.append(section('快問快答：這句的 %s 是什麼意思？' % '粗體字',
                     qas([(_bold(s['ex'], w['w']), s['zh']) for w, s in picks[:half]])))
    S.append(section('快問快答：這句的 %s 是什麼意思？' % '粗體字',
                     qas([(_bold(s['ex'], w['w']), s['zh']) for w, s in picks[half:]])))
    S.append(section('學完了！接下來', two(card('複習方法', ul([
        '回到「📗 單字卡」，按「遮中文」，看例句說出每個意思',
        '特別記「容易忽略的意思」（例如 pen 圍欄、ball 舞會）',
        '每個例句跟著 🔊 唸一次']), sub='review'),
        card('準備好了', ul(['按右上角「📝 前往測驗」', '測驗錯的題目要訂正到全對', '訂正完成補送 1 點']), 'o'))))

    head = BV.read(os.path.join(BV.C2, 'slides_head.html'))
    tail = BV.read(os.path.join(BV.C2, 'slides_tail.html'))
    book_name = BV.BOOKS['lala']
    reps = [
        ('第二期 WEEK 14 投影片｜分詞構句、連接詞與轉折語', '單字區 %s Unit %d 投影片｜%s %s' % (book_name, u['no'], u['en'], u['zh'])),
        ('<div class="eyebrow">WEEK 14 · SLIDES</div>', '<div class="eyebrow">LALA WORD UNIT %d · SLIDES</div>' % u['no']),
        ('<h1 class="page">分詞構句、連接詞與轉折語</h1>', '<h1 class="page">%s %s</h1>' % (E(u['en']), u['zh'])),
        ('<a class="home-link" href="../index.html">🏠 回總目錄</a>',
         '<a class="home-link" href="../index.html">← 單字區目錄</a>\n    <a class="home-link" href="%s.html">📗 單字卡</a>' % tag),
        ('<a class="quiz-link" href="quiz.html">📝 前往測驗</a>', '<a class="quiz-link" href="%s-quiz.html">📝 前往測驗</a>' % tag),
    ]
    for a, b in reps:
        assert a in head, a
        head = head.replace(a, b)
    head = head.replace('</style>', SLIDE_CSS + '</style>', 1)
    tail = tail.replace("new Audio('audio/slide-'", "new Audio('audio/%s/slide-'" % tag)
    title = ('<section class="s dark title"><div class="week">LALA WORD · UNIT %d</div><h1 class="big">%s</h1>'
             '<div class="en-sub">%s</div><div class="venn"><span class="c1">%d 個單字</span><span class="c2">一字多義</span></div></section>'
             % (u['no'], u['zh'], E(u['en']), len(ws)))
    return head + '\n'.join([title] + S) + tail


def _bold(ex, word):
    """例句裡把這個字（含變化形）標粗體。"""
    pat = re.compile(r'\b(%s\w*)\b' % re.escape(word), re.I)
    e = E(ex)
    return pat.sub(r'<b>\1</b>', e, count=1) if pat.search(e) else e


def build(mod):
    u, quiz = mod.UNIT, mod.QUIZ
    no = u['no']
    BV.CUR['book'] = 'lala'
    tag = 'u%02d' % no
    out = os.path.join(BV.REPO, 'vocab', 'lala')
    fmt = dict(book=BV.BOOKS['lala'], bookup='LALA WORD', no=no, en=E(u['en']), zh=E(u['zh']), intro=E(u['intro']), tag=tag,
               n=len(u['words']))
    cards_page = BV.CARDS_TPL.format(cards='\n'.join(card_html(i, w, tag) for i, w in enumerate(u['words'])),
                                     focus=BV.focus_html(u), **fmt)
    cards_page = cards_page.replace('</head>', '<style>%s</style>\n</head>' % LALA_CSS, 1)
    BV.write(os.path.join(out, tag + '.html'), cards_page)
    page, keep = link_slide_audio.link(slides(u, tag), link_slide_audio.card_map(cards_page))
    BV.write(os.path.join(out, tag + '-slides.html'), page)
    # 測驗：「<b>字</b>」題目記下考哪個字（學習進度用）
    for sec in quiz:
        for it in sec['items']:
            m = re.search(r'<b>([A-Za-z]+)</b>', it.get('q', ''))
            if m and 'w' not in it:
                word = m.group(1).lower()
                it['w'] = next((w['w'] for w in u['words'] if word.startswith(w['w'].lower())), word)
    data = {'label': 'Vocab LALA U%d' % no, 'title': '單字區 %s Unit %d %s' % (BV.BOOKS['lala'], no, u['zh']),
            'back': tag + '.html', 'sections': quiz}
    qpage = BV.QUIZ_TPL.format(data=json.dumps(data, ensure_ascii=False, indent=1), **fmt)
    qpage = qpage.replace('看中文選英文 → 看英文選中文 → 拼字 → 例句填空。', '看句子選意思 → 一字填兩句 → 例句填空。')
    BV.write(os.path.join(out, tag + '-quiz.html'), qpage)
    adir = os.path.join(out, 'audio', tag)
    jobs = []
    for i, w in enumerate(u['words']):
        jobs.append([w['w'], os.path.join(adir, 'w-%02d.mp3' % (i + 1))])
        for k, s in enumerate(w['senses'], 1):
            jobs.append([s.get('exsay', s['ex']), os.path.join(adir, 'e-%02d-%d.mp3' % (i + 1, k))])
    jobs += [[s, os.path.join(adir, 'slide-%02d.mp3' % i)] for i, s in keep]
    return jobs


if __name__ == '__main__':
    jobs = []
    for m in UNITS:
        j = build(m)
        print('LaLa Word Unit %d：%d 個音檔' % (m.UNIT['no'], len(j)))
        jobs += j
    with open(os.path.join(HERE, 'audio_jobs.json'), 'w', encoding='utf-8') as f:
        json.dump(jobs, f, ensure_ascii=False, indent=0)
