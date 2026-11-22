"""檢查主題 2000 字 PART 2 資料檔：字有沒有重複、測驗選項是否重複、答案索引是否合理、填空題的正解是不是本單元的字。
用法：python tools/vocab_gen/p2_check.py"""
import glob, importlib, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.stdout.reconfigure(encoding='utf-8')
bad = 0
seen = {}
for f in sorted(glob.glob(os.path.join(HERE, 'w2000p2_u[0-9][0-9]*.py'))):
    m = importlib.import_module(os.path.basename(f)[:-3])
    no = m.UNIT['no']
    ws = [w['w'] for w in m.UNIT['words']]
    for w in m.UNIT['words']:
        for k in ('w', 'pos', 'zh', 'ex', 'exzh', 'pic'):
            if not w.get(k):
                print('U%d %s 缺 %s' % (no, w.get('w'), k)); bad += 1
        if w['w'].lower() in seen:
            print('U%d %s 和 U%d 重複' % (no, w['w'], seen[w['w'].lower()]))
        seen[w['w'].lower()] = no
    n = 0
    for s in m.QUIZ:
        for it in s['items']:
            n += 1
            if it.get('type') == 'mc':
                o = it['opts']
                if len(set(o)) != len(o) or not (0 <= it['answer'] < len(o)):
                    print('U%d 選項重複或答案錯：%s %s' % (no, it['q'], o)); bad += 1
                if '______' in it['q'] and it['q'].count('______') != 1:
                    print('U%d 空格數不對：%s' % (no, it['q'])); bad += 1
            else:
                if it['q'].count('{') != len(it['blanks']):
                    print('U%d 填空數不對：%s' % (no, it['q'])); bad += 1
    print('U%02d：%d 字、%d 題' % (no, len(ws), n))
print('問題', bad)
