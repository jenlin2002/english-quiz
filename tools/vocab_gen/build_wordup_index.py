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
where = {}   # 小寫單字 → [(資料夾, 單元號, 單元名)]；w2000＝PART 1（1–1200 字），w2000p2＝PART 2（1201–2000 字）
for book in ('w2000', 'w2000p2'):
    for p in sorted(glob.glob(os.path.join(VOC, book, 'u[0-9][0-9]*.html'))):
        m = re.search(r'(u(\d\d)[a-z]?)\.html$', p)   # u34a.html：拆頁的單元
        if not m:
            continue
        s = open(p, encoding='utf-8').read()
        title = re.search(r'<h1>(.*?)</h1>', s, re.S).group(1)
        for w in re.findall(r'<span class="vc-word">(.*?)</span>', s):
            where.setdefault(html.unescape(w).lower(), []).append((book, m.group(1), int(m.group(2)), html.unescape(re.sub('<.*?>', '', title))))

rows, units = [], []
for tag, u in status['units'].items():
    built = os.path.exists(os.path.join(VOC, 'wordup', tag + '.html'))   # 已做好的 WORD UP 複習單元
    if built:
        units.append('<a class="btn" href="%s.html">📗 WORD UP %s</a>' % (tag, E(u['name'])))
    links = '　<a href="%s.html">單字卡</a>．<a href="%s-quiz.html">測驗</a>' % (tag, tag) if built else '　<span class="soon">（複習單元製作中）</span>'
    rows.append('<tr class="grp"><td colspan="4">WORD UP 單元 %s（%d 個字）%s</td></tr>' % (E(u['name']), len(u['words']), links))
    rows.append('<tr class="hd"><td>單字</td><td colspan="2">熟悉度（登入後顯示）</td><td>本站在哪裡複習</td></tr>')
    for w in u['words']:
        hits = where.get(w.lower(), [])
        wu = '<a href="%s.html">WORD UP %s</a>' % (tag, E(u['name'])) if built else '<span class="only">WORD UP %s（製作中）</span>' % E(u['name'])
        ours = '、'.join(['<a href="../%s/%s.html">主題%s Unit %d %s</a>' % (bk, tg, ' PART 2' if bk == 'w2000p2' else '', no, E(t.split('．')[-1])) for bk, tg, no, t in hits] + [wu])
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
  table.az tr.hd td{ background:#F3EBD2; color:#6B5E44; font-size:13px; font-weight:700; padding:5px 12px; }
  .soon{ color:#F6E7B4; opacity:.75; font-weight:400; }
  .lv small, .lv2 small{ color:#8A7D62; margin-right:4px; }
  .lv span{ display:inline-block; padding:2px 10px; border-radius:999px; font-size:13px; font-weight:700; }
  .lv .r, .lv2 .r{ background:#FDECEC; color:#C62828; } .lv .g, .lv2 .g{ background:#E6E6E6; color:#555; }
  .lv .n, .lv2 .n{ background:#E8EEF6; color:#3B5B85; }
  .lv span, .lv2 span{ display:inline-block; padding:2px 10px; border-radius:999px; font-size:13px; font-weight:700; }
  .az-sum{ margin:8px 0 14px; padding:12px 16px; border-radius:10px; background:#FFF8E6; color:#3A3226; font-weight:700; }
  .az-p{ margin-bottom:12px; }
  .az-name{ font-size:16px; margin-bottom:4px; }
  .az-bar{ display:flex; height:30px; border-radius:8px; overflow:hidden; background:#EFE6CC; }
  .az-bar i{ display:flex; align-items:center; justify-content:center; font-style:normal; font-size:13px; font-weight:700; min-width:2px; }
  .az-bar i.g, .az-leg b.g{ background:#8C8C8C; color:#fff; }
  .az-bar i.r, .az-leg b.r{ background:#E05252; color:#fff; }
  .az-bar i.n, .az-leg b.n{ background:#7FA3D1; color:#fff; }
  .az-bar i.e, .az-leg b.e{ background:#E9E0C6; color:#7A6E58; }
  .az-leg{ display:flex; flex-wrap:wrap; gap:4px 14px; margin-top:6px; font-size:13px; font-weight:500; }
  .gp-h{ font-size:20px; margin:22px 0 10px; color:#F6E7B4; }
  .gp-box{ padding:12px 16px; border-radius:10px; background:#FFF8E6; color:#3A3226; }
  .gp-name{ font-weight:700; font-size:16px; margin:6px 0; } .gp-name small{ font-weight:400; color:#8A7D62; margin-left:6px; }
  .gp-scroll{ overflow-x:auto; margin-bottom:10px; }
  table.gp{ width:100%%; border-collapse:collapse; background:#FFFDF6; min-width:480px; }
  table.gp td{ padding:7px 10px; border-bottom:1px solid #EFE6CC; vertical-align:top; }
  table.gp td:first-child{ white-space:nowrap; }
  table.gp tr.hd td{ background:#F3EBD2; color:#6B5E44; font-size:13px; font-weight:700; }
  table.gp small{ color:#8A7D62; margin-left:4px; }
  .gp-parts{ font-size:12px; color:#8A7D62; margin-top:2px; }
  .gp-good{ color:#2E7D32; } .gp-mid{ color:#B26A00; } .gp-low{ color:#C62828; } .gp-no, .gp-none{ color:#A89C80; }
  .gp-note{ font-size:12px; color:#8A7D62; }
  .az-leg b{ display:inline-block; width:12px; height:12px; border-radius:3px; margin-right:5px; vertical-align:-1px; }
</style>
</head>
<body>
<div class="wrap">
  <div class="top-links"><a class="home-link" href="units.html">← WORD UP 目錄</a></div>
  <div class="eyebrow">VOCABULARY · WORD UP</div>
  <h1>WORD UP 單字 A–Z 對照表</h1>
  <div class="subtitle">孩子在 WORD UP（全民英檢初級單字一本通）背的字，對照到本站「主題 2000 字」的單元。<br>
  以本站測驗結果為準：灰＝本站答對（已會）、紅＝要複習（本站答錯或 WORD UP 標不熟）、藍＝WORD UP 自己標熟記，還要本站考對才算會。</div>
  <div class="unit-btns">%s</div>
  <div class="az-sum" id="azSum">登入後會顯示你的熟悉度。</div>
  <h2 class="gp-h">📝 GEPT 初級模擬試題成績（WORD UP 10 回）</h2>
  <div id="gept" class="gp-box">登入後會顯示 GEPT 模擬試題成績。</div>
  <h2 class="gp-h">🔤 單字 A–Z 對照表</h2>
  <table class="az">%s</table>
  <div class="footer-note">只使用 WORD UP 的英文字表、孩子的熟悉度紀錄與模擬試題答對題數；本站的中文、例句、題目、語音都是自編。</div>
</div>
<script src="/dict/dict.js?v=20261118a" defer></script>
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
    // 堆疊柱狀圖：已會（灰）、要複習（紅）、WORD UP 熟記待測驗（藍）、還沒背（淺色）
    const parts = [['g', '本站答對（已會）', c.g], ['r', '要複習', c.r], ['n', 'WORD UP 熟記待測驗', c.n], ['e', '還沒背', all.length - c.g - c.r - c.n]];
    return '<div class="az-p"><div class="az-name">' + p + '</div><div class="az-bar">' +
      parts.filter(x => x[2]).map(x => '<i class="' + x[0] + '" style="flex:' + x[2] + '" title="' + x[1] + ' ' + x[2] + ' 個">' +
        (x[2] / all.length > 0.06 ? x[2] : '') + '</i>').join('') + '</div><div class="az-leg">' +
      parts.map(x => '<span><b class="' + x[0] + '"></b>' + x[1] + ' ' + x[2] + ' 個（' + Math.round(x[2] / all.length * 100) + '%%）</span>').join('') + '</div></div>';
  });
  document.getElementById('azSum').innerHTML = sums.join('') + '<small>（共 ' + all.length + ' 個字）</small>';

  // GEPT 模擬試題成績表（gept.json）：每回聽力、閱讀答對題數（各 30 題）
  let gp = {};
  try{ gp = await (await fetch('gept.json', { cache:'no-cache' })).json(); }catch(e){}
  const P = gp.parts || {}, sum = (a, i) => a.reduce((s, x) => s + x[i], 0);
  const cell = (arr, names) => {
    const ok = sum(arr, 0), done = sum(arr, 1), tot = sum(arr, 2);
    if(!done) return '<td class="gp-no">還沒做</td>';
    const pct = Math.round(ok / done * 100);
    return '<td><b class="' + (pct >= 80 ? 'gp-good' : pct >= 60 ? 'gp-mid' : 'gp-low') + '">' + ok + ' / ' + done + '</b>' +
      (done < tot ? '<small>（做了 ' + done + '／' + tot + ' 題）</small>' : '<small>（' + pct + '%%）</small>') +
      '<div class="gp-parts">' + arr.map((x, i) => x[1] ? (names[i] ? names[i][0] : '') + ' ' + x[0] + '/' + x[1] : '').filter(Boolean).join('．') + '</div></td>';
  };
  const tables = people.map(p => {
    const u = (gp.users || {})[p];
    if(!u || !u.rounds || !u.rounds.length) return '<div class="gp-name">' + p + '</div><div class="gp-none">還沒有 GEPT 模擬試題紀錄。</div>';
    const byNo = {}; u.rounds.forEach(r => byNo[r.round] = r);
    let rows = '';
    for(let n = 1; n <= 10; n++){
      const r = byNo[n];
      if(!r){ rows += '<tr><td>第 ' + n + ' 回</td><td class="gp-no">還沒做</td><td class="gp-no">還沒做</td><td class="gp-no">—</td></tr>'; continue; }
      rows += '<tr><td>第 ' + n + ' 回</td>' + cell(r.listening, P.listening || []) + cell(r.reading, P.reading || []) + '<td>' + (r.date || '—') + '</td></tr>';
    }
    return '<div class="gp-name">' + p + '<small>（' + (u.read || '') + ' 從 WORD UP 讀取）</small></div>' +
      '<div class="gp-scroll"><table class="gp"><tr class="hd"><td>回次</td><td>聽力（30 題）</td><td>閱讀（30 題）</td><td>作答日期</td></tr>' + rows + '</table></div>';
  });
  document.getElementById('gept').innerHTML = tables.join('') + '<div class="gp-note">答對 / 已做題數；括號是答對率。作答日期 WORD UP 沒有顯示時寫「—」。</div>';
})();
</script>
</body>
</html>
''' % (''.join(units), '\n'.join(rows))
open(os.path.join(VOC, 'wordup', 'index.html'), 'w', encoding='utf-8', newline='\n').write(page)
print('wordup index：%d 個字，%d 個對到主題單元' % (sum(len(u['words']) for u in status['units'].values()),
      sum(1 for u in status['units'].values() for w in u['words'] if w.lower() in where)))
