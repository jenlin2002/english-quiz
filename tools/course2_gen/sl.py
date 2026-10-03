"""Tiny helpers that emit slide markup in the same shape as course2/w14/slides.html."""
import html, re, os

GEN = os.path.dirname(os.path.abspath(__file__))


def _say(en):
    t = re.sub(r'<[^>]+>', '', en)
    t = html.unescape(t)
    return re.sub(r'\s+', ' ', t).strip()


def btn(say):
    return ('<button class="sentence-btn" type="button" data-say="%s" aria-label="播放這個句子">🔊</button>'
            % html.escape(say, quote=True))


def ex(en, zh='', cls='g'):
    z = '<div class="zh">%s</div>' % zh if zh else ''
    return '<div class="ex %s"><div class="en">%s %s</div>%s</div>' % (cls, en, btn(_say(en)), z)


def card(h3, body, cls='g', sub=''):
    s = '<div class="sub">%s</div>' % sub if sub else ''
    return '<div class="card %s"><h3>%s</h3>%s%s</div>' % (cls, h3, s, body)


def row(label, text):
    return '<p class="row"><b>%s</b>%s</p>' % (label, text)


def ul(items):
    return '<ul class="b">%s</ul>' % ''.join('<li>%s</li>' % i for i in items)


def ol(items):
    return '<ol class="b">%s</ol>' % ''.join('<li>%s</li>' % i for i in items)


def cards(n, *cs, tight=False):
    return '<div class="cards n%d%s">%s</div>' % (n, ' tight' if tight else '', ''.join(cs))


def two(a, b, tight=False):
    return '<div class="two%s">%s%s</div>' % (' tight' if tight else '', a, b)


def div(*xs):
    return '<div>%s</div>' % ''.join(xs)


def note(t):
    return '<div class="note">%s</div>' % t


def lead(t):
    return '<p class="lead">%s</p>' % t


def qas(items):
    out = []
    for i, (q, a) in enumerate(items, 1):
        out.append('<div class="qa"><span class="n">%d</span><span class="q">%s</span>'
                   '<button class="rv" type="button">看答案</button><span class="ans" hidden>%s</span></div>' % (i, q, a))
    return '<div class="qas">%s</div>' % ''.join(out)


def table(head, rows, audio_col=None):
    """rows: list of lists; if audio_col given, that column is (en, zh) and gets a play button."""
    th = ''.join('<th>%s</th>' % h for h in head)
    trs = []
    for r in rows:
        tds = []
        for ci, c in enumerate(r):
            if ci == audio_col:
                en, zh = c
                tds.append('<td><div>%s %s <span style="color:var(--ink-soft);font-size:.9em">（%s）</span></div></td>'
                           % (en, btn(_say(en)), zh))
            else:
                tds.append('<td>%s</td>' % c)
        trs.append('<tr>%s</tr>' % ''.join(tds))
    return '<table class="t"><thead><tr>%s</tr></thead><tbody>%s</tbody></table>' % (th, ''.join(trs))


def top5(items):
    out = []
    for i, (bad, good, why) in enumerate(items, 1):
        out.append('<div class="t5"><span class="rank">%d</span><div><div class="en"><span class="bad">%s</span> → '
                   '<span class="good">%s</span></div><div class="why">%s</div></div></div>' % (i, bad, good, why))
    return '<div class="top5">%s</div>' % ''.join(out)


def passage(en_html):
    return '<div class="card"><div class="ex"><div class="en">%s%s</div></div></div>' % (en_html, btn(_say(en_html)))


def section(h2, body, cls='paper'):
    return '<section class="s %s"><h2>%s</h2>%s</section>' % (cls, h2, body)


def title(week_no, zh, en, c1, c2):
    return ('<section class="s dark title"><div class="week">WEEK %d · GRAMMAR</div><h1 class="big">%s</h1>'
            '<div class="en-sub">%s</div><div class="venn"><span class="c1">%s</span><span class="c2">%s</span></div></section>'
            % (week_no, zh, en, c1, c2))


def build(week_no, zh_title, sections, out_dir):
    head = open(os.path.join(GEN, 'slides_head.html')).read()
    tail = open(os.path.join(GEN, 'slides_tail.html')).read()
    head = head.replace('第二期 WEEK 14 投影片｜分詞構句、連接詞與轉折語', '第二期 WEEK %d 投影片｜%s' % (week_no, zh_title))
    head = head.replace('<div class="eyebrow">WEEK 14 · SLIDES</div>', '<div class="eyebrow">WEEK %d · SLIDES</div>' % week_no)
    head = head.replace('<h1 class="page">分詞構句、連接詞與轉折語</h1>', '<h1 class="page">%s</h1>' % zh_title)
    assert 'WEEK 14' not in head and '分詞構句' not in head, 'head replace failed'
    body = '\n'.join(sections)
    page = head + body + tail
    os.makedirs(out_dir, exist_ok=True)
    open(os.path.join(out_dir, 'slides.html'), 'w').write(page)
    says = [html.unescape(m) for m in re.findall(r'class="sentence-btn" type="button" data-say="([^"]*)"', body)]
    return says
