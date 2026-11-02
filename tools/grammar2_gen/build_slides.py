"""產生國中文法分科區的投影片 grammar2/uNN-slides.html，並輸出要錄音的句子清單 audio_jobs.json。

沿用第二期 tools/course2_gen 的投影片樣式（slides_head.html、slides_tail.html）與小工具 sl.py。
執行：python tools/grammar2_gen/build_slides.py
錄音：python tools/course2_gen/tts.py tools/grammar2_gen/audio_jobs.json
     （mp3 放在 grammar2/audio/uNN/slide-NN.mp3，NN 依 🔊 按鈕出現的順序；沒有 mp3 時頁面會改用瀏覽器語音）
"""
import html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
C2 = os.path.join(REPO, 'tools', 'course2_gen')
sys.path.insert(0, C2)
from sl import ex, card, row, ul, cards, two, div, note, lead, qas, table, top5, section  # noqa: E402

sys.path.insert(0, HERE)
from u01_slides import UNIT as U01  # noqa: E402
from u02_slides import UNIT as U02  # noqa: E402

OUT = os.path.join(REPO, 'grammar2')


def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def title_slide(no, zh, en, c1, c2):
    return ('<section class="s dark title"><div class="week">UNIT %d · GRAMMAR</div><h1 class="big">%s</h1>'
            '<div class="en-sub">%s</div><div class="venn"><span class="c1">%s</span><span class="c2">%s</span></div></section>'
            % (no, zh, en, c1, c2))


def build(unit):
    no, zh = unit['no'], unit['zh']
    tag = 'u%02d' % no
    head = read(os.path.join(C2, 'slides_head.html'))
    tail = read(os.path.join(C2, 'slides_tail.html'))
    reps = [
        ('第二期 WEEK 14 投影片｜分詞構句、連接詞與轉折語', '國中文法 Unit %d 投影片｜%s' % (no, zh)),
        ('<div class="eyebrow">WEEK 14 · SLIDES</div>', '<div class="eyebrow">GRAMMAR UNIT %d · SLIDES</div>' % no),
        ('<h1 class="page">分詞構句、連接詞與轉折語</h1>', '<h1 class="page">%s</h1>' % zh),
        ('<a class="home-link" href="../index.html">🏠 回總目錄</a>',
         '<a class="home-link" href="index.html">← 國中文法目錄</a>\n    <a class="home-link" href="%s.html">📘 講解</a>' % tag),
        ('<a class="quiz-link" href="quiz.html">📝 前往測驗</a>', '<a class="quiz-link" href="%s-quiz.html">📝 前往測驗</a>' % tag),
    ]
    for a, b in reps:
        assert a in head, 'head 找不到：' + a
        head = head.replace(a, b)
    a = "new Audio('audio/slide-'"
    assert a in tail
    tail = tail.replace(a, "new Audio('audio/%s/slide-'" % tag)
    body = '\n'.join([title_slide(no, zh, unit['en'], unit['c1'], unit['c2'])] + unit['slides'])
    with open(os.path.join(OUT, tag + '-slides.html'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(head + body + tail)
    says = [html.unescape(m) for m in re.findall(r'class="sentence-btn" type="button" data-say="([^"]*)"', body)]
    return [[s, os.path.join(OUT, 'audio', tag, 'slide-%02d.mp3' % (i + 1))] for i, s in enumerate(says)]


if __name__ == '__main__':
    jobs = []
    for u in (U01, U02):
        j = build(u)
        os.makedirs(os.path.join(OUT, 'audio', 'u%02d' % u['no']), exist_ok=True)
        print('Unit %d：%d 頁、%d 句' % (u['no'], len(u['slides']) + 1, len(j)))
        jobs += j
    with open(os.path.join(HERE, 'audio_jobs.json'), 'w', encoding='utf-8') as f:
        json.dump(jobs, f, ensure_ascii=False, indent=0)
