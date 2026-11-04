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

  const VOCAB = /^Vocab/.test(CFG.label || '');   // 單字區測驗：依登入者的進度出題（見 prepVocab）
  let V = null;                                    // 單字區：{ key, cards, mastered:Set, wrong:Set, retest }

  // 題目攤平成一題一題（每題一個分數）；單字區要先等 prepVocab() 決定這次考哪些題
  let items = [], total = 0;
  function flatten(){
    items = [];
    CFG.sections.forEach((sec, si) => sec.items.forEach(it => items.push(Object.assign({ sec: si }, it))));
    total = items.length;
  }

  const who = () => (get('quizStudentName') || '').trim();
  const draftKey = () => 'gqDraft:' + location.pathname + ':' + (who() || '-');

  // ---- 狀態 ----
  // phase: 'answer' 作答中、'graded' 已對答案、'fixing' 訂正中、'done' 全部訂正完成
  let S = null;
  const freshState = () => ({ phase:'answer', ans: items.map(() => null), ok: items.map(() => null), round: 0, firstWrong: [] });

  // ---- 單字區：每個登入者各自的進度（這台裝置的 localStorage） ----
  //   vocabProgress:<單字卡頁路徑>:<登入者> = { mastered:[第一次就答對的字], wrong:[答錯、還要複習的字], total, at }
  //   第一次考全部單字（課本題目沒考到的字，自動補「看中文選英文」）；之後只考還沒答對的字；全部答對就不用再考。
  function wordsOf(it, cardWords){
    const c = [];
    if(it.w) c.push(it.w);
    if(it.type === 'mc'){
      if(/^[A-Za-z' .-]+$/.test(it.q) && it.q.trim().split(/\s+/).length <= 3) c.push(it.q);   // 看英文選中文：題目就是單字
      c.push(it.opts[it.answer]);
    } else {
      it.blanks.forEach(b => c.push(b[0]));
      const m = /^\s*([A-Za-z][A-Za-z' -]*?)\s*→/.exec(it.q);   // 「swim → (V-ing) {0}」：原形也算
      if(m) c.push(m[1]);
    }
    const cands = c.map(s => String(s || '').toLowerCase().trim()).filter(Boolean);
    return cardWords.filter(w => {
      const lw = w.toLowerCase();
      return cands.some(x => x === lw || x.split(/[^a-z'-]+/).includes(lw) ||
        (lw.length >= 3 && x.indexOf(' ') < 0 && x.startsWith(lw) && x.length - lw.length <= 4));   // stamps、swimming、dishes
    });
  }
  async function prepVocab(){
    if(!who()) return;   // 沒登入：照原本整份考，不記進度
    let cards = [];
    try{
      const html = await (await fetch(CFG.back, { cache:'no-cache' })).text();
      const doc = new DOMParser().parseFromString(html, 'text/html');
      cards = [...doc.querySelectorAll('.vc-card')].map(c => ({ w: c.querySelector('.vc-word').textContent.trim(), zh: (c.querySelector('.vc-zh') || {}).textContent || '' }));
    }catch(e){}
    if(!cards.length) return;
    const page = new URL(CFG.back, location.href).pathname;
    const user = who().toUpperCase();
    const key = 'vocabProgress:' + page + ':' + user;
    let prog = null;
    try{ prog = JSON.parse(get(key) || 'null'); }catch(e){}
    const words = cards.map(c => c.w);
    // 每個字的狀態：本站答過的（vocabWords，所有單元共用）優先，沒答過就看 WORD UP 熟悉度（熟記＝已會，其他＝要複習）
    const st = await wordStatus(user);
    const mastered = new Set(words.filter(w => (st.get(w.toLowerCase()) || {}).s === 'm'));
    V = { key: key, user: user, cards: cards, mastered: mastered, wrong: new Set(words.filter(w => (st.get(w.toLowerCase()) || {}).s === 'w')), retest: !!prog, page: page };
    const covered = new Set();
    const secs = CFG.sections.map(sec => ({ title: sec.title, note: sec.note, items: sec.items.map(it => {
      const ws = wordsOf(it, words); ws.forEach(w => covered.add(w));
      return Object.assign({}, it, { _words: ws });
    }) }));
    // 課本題目沒考到的字：自動出「看中文選英文」（選項用同單元其他字，固定順序）
    const auto = [];
    cards.forEach((c, k) => {
      if(covered.has(c.w)) return;
      const others = words.map((w, j) => [w, (j * 37 + k * 53) % 101]).filter(x => x[0] !== c.w).sort((a, b) => a[1] - b[1]).map(x => x[0]);
      const opts = others.slice(0, 3); const pos = k % (opts.length + 1); opts.splice(pos, 0, c.w);
      auto.push({ type:'mc', q: c.zh.trim() || c.w, opts: opts, answer: pos, exp: c.w + '：' + c.zh.trim() + '。', _words: [c.w] });
    });
    if(auto.length) secs.push({ title: '⑦ 其他單字：看中文選英文', note: '本單元其他的字，每個字都要考到。', items: auto });
    // 複習：只留還有「沒答對的字」的題目；對不到單字的題目（如 the／不填）只在第一次考
    CFG.sections = secs.map(sec => Object.assign(sec, { items: sec.items.filter(it =>
      it._words.length ? it._words.some(w => !mastered.has(w)) : !V.retest) })).filter(sec => sec.items.length);
  }
  // 本站答題紀錄 vocabWords:<登入者> = { 小寫單字: 'm'(答對)|'w'(答錯) }，同一個字在每個單元共用；
  // WORD UP 熟悉度（vocab/wordup/status.json）只當參考：不熟＝'w'（紅、先複習），熟記＝'k'（只標記、照樣要考）。
  // 只有本站測驗答對（'m'）才算已會、不用再考（2026-11-04 使用者決定以本站測驗為準）。
  async function wordStatus(user){
    const m = new Map();
    try{
      const wu = await (await fetch(new URL('../wordup/status.json', location.href), { cache:'no-cache' })).json();
      const u = (wu.users || {})[user];
      if(u) Object.keys(u.words).forEach(w => m.set(w.toLowerCase(), { s: u.words[w][0] === '熟記' ? 'k' : 'w', src: 'wordup', lv: u.words[w][0] }));
    }catch(e){}
    try{ const mine = JSON.parse(get('vocabWords:' + user) || '{}'); Object.keys(mine).forEach(w => m.set(w, { s: mine[w], src: 'site' })); }catch(e){}
    return m;
  }
  function saveProgress(){
    if(!V) return;
    const okW = new Set(), badW = new Set();
    items.forEach((it, i) => (it._words || []).forEach(w => (S.ok[i] ? okW : badW).add(w)));
    let mine = {};
    try{ mine = JSON.parse(get('vocabWords:' + V.user) || '{}'); }catch(e){}
    okW.forEach(w => { if(!badW.has(w)){ V.mastered.add(w); V.wrong.delete(w); mine[w.toLowerCase()] = 'm'; } });
    badW.forEach(w => { V.mastered.delete(w); V.wrong.add(w); mine[w.toLowerCase()] = 'w'; });
    set('vocabWords:' + V.user, JSON.stringify(mine));
    set(V.key, JSON.stringify({ mastered: [...V.mastered], wrong: [...V.wrong], total: V.cards.length, at: Date.now() }));
  }
  function vocabInfo(){
    if(!V) return '';
    const n = V.cards.length, m = V.mastered.size;
    const words = V.cards.map(c => c.w), test = new Set(); items.forEach(it => (it._words || []).forEach(w => test.add(w)));
    return '<div class="gq-hint w100">📊 ' + esc(who()) + ' 這個單元：已答對 <b>' + m + '</b> / ' + n + ' 個字（' + Math.round(m / n * 100) + '%）' +
      (V.retest || m ? '；這次只考還沒答對的 <b>' + words.filter(w => test.has(w)).length + '</b> 個字' + (V.retest ? '' : '（在其他單元已經答對的字不用再考）') : '；第一次測驗，每個字都會考到') + '。</div>';
  }
  function allDoneScreen(){
    root.innerHTML = '<div class="gq-top"><span class="gq-ok">🎉 ' + esc(who()) + ' 這個單元 ' + V.cards.length + ' 個字已經全部答對了！單字卡都變成灰色，不用再背了。</span></div>' +
      '<div class="gq-links"><a class="btn" href="' + CFG.back + '">← 回單字卡</a> <a class="btn" href="../index.html">單字區目錄</a> ' +
      '<button class="btn" data-act="reset">↺ 清除紀錄、全部重新測驗</button></div>';
    root.addEventListener('click', e => {
      if(e.target.closest('[data-act=reset]') && confirm('要清除這個單元的答對紀錄，全部重新測驗嗎？')){ del(V.key); del(draftKey()); location.reload(); }
    });
  }

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
      top = vocabInfo() + whoLine + '<span>已作答 <b>' + filled + '</b> / ' + total + '</span><span><button class="btn" data-act="save">💾 暫存</button></span>';
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
    if(VOCAB) return '<div class="gq-links"><a class="btn" href="' + (CFG.back || 'index.html') + '">← 回單字卡（看紅色的字）</a> <a class="btn" href="../index.html">單字區目錄</a> <button class="btn" data-act="restart">↺ ' + (V ? '再考還沒答對的字' : '重新測驗') + '</button></div>';
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
    else if(act === 'restart'){ if(confirm('要重新測驗嗎？（重新作答的點數依每天規則計算）')){ del(draftKey()); if(V){ location.reload(); return; } S = freshState(); render(); scrollTo(0, root.offsetTop - 20); } }
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
    saveProgress();   // 單字區：只看第一次作答，答對的字變灰、答錯的字變紅（訂正後也還是紅，下次再考）
    const right = total - S.firstWrong.length;
    S.phase = S.firstWrong.length ? 'graded' : 'done';
    if(S.phase === 'done') del(draftKey()); else saveDraft();
    render();
    scrollTo(0, root.offsetTop - 20);
    const mode = !VOCAB ? '文法單元測驗' : (V && V.retest ? '單字複習測驗（只考沒答對的字）' : '單字測驗');
    if(window.Points) Points.earn({ name: who(), label: CFG.label, mode: mode, correct: right, total: total });
    sync(mode, right, total, details(all));
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
  const mustStay = () => !!S && (S.phase === 'graded' || S.phase === 'fixing') && S.ok.some(x => x === false);
  const isTester = () => /^(TEST|PARENT)$/i.test(who());
  window.addEventListener('beforeunload', e => { if(mustStay()){ e.preventDefault(); e.returnValue = ''; } });
  document.addEventListener('click', e => {
    const a = e.target.closest('a[href]');
    if(!a || !mustStay()) return;
    e.preventDefault();
    alert('錯題還沒訂正完，不能離開這一頁喔！請先按「✏️ 訂正錯誤」把錯題改對。');
  }, true);

  async function init(){
    if(VOCAB){ root.innerHTML = '<p class="gq-note">載入中…</p>'; await prepVocab(); }
    if(V && V.mastered.size >= V.cards.length){ allDoneScreen(); return; }
    flatten();
    S = freshState();
    loadDraft();
    render();
    if(S.phase !== 'answer' || S.ans.some(a => a != null)) setTimeout(() => flash('📂 已載入上次的暫存，接著做吧！'), 300);
  }
  init();
})();
