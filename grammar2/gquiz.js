// 國中文法單元測驗（共用）。作答、送出、計分、訂正方式照段考題庫 sync.js 的規則：
//   全部作答才能送出 → 馬上對答案（綠對紅錯＋正解＋詳解）→ Points.earn ＋ 同步試算表
//   → 有錯題：「✏️ 訂正錯誤」（答對的鎖住、錯題清空重答）→「送出訂正」直到全對 → 補送 1 點（kind:'fix-bonus'）
//   訂正完成前不能離開（擋連結、關分頁跳確認）；TEST／PARENT 有「🚪 立即離開」；「💾 暫存」＋自動暫存接續作答。
// 頁面提供 window.GQUIZ = { label, title, sections:[{ title, note, items:[...] }] }
//   選擇題 { type:'mc', q, opts:[...], answer:索引, exp }
//   填空類 { q:'含 {0} {1} 的題幹', blanks:[[可接受答案...], ...], exp }（填空、找錯改正、改寫、短文填空都用這種）
(function(){
  const CFG = window.GQUIZ;
  const root = document.getElementById('gquiz');
  if(!CFG || !root) return;
  const DEFAULT_SYNC_URL = 'https://script.google.com/macros/s/AKfycbwqd9cr_3MfXK8hzs8Y-YPQQUqOH5vKtW_vMav1nMAAt9VkBCP_5WP6Q1TDngIlr51U/exec';
  const LETTERS = 'ABCD';
  const mem = {};
  const get = k => { try{ return localStorage.getItem(k); }catch(e){ return k in mem ? mem[k] : null; } };
  const set = (k, v) => { try{ localStorage.setItem(k, v); }catch(e){ mem[k] = v; } };
  const del = k => { try{ localStorage.removeItem(k); }catch(e){ delete mem[k]; } };
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));

  // 題目攤平成一題一題（每題一個分數）
  const items = [];
  CFG.sections.forEach((sec, si) => sec.items.forEach(it => items.push(Object.assign({ sec: si }, it))));
  const total = items.length;

  const who = () => (get('quizStudentName') || '').trim();
  const draftKey = () => 'gqDraft:' + location.pathname + ':' + (who() || '-');

  // ---- 狀態 ----
  // phase: 'answer' 作答中、'graded' 已對答案、'fixing' 訂正中、'done' 全部訂正完成
  let S = { phase:'answer', ans: items.map(() => null), ok: items.map(() => null), round: 0, firstWrong: [] };

  function loadDraft(){
    try{ const d = JSON.parse(get(draftKey()) || 'null'); if(d && d.ans && d.ans.length === total) S = d; }catch(e){}
  }
  function saveDraft(showMsg){
    set(draftKey(), JSON.stringify(S));
    if(showMsg) flash('💾 已暫存，下次打開這一頁會從這裡接著做。');
  }

  // ---- 比對答案 ----
  function norm(s){
    s = String(s || '').toLowerCase().replace(/[’‘`]/g, "'").replace(/\s+/g, ' ').trim().replace(/[.!?,]+$/, '').trim();
    s = s.replace(/\bwon't\b/g, 'will not').replace(/\bcan't\b/g, 'cannot').replace(/\bcan not\b/g, 'cannot')
         .replace(/n't\b/g, ' not').replace(/'m\b/g, ' am').replace(/'re\b/g, ' are').replace(/'ve\b/g, ' have').replace(/'ll\b/g, ' will');
    return s.replace(/\s+/g, ' ');
  }
  function check(it, a){
    if(it.type === 'mc') return a === it.answer;
    return it.blanks.every((acc, k) => a && acc.some(x => norm(x) === norm(a[k])));
  }
  const answered = (it, a) => it.type === 'mc' ? a != null : !!(a && it.blanks.every((_, k) => String(a[k] || '').trim()));
  const showAns = (it, a) => it.type === 'mc' ? (a == null ? '' : '(' + LETTERS[a] + ') ' + it.opts[a]) : (a || []).join(' / ');
  const rightAns = it => it.type === 'mc' ? '(' + LETTERS[it.answer] + ') ' + it.opts[it.answer] : it.blanks.map(b => b[0]).join(' / ');

  // ---- 畫面 ----
  function render(){
    const locked = i => S.phase === 'graded' || S.phase === 'done' || (S.phase === 'fixing' && S.ok[i]);
    let html = '<div class="gq-top" id="gqTop"></div>';
    let n = 0;
    CFG.sections.forEach((sec, si) => {
      html += '<div class="gq-sec"><div class="level">' + sec.title + '</div>' + (sec.note ? '<p class="gq-note">' + sec.note + '</p>' : '');
      items.forEach((it, i) => {
        if(it.sec !== si) return;
        n++;
        const a = S.ans[i], lk = locked(i);
        const graded = S.phase !== 'answer' && S.ok[i] !== null && !(S.phase === 'fixing' && !S.ok[i]);
        const cls = 'q gq-item' + (graded ? (S.ok[i] ? ' hit done' : ' miss done') : '') + (S.phase === 'fixing' && !S.ok[i] ? ' gq-redo' : '');
        html += '<div class="' + cls + '" data-i="' + i + '"><div class="q-stem"><span class="num">' + n + '.</span>';
        if(it.type === 'mc'){
          html += it.q + '</div><div class="q-opts">' + it.opts.map((o, k) => {
            let c = 'q-opt';
            if(graded && k === it.answer) c += ' right';
            else if(graded && k === a) c += ' wrong';
            else if(a === k) c += ' picked';
            return '<button type="button" class="' + c + '" data-k="' + k + '"' + (lk ? ' disabled' : '') + '>(' + LETTERS[k] + ') ' + o + '</button>';
          }).join('') + '</div>';
        } else {
          html += it.q.replace(/\{(\d+)\}/g, (_, k) => '<input class="gq-blank" data-k="' + k + '" autocomplete="off" autocapitalize="off" spellcheck="false" value="' +
            esc(a && a[k] || '') + '"' + (lk ? ' disabled' : '') + ' size="' + Math.max(6, Math.min(28, (it.blanks[k][0] || '').length + 2)) + '">') + '</div>';
        }
        if(graded){
          html += '<div class="q-exp"><span class="verdict">' + (S.ok[i] ? '✓ 答對了' : '✗ 你的答案：' + esc(showAns(it, a)) + '　正解：' + esc(rightAns(it))) + '</span><br>' + it.exp + '</div>';
        }
        html += '</div>';
      });
      html += '</div>';
    });
    html += '<div class="gq-bottom" id="gqBottom"></div>';
    root.innerHTML = html;
    renderBars();
  }

  function renderBars(){
    const right = S.ok.filter(x => x === true).length;
    const wrong = S.ok.filter(x => x === false).length;
    const filled = items.filter((it, i) => answered(it, S.ans[i])).length;
    const leave = isTester() && (S.phase === 'graded' || S.phase === 'fixing') && wrong ? '<button class="btn" data-act="leave">🚪 立即離開</button>' : '';
    let top = '', bottom = '';
    const whoLine = '<span class="gq-who">作答者：<b>' + esc(who() || '（尚未登入）') + '</b></span>';
    if(S.phase === 'answer'){
      top = whoLine + '<span>已作答 <b>' + filled + '</b> / ' + total + '</span><span><button class="btn" data-act="save">💾 暫存</button></span>';
      bottom = '<button class="btn alt big" data-act="submit"' + (filled < total ? ' disabled' : '') + '>📤 送出成績</button>' +
        (filled < total ? '<div class="gq-hint">還有 ' + (total - filled) + ' 題沒作答，全部作答才能送出。</div>' : '');
    } else if(S.phase === 'graded'){
      top = whoLine + '<span>得分 <b>' + right + '</b> / ' + total + '（' + Math.round(right / total * 100) + '%）</span>' +
        (wrong ? '<span><button class="btn alt" data-act="fix">✏️ 訂正錯誤</button> ' + leave + '</span>' : '<span class="gq-ok">🎉 全對！</span>');
      if(wrong) top += '<div class="gq-hint w100">有 ' + wrong + ' 題錯了。錯誤全部訂正完畢再另加補送 1 點；沒訂正完不能離開這一頁。</div>';
      bottom = wrong ? '<button class="btn alt big" data-act="fix">✏️ 訂正錯誤（' + wrong + ' 題）</button>' : doneLinks();
    } else if(S.phase === 'fixing'){
      const need = S.ok.filter(x => x === false).length;
      const fixedFilled = items.filter((it, i) => S.ok[i] === false && answered(it, S.ans[i])).length;
      top = whoLine + '<span>第 <b>' + S.round + '</b> 次訂正：還有 <b>' + need + '</b> 題要改</span><span><button class="btn" data-act="save">💾 暫存</button> ' + leave + '</span>';
      bottom = '<button class="btn alt big" data-act="refix"' + (fixedFilled < need ? ' disabled' : '') + '>📤 送出訂正</button>' +
        (fixedFilled < need ? '<div class="gq-hint">紅框的錯題全部重新作答才能送出訂正。</div>' : '');
    } else {
      top = whoLine + '<span class="gq-ok">' + (S.firstWrong.length ? '✅ 錯題全部訂正完成！第一次得分 ' : '🎉 全對！得分 ') + (total - S.firstWrong.length) + ' / ' + total + '</span>';
      bottom = reviewList() + doneLinks();
    }
    document.getElementById('gqTop').innerHTML = top;
    document.getElementById('gqBottom').innerHTML = bottom + '<div id="gqSync" class="gq-sync"></div><div id="gqFlash" class="gq-flash"></div>';
  }

  function reviewList(){
    if(!S.firstWrong.length) return '';
    return '<div class="gq-review"><div class="level">📒 錯題複習（第一次做錯的 ' + S.firstWrong.length + ' 題）</div>' +
      S.firstWrong.map(i => '<div class="gq-rv"><b>' + (i + 1) + '.</b> ' + items[i].q.replace(/\{\d+\}/g, '____') +
        '<br><span class="gq-rv-a">正解：' + esc(rightAns(items[i])) + '</span><br><span class="gq-rv-e">' + items[i].exp + '</span></div>').join('') + '</div>';
  }
  function doneLinks(){
    return '<div class="gq-links"><a class="btn" href="' + (CFG.back || 'index.html') + '">← 回單元講解</a> <a class="btn" href="index.html">國中文法目錄</a> <button class="btn" data-act="restart">↺ 重新測驗</button></div>';
  }
  function flash(t){ const f = document.getElementById('gqFlash'); if(f){ f.textContent = t; clearTimeout(flash.t); flash.t = setTimeout(() => f.textContent = '', 4000); } }

  // ---- 作答事件 ----
  root.addEventListener('click', e => {
    const opt = e.target.closest('.q-opt');
    if(opt && !opt.disabled){
      const i = +opt.closest('.gq-item').dataset.i;
      S.ans[i] = +opt.dataset.k;
      opt.parentNode.querySelectorAll('.q-opt').forEach(b => b.classList.toggle('picked', b === opt));
      saveDraft(); renderBars(); return;
    }
    const b = e.target.closest('[data-act]');
    if(!b || b.disabled) return;
    const act = b.dataset.act;
    if(act === 'save') saveDraft(true);
    else if(act === 'submit') submit();
    else if(act === 'fix') startFix();
    else if(act === 'refix') submitFix();
    else if(act === 'leave'){ S.phase = 'done'; del(draftKey()); location.href = CFG.back || 'index.html'; }
    else if(act === 'restart'){ if(confirm('要重新測驗嗎？（重新作答的點數依每天規則計算）')){ S = { phase:'answer', ans: items.map(() => null), ok: items.map(() => null), round: 0, firstWrong: [] }; del(draftKey()); render(); scrollTo(0, root.offsetTop - 20); } }
  });
  root.addEventListener('input', e => {
    const inp = e.target.closest('.gq-blank');
    if(!inp) return;
    const i = +inp.closest('.gq-item').dataset.i;
    const a = S.ans[i] || [];
    a[+inp.dataset.k] = inp.value;
    S.ans[i] = a;
    saveDraft(); renderBars();
  });

  // ---- 送出、訂正 ----
  function grade(idx){ idx.forEach(i => S.ok[i] = check(items[i], S.ans[i])); }
  function details(idx){
    return idx.map(i => ({ q: (i + 1) + '. ' + items[i].q.replace(/<[^>]+>/g, '').replace(/\{\d+\}/g, '___'), picked: showAns(items[i], S.ans[i]), correct: rightAns(items[i]), isCorrect: S.ok[i] }));
  }
  function submit(){
    const all = items.map((_, i) => i);
    grade(all);
    S.firstWrong = all.filter(i => !S.ok[i]);
    const right = total - S.firstWrong.length;
    S.phase = S.firstWrong.length ? 'graded' : 'done';
    if(S.phase === 'done') del(draftKey()); else saveDraft();
    render();
    scrollTo(0, root.offsetTop - 20);
    if(window.Points) Points.earn({ name: who(), label: CFG.label, mode: '文法單元測驗', correct: right, total: total });
    sync('文法單元測驗', right, total, details(all));
  }
  function startFix(){
    S.phase = 'fixing'; S.round++;
    items.forEach((it, i) => { if(!S.ok[i]) S.ans[i] = null; });
    saveDraft(); render();
    const first = root.querySelector('.gq-redo');
    if(first) first.scrollIntoView({ behavior:'smooth', block:'center' });
  }
  function submitFix(){
    const idx = items.map((_, i) => i).filter(i => S.ok[i] === false);
    grade(idx);
    const still = idx.filter(i => !S.ok[i]).length;
    const fixedNow = idx.length - still;
    sync(CFG.title + '【第 ' + S.round + ' 次訂正】', fixedNow, idx.length, details(idx));
    if(still){ S.phase = 'graded'; saveDraft(); }
    else {
      S.phase = 'done'; del(draftKey());
      if(window.Points) Points.earn({ name: who(), label: CFG.label, mode: '訂正完成', correct: 1, total: 1, kind: 'fix-bonus' });
      sync(CFG.title + '【全部訂正完成】補送 1 點', S.firstWrong.length, S.firstWrong.length, []);
    }
    render();
    scrollTo(0, root.offsetTop - 20);
  }

  async function sync(mode, score, tot, det){
    const el = document.getElementById('gqSync');
    const url = get('quizSyncUrl') || DEFAULT_SYNC_URL;
    const name = who();
    if(!name){ if(el) el.textContent = '☁️ 還沒登入，成績沒有回傳'; return; }
    if(el) el.textContent = '☁️ 同步中…';
    try{
      await fetch(url, { method:'POST', mode:'no-cors', headers:{ 'Content-Type':'text/plain;charset=utf-8' },
        body: JSON.stringify({ name: name, week: CFG.label, mode: mode, score: score, total: tot, percent: tot ? Math.round(score / tot * 100) : 0, details: det }) });
      if(el) el.textContent = '☁️ 成績已送出到試算表';
    }catch(e){ if(el) el.textContent = '☁️ 同步失敗，請檢查網路連線'; }
  }

  // ---- 訂正完成前不能離開 ----
  const mustStay = () => (S.phase === 'graded' || S.phase === 'fixing') && S.ok.some(x => x === false);
  const isTester = () => /^(TEST|PARENT)$/i.test(who());
  window.addEventListener('beforeunload', e => { if(mustStay()){ e.preventDefault(); e.returnValue = ''; } });
  document.addEventListener('click', e => {
    const a = e.target.closest('a[href]');
    if(!a || !mustStay()) return;
    e.preventDefault();
    alert('錯題還沒訂正完，不能離開這一頁喔！請先按「✏️ 訂正錯誤」把錯題改對。');
  }, true);

  loadDraft();
  render();
  if(S.phase !== 'answer' || S.ans.some(a => a != null)) setTimeout(() => flash('📂 已載入上次的暫存，接著做吧！'), 300);
})();
