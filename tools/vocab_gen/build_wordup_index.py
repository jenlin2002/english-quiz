"""產生 vocab/wordup/index.html：WORD UP 單字 A–Z 對照表。
讀 vocab/wordup/status.json 的單元字表，對到主題 2000 字（vocab/w2000/uNN.html 的 .vc-word）在哪個單元；
登入者的熟悉度由頁面上的 JS 讀 status.json＋本站答題紀錄（vocabWords）顯示。
執行：python tools/vocab_gen/build_wordup_index.py（WORD UP 新增單元或主題單元做好後重跑）"""
import glob, html, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
VOC = os.path.join(REPO, 'vocab')
E = html.escape

status = json.load(open(os.path.join(VOC, 'wordup', 'status.json'), encoding='utf-8'))
where = {}   # 小寫單字 → [(單元號, 單元名)]
for p in sorted(glob.glob(os.path.join(VOC, 'w2000', 'u[0-9][0-9].html'))):
    s = open(p, encoding='utf-8').read()
    no = int(re.search(r'u(\d\d)\.html$', p).group(1))
    title = re.search(r'<h1>(.*?)</h1>', s, re.S).group(1)
    for w in re.findall(r'<span class="vc-word">(.*?)</span>', s):
        where.setdefault(html.unescape(w).lower(), []).append((no, html.unescape(re.sub('<.*?>', '', title))))

rows, units = [], []
for tag, u in status['units'].items():
    built = os.path.exists(os.path.join(VOC, 'wordup', tag + '.html'))   # 已做好的 WORD UP 複習單元
    if built:
        units.append('<a class="btn" href="%s.html">📗 WORD UP %s</a>' % (tag, E(u['name'])))
    links = '　<a href="%s.html">單字卡</a>．<a href="%s-quiz.html">測驗</a>' % (tag, tag) if built else '　<span class="soon">（複習單元製作中）</span>'
    rows.append('<tr class="grp"><td colspan="4">WORD UP 單元 %s（%d 個字）%s</td></tr>' % (E(u['name']), len(u['words']), links))
    for w in u['words']:
        hits = where.get(w.lower(), [])
        ours = '、'.join('<a href="../w2000/u%02d.html">Unit %d %s</a>' % (no, no, E(t.split('．')[-1])) for no, t in hits) \
            or '<span class="only">%s</span>' % ('只在 WORD UP 複習區' if built else '本站還沒有')
        word = '<a href="%s.html">%s</a>' % (tag, E(w)) if built else E(w)
        rows.append('<tr data-w="%s"><td class="w">%s</td><td class="lv"></td><td class="lv2"></td><td>%s</td></tr>' % (E(w.lower(), quote=True), word, ours))

page = '''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>單字區｜WORD UP 單字 A–Z 對照表</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Kalam:wght@400;700&family=Noto+Sans+TC:wght@400;500;700;900&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../grammar2/grammar.css?v=20261102">
<style>
  table.az{ width:100%%; border-collapse:collapse; background:#FFFDF6; border-radius:12px; overflow:hidden; }
  table.az td{ padding:8px 12px; border-bottom:1px solid #EFE6CC; color:#2B2B2B; }
  table.az tr.grp td{ background:#1F3A2E; color:#F6E7B4; font-weight:700; }
  table.az tr.grp a{ color:#FFD66B; }
  table.az td.w{ font-family:Georgia,serif; font-size:18px; font-weight:700; }
  table.az td.w a{ color:#1F3A2E; text-decoration:none; }
  .only{ color:#8A7D62; }
  .soon{ color:#F6E7B4; opacity:.75; font-weight:400; }
  .lv small, .lv2 small{ color:#8A7D62; margin-right:4px; }
  .lv span{ display:inline-block; padding:2px 10px; border-radius:999px; font-size:13px; font-weight:700; }
  .lv .r, .lv2 .r{ background:#FDECEC; color:#C62828; } .lv .g, .lv2 .g{ background:#E6E6E6; color:#555; }
  .lv .n, .lv2 .n{ background:#E8EEF6; color:#3B5B85; }
  .lv span, .lv2 span{ display:inline-block; padding:2px 10px; border-radius:999px; font-size:13px; font-weight:700; }
  .az-sum{ margin:8px 0 14px; padding:10px 14px; border-radius:10px; background:#FFF8E6; color:#3A3226; font-weight:700; }
</style>
</head>
<body>
<div class="wrap">
  <div class="top-links"><a class="home-link" href="../index.html">← 單字區目錄</a></div>
  <div class="eyebrow">VOCABULARY · WORD UP</div>
  <h1>WORD UP 單字 A–Z 對照表</h1>
  <div class="subtitle">孩子在 WORD UP（全民英檢初級單字一本通）背的字，對照到本站「主題 2000 字」的單元。<br>
  以本站測驗結果為準：灰＝本站答對（已會）、紅＝要複習（本站答錯或 WORD UP 標不熟）、藍＝WORD UP 自己標熟記，還要本站考對才算會。</div>
  <div class="unit-btns">%s</div>
  <div class="az-sum" id="azSum">登入後會顯示你的熟悉度。</div>
  <table class="az">%s</table>
  <div class="footer-note">只使用 WORD UP 的英文字表與孩子的熟悉度紀錄；本站的中文、例句、題目、語音都是自編。</div>
</div>
<script>
// 學生看自己的一欄；家長 PARENT／TEST 看 BRANDEN、MELISSA 兩欄
(async function(){
  let name = '';
  try{ name = (localStorage.getItem('quizStudentName') || '').trim().toUpperCase(); }catch(e){}
  if(!name) return;
  const people = /^(PARENT|TEST)$/.test(name) ? ['BRANDEN', 'MELISSA'] : [name];
  let wu = {};
  try{ wu = await (await fetch('status.json', { cache:'no-cache' })).json(); }catch(e){}
  const all = document.querySelectorAll('tr[data-w]');
  const sums = people.map((p, k) => {
    const m = new Map(), u = (wu.users || {})[p];
    // WORD UP 熟記只是參考（n，藍）；只有本站測驗答對（g，灰）才算已會
    if(u) Object.keys(u.words).forEach(w => m.set(w.toLowerCase(), u.words[w][0] === '熟記' ? ['n', 'WORD UP 熟記（待測驗）'] : ['r', 'WORD UP：' + u.words[w][0]]));
    try{ const mine = JSON.parse(localStorage.getItem('vocabWords:' + p) || '{}'); Object.keys(mine).forEach(w => m.set(w, mine[w] === 'm' ? ['g', '本站答對'] : ['r', '本站答錯'])); }catch(e){}
    const c = { r: 0, g: 0, n: 0 };
    all.forEach(tr => {
      const s = m.get(tr.dataset.w);
      if(!s) return;
      c[s[0]]++;
      tr.querySelector(k ? '.lv2' : '.lv').innerHTML = (people.length > 1 ? '<small>' + p + '</small> ' : '') + '<span class="' + s[0] + '">' + s[1] + '</span>';
    });
    return p + '：本站答對（已會）' + c.g + ' 個、要複習 ' + c.r + ' 個、WORD UP 熟記待測驗 ' + c.n + ' 個、還沒背 ' + (all.length - c.g - c.r - c.n) + ' 個';
  });
  document.getElementById('azSum').innerHTML = sums.join('<br>') + '<br><small>（共 ' + all.length + ' 個字）</small>';
})();
</script>
</body>
</html>
''' % (''.join(units), '\n'.join(rows))
open(os.path.join(VOC, 'wordup', 'index.html'), 'w', encoding='utf-8', newline='\n').write(page)
print('wordup index：%d 個字，%d 個對到主題單元' % (sum(len(u['words']) for u in status['units'].values()),
      sum(1 for u in status['units'].values() for w in u['words'] if w.lower() in where)))
