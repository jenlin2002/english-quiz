"""主題 2000 字 PART 2 資料檔共用小工具（2026-11-22）。
W(...) 建一個字；auto_quiz(words, fill, ...) 自動產生「看中文選英文、看英文選中文、拼字」三段，再接手寫的例句填空題。
干擾選項從同一單元挑（同一單元不到 4 個字時從 POOL 補），用固定亂數種子，重跑結果一樣。"""
import random

# 單元字太少時補干擾選項用（PART 1／PART 2 常見字，字＋簡短中文）
POOL = [('teacher', '老師'), ('window', '窗戶'), ('happy', '快樂的'), ('river', '河流'), ('money', '錢'), ('kitchen', '廚房'),
        ('borrow', '借入'), ('quickly', '快速地'), ('friend', '朋友'), ('weather', '天氣'), ('library', '圖書館'), ('dangerous', '危險的'),
        ('finish', '完成'), ('travel', '旅行'), ('history', '歷史'), ('village', '村莊')]


def W(w, pos, zh, note, ex, exzh, pic, **kw):
    d = {'w': w, 'pos': pos, 'zh': zh, 'note': note, 'ex': ex, 'exzh': exzh, 'pic': pic}
    d.update(kw)
    return d


def short(zh):
    """選項用的簡短中文：取第一個「；」前面。"""
    return zh.split('；')[0].split('（')[0]


def _pool(words):
    have = {w['w'].lower() for w in words}
    return [(w['w'], short(w['zh'])) for w in words] + [p for p in POOL if p[0] not in have]


def auto_quiz(words, fill=None, seed=1, n_ce=6, n_ec=5, n_sp=5, extra=None):
    rnd = random.Random(seed)
    pool = _pool(words)
    secs = []
    pick = list(words)
    rnd.shuffle(pick)
    def others_for(w):
        # 干擾選項：不能是同一個字，也不能和正解的簡短中文一樣（同義字會變成兩個正解）
        o = [p for p in pool if p[0] != w['w'] and p[1] != short(w['zh'])]
        unit = [p for p in o if p[0] in {x['w'] for x in words}]
        return unit if len(unit) >= 3 else o

    def pick3(w):
        # 三個干擾選項彼此的中文也不能一樣（例如 neither、nor 都是「也不」）
        cand = others_for(w)[:]
        rnd.shuffle(cand)
        out, seen = [], set()
        for p in cand:
            if p[1] in seen:
                continue
            out.append(p); seen.add(p[1])
            if len(out) == 3:
                break
        return out
    ce = []
    for w in pick[:n_ce]:
        opts = pick3(w) + [(w['w'], short(w['zh']))]
        rnd.shuffle(opts)
        ce.append({'type': 'mc', 'q': w['zh'], 'opts': [o[0] for o in opts], 'answer': [o[0] for o in opts].index(w['w']),
                   'exp': '%s %s。' % (w['w'], w['zh'])})
    if ce:
        secs.append({'title': '看中文選英文', 'items': ce})
    rnd.shuffle(pick)
    ec = []
    for w in pick[:n_ec]:
        opts = pick3(w) + [(w['w'], short(w['zh']))]
        rnd.shuffle(opts)
        ec.append({'type': 'mc', 'q': w['w'], 'opts': [o[1] for o in opts], 'answer': [o[0] for o in opts].index(w['w']),
                   'exp': '%s %s。' % (w['w'], w['zh'])})
    if ec:
        secs.append({'title': '看英文選中文', 'items': ec})
    rnd.shuffle(pick)
    sp = []
    for w in [x for x in pick if ' ' not in x['w'] and "'" not in x['w'] and '.' not in x['w']][:n_sp]:
        n = len(w['w'])
        sp.append({'q': '%s（%s%s，%d 個字母）：{0}' % (short(w['zh']), w['w'][0], '＿' * (n - 1), n),
                   'blanks': [[w['w']]], 'exp': '%s。' % w['w']})
    if sp:
        secs.append({'title': '拼字：看中文和提示，寫出整個單字', 'note': '括號裡是第一個字母和字母數。', 'items': sp})
    for s in (extra or []):
        secs.append(s)
    if fill:
        secs.append({'title': '例句填空：選出最合適的單字', 'items': fill})
    num = '①②③④⑤⑥⑦⑧'
    return [dict(s, title='%s %s' % (num[i], s['title'])) for i, s in enumerate(secs)]


def F(q, opts, answer, exp):
    """手寫的例句填空選擇題。"""
    return {'type': 'mc', 'q': q, 'opts': opts, 'answer': answer, 'exp': exp}
