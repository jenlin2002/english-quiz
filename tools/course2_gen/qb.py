"""Build a course2 quiz page from the week 14 template plus a week's data block."""
import os, re, sys

GEN = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'course2')


def build(week_no, title, data_file, out_dir, review=False, seed=None):
    t = open(os.path.join(REPO, 'w14/quiz.html')).read()
    old_title = '分詞構句、連接詞與轉折語'

    def rep(old, new, count=1):
        nonlocal t
        assert t.count(old) == count, (old, t.count(old))
        t = t.replace(old, new)

    rep('<title>英文測驗系統｜第二期第 14 週：%s</title>' % old_title,
        '<title>英文測驗系統｜第二期第 %d 週：%s</title>' % (week_no, title))
    rep('<div class="eyebrow">Course II · Week 14 · Test System</div>',
        '<div class="eyebrow">Course II · Week %d · %s</div>' % (week_no, 'Review' if review else 'Test System'))
    rep('<h1 class="board-title" id="mainTitle">%s</h1>' % old_title,
        '<h1 class="board-title" id="mainTitle">%s</h1>' % title)
    rep('const WEEK_LABEL = "II Week 14";', 'const WEEK_LABEL = "II Week %d";' % week_no)
    rep("grammar: { questions: GRAMMAR_QUESTIONS, title: '%s'," % old_title,
        "grammar: { questions: GRAMMAR_QUESTIONS, title: '%s'," % title)
    rep('const rnd = mulberry32(20261003);', 'const rnd = mulberry32(%d);' % (seed or (20261000 + week_no)))

    a = t.index('const GRAMMAR_QUESTIONS = [')
    b = t.index('// ---- 選項重新排列')
    data = open(os.path.join(GEN, data_file)).read().strip() + '\n\n'
    t = t[:a] + data + t[b:]

    checks = open(os.path.join(GEN, 'checks.js')).read().rstrip('\n') + '\n'
    rep("  } else if(q.checkType === 'perfect'){", checks + "  } else if(q.checkType === 'perfect'){")
    assert old_title not in t
    os.makedirs(out_dir, exist_ok=True)
    open(os.path.join(out_dir, 'quiz.html'), 'w').write(t)
    return t
