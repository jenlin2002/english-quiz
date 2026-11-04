"""把讀到的 WORD UP 資料寫成 vocab/wordup/status.json。
輸入：每個學生一個文字檔（家長登入 WORD UP 後由 Claude 讀取），每行一個單元：
  單元名|熟記/不太熟/很模糊/沒印象（WORD UP 側欄的數字）|單字~等級[*],…   等級 0 熟記 1 不太熟 2 很模糊 3 沒印象，* 星號
  單元名|0/0/0/N|U|單字,…                                           U＝還沒開始背的單元（只記字表）
還沒開始背的單元（熟記、不太熟、很模糊都是 0）只記字表，不記熟悉度（不然整個單元都會被標成紅色）。
用法：python tools/vocab_gen/build_wordup_status.py BRANDEN=路徑 MELISSA=路徑
  沒給檔案的學生，保留 status.json 裡原本的資料。"""
import json, os, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'vocab', 'wordup', 'status.json')
LV = ['熟記', '不太熟', '很模糊', '沒印象']

old = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {'units': {}, 'users': {}}
units, users = {}, dict(old.get('users', {}))
for arg in sys.argv[1:]:
    who, path = arg.split('=', 1)
    words, studied = {}, []
    for k, line in enumerate(l.strip() for l in open(path, encoding='utf-8-sig')):
        if not line:
            continue
        p = line.split('|')
        name, side = p[0], list(map(int, p[1].split('/')))
        tag = 'u%02d' % (len(units) + 1) if name not in [u['name'] for u in units.values()] else None
        if p[2] == 'U':
            ws = p[3].split(',')
        else:
            ws = [x.split('~')[0] for x in p[2].split(',')]
            if sum(side[:3]) > 0:   # 有開始背的單元才記熟悉度
                studied.append(name)
                for x in p[2].split(','):
                    w, lv = x.split('~')
                    words[w] = [LV[int(lv.rstrip('*'))], 1 if lv.endswith('*') else 0]
        if tag:
            units[tag] = {'name': name, 'words': list(dict.fromkeys(ws))}
    users[who] = {'updated': datetime.date.today().isoformat(), 'studied': studied, 'words': words}
if not units:
    units = old.get('units', {})
data = {'note': old.get('note', ''), 'units': units, 'users': users}
with open(OUT, 'w', encoding='utf-8', newline='\n') as f:
    f.write('{\n "note": %s,\n "units": {\n' % json.dumps(data['note'], ensure_ascii=False))
    f.write(',\n'.join('  "%s": %s' % (t, json.dumps(u, ensure_ascii=False)) for t, u in units.items()))
    f.write('\n },\n "users": {\n')
    f.write(',\n'.join('  "%s": %s' % (n, json.dumps(u, ensure_ascii=False)) for n, u in users.items()))
    f.write('\n }\n}\n')
for n, u in users.items():
    print(n, '已背單元', len(u.get('studied', [])), '個，記錄', len(u['words']), '個字')
print('單元', len(units), '個，共', sum(len(u['words']) for u in units.values()), '個字')
