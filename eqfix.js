/* 英文測驗系統：測驗規則統一以段考題庫為準（使用者 2026-10-18）。
 * 作答方式維持「一題一題做、答完看解說」（使用者選的），最後的成績頁改成段考題庫的訂正規則：
 *   1. 做完送出成績 → 成績頁列出每題對錯（原本就有）；點數只算這一次。
 *   2. 有錯題時成績頁上方「✏️ 訂正錯誤」＋「錯誤全部訂正完畢再另加補送 1 點」：按下後只重做答錯的題目（一樣一題一題），
 *      做完「送出訂正」→ 還有錯就再訂正，直到全對 → 補送 1 點（Points.earn kind:'fix-bonus'）。
 *   3. 還有錯題沒訂正完：不能離開這一頁、不能換測驗分頁、不能「重新測驗」；測試帳號 TEST、家長 PARENT 有「🚪 立即離開」。
 *   4. 試算表：第 N 次訂正只送訂正的題目，mode 後加「【第 N 次訂正】」；全部訂正完成另送「【全部訂正完成】補送 1 點」。
 *   5. 暫存：每答一題自動暫存（localStorage eqDraft:頁面:登入者），上方「💾 暫存」；下次打開、切到同一個測驗自動接續到下一題；送出成績後清掉。
 * 頁面的 questions／history／current… 是各頁 <script> 的全域變數，這支在 points.js 後面載入、包住 renderResult／syncResult／switchMode／handleAnswer。 */
(function () {
  if (typeof renderResult !== 'function' || typeof switchMode !== 'function') return;
  function get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function who() { var n = String(get('quizStudentName') || '').trim(); return (!n || /^訪客/.test(n)) ? '' : n.toUpperCase(); }
  function canSkip() { var n = who(); return n === 'TEST' || n === 'PARENT'; }
  function label() { return MODE_CONFIG[mode] ? MODE_CONFIG[mode].syncLabel : mode; }
  var css = document.createElement('style');
  css.textContent = '.fk-bar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin:0 0 16px;padding:10px 14px;border-radius:14px;background:#fff4dc;border:2px solid #e7c98a;font:600 14.5px/1.5 "Noto Sans TC","Microsoft JhengHei",sans-serif;color:#6b4a12;text-align:left}'
    + '.fk-bar b{color:#c0392b}.fk-bar.done{background:#e8f5ec;border-color:#9ccfab;color:#1f6b3a}.fk-bar.done b{color:#1f6b3a}'
    + '.fk-bar button{background:#c0392b;color:#fff;border:0;border-radius:999px;padding:9px 18px;font:800 15px "Noto Sans TC","Microsoft JhengHei",sans-serif;cursor:pointer}'
    + '.fk-bar button.exit{background:#fff;color:#5a4a2a;border:1.5px solid #c9b88f}'
    + '.fk-bar a{display:inline-block;padding:7px 14px;border-radius:999px;background:#2f6fb5;color:#fff !important;font-weight:800;text-decoration:none}'
    + '.fk-fixtag{display:inline-block;margin:0 0 10px;padding:4px 12px;border-radius:999px;background:#fff4dc;border:1.5px solid #e7c98a;color:#b5761a;font:800 13px "Noto Sans TC",sans-serif}'
    + '.fk-draftbar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin:0 0 10px;font:13px "Noto Sans TC","Microsoft JhengHei",sans-serif;color:#7a7259}'
    + '.fk-draftbar button{background:#fff;color:#2f4538;border:1.5px solid #b9c4b4;border-radius:10px;padding:5px 12px;font:700 13px "Noto Sans TC",sans-serif;cursor:pointer}';
  document.head.appendChild(css);

  // fx：目前這個測驗的訂正狀態 { mode, orig（全部題目）, idx（這一輪訂正的題目在 orig 的位置）, round, wrong（還錯的位置）, first（第一次的分數） }
  var fx = null, pending = false, skipped = false;

  var origSync = syncResult;
  function quietPoints(fn) {   // 訂正時試算表照送，但不要再算一般點數
    var P = window.Points, saved = P && P.earn;
    if (P) P.earn = function () { return Promise.resolve(null); };
    try { return fn(); } finally { if (P) P.earn = saved; }
  }
  syncResult = function (modeLabel, score, total, details) {
    if (fx && fx.round > 0) return quietPoints(function () { return origSync(modeLabel + '【第 ' + fx.round + ' 次訂正】', score, total, details); });
    return origSync(modeLabel, score, total, details);
  };

  var origResult = renderResult;
  renderResult = function () {
    var wrongNow = history.map(function (h, i) { return h.isCorrect ? -1 : i; }).filter(function (i) { return i >= 0; });
    if (!fx || fx.mode !== mode || fx.round === 0) {
      fx = { mode: mode, orig: questions, idx: questions.map(function (q, i) { return i; }), round: 0, first: correctCount + ' / ' + questions.length };
      clearDraft(mode);
    }
    fx.wrong = wrongNow.map(function (i) { return fx.idx[i]; });
    origResult();
    var restart = document.getElementById('restartBtn');
    pending = fx.wrong.length > 0 && !skipped;
    if (pending && restart) restart.style.display = 'none';
    if (!pending && fx.round > 0) {   // 全部訂正完成：補送 1 點、回到完整題目
      var name = who(), lb = label(), r = fx.round;
      if (name && name !== 'PARENT' && !skipped) quietPoints(function () { return origSync(lb + '【全部訂正完成】補送 1 點', 1, 1, [{ q: '錯題全部訂正完成（共訂正 ' + r + ' 次）', picked: '', correct: '', isCorrect: true }]); });
      if (window.Points && name && !skipped) { try { Points.earn({ name: name, label: WEEK_LABEL + '・' + lb, mode: '訂正完成', kind: 'fix-bonus', correct: 1, total: 1 }); } catch (e) {} }
      questions = fx.orig;
    }
    drawBar();
  };
  function drawBar() {
    var wrap = card.querySelector('.result-wrap'); if (!wrap || !fx) return;
    var bar = wrap.querySelector('.fk-bar');
    if (!bar) { bar = document.createElement('div'); bar.className = 'fk-bar'; wrap.insertBefore(bar, wrap.firstChild); }
    var exit = canSkip() ? '<button type="button" class="exit" data-fk-exit>🚪 立即離開</button>' : '';
    if (skipped) { bar.className = 'fk-bar done'; bar.innerHTML = '🚪 已解除訂正限制（測試／家長帳號），可以離開：<a href="' + backHref() + '">↩ 回上一層</a><a href="https://jenlin2002.github.io/">🏠 回主頁面</a>'; }
    else if (pending) { bar.className = 'fk-bar'; bar.innerHTML = '<button type="button" data-fk-fix>✏️ 訂正錯誤</button><span>還有 <b>' + fx.wrong.length + ' 題</b>錯誤。按「訂正錯誤」把錯的題目重新作答，<b>錯誤全部訂正完畢再另加補送 1 點</b>；訂正完才能離開這一頁。</span>' + exit; }
    else if (fx.round > 0) { bar.className = 'fk-bar done'; bar.innerHTML = '🎉 錯題全部訂正完成（訂正 ' + fx.round + ' 次）！補送 <b>1 點</b>。第一次的成績：' + fx.first + '。'; }
    else bar.remove();
  }
  function backHref() { return /\/course2\//.test(location.pathname) ? '../index.html' : 'course1.html'; }
  card.addEventListener('click', function (e) {
    if (e.target.closest('[data-fk-exit]')) { skipped = true; pending = false; var r = document.getElementById('restartBtn'); if (r) r.style.display = ''; if (fx) questions = fx.orig; drawBar(); return; }
    if (!e.target.closest('[data-fk-fix]') || !fx || !fx.wrong.length) return;
    fx.round++; fx.idx = fx.wrong.slice();
    questions = fx.idx.map(function (i) { return fx.orig[i]; });
    current = 0; correctCount = 0; wrongCount = 0; history = [];
    renderTally(); renderQuestion(); tagFix();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
  function tagFix() {
    if (!fx || fx.round === 0 || questions === fx.orig) return;
    if (card.querySelector('.result-wrap') || card.querySelector('.fk-fixtag')) return;
    var t = document.createElement('div'); t.className = 'fk-fixtag';
    t.textContent = '✏️ 第 ' + fx.round + ' 次訂正：共 ' + questions.length + ' 題（全部訂正完畢補送 1 點）';
    card.insertBefore(t, card.firstChild);
  }
  var origReset = resetQuiz;
  resetQuiz = function () {   // 「重新測驗一次」或換分頁：重新開始，訂正狀態清掉
    if (fx && questions !== fx.orig) questions = fx.orig;
    fx = null; pending = false; skipped = false;
    origReset();
  };
  var origRQ = renderQuestion;
  renderQuestion = function () { origRQ(); tagFix(); };

  // 還有錯題沒訂正完：不能換測驗分頁、不能離開這一頁
  var origSwitch = switchMode;
  switchMode = function (m) {
    if (pending || (fx && fx.round > 0 && questions !== fx.orig && !skipped)) { alert('還有錯題沒訂正完，先把「' + label() + '」訂正完才能換別的測驗喔！'); return; }
    fx = null; origSwitch(m); resume();
  };
  function blocking() { return pending || (fx && fx.round > 0 && questions !== fx.orig && !skipped); }
  document.addEventListener('click', function (e) {
    if (!blocking()) return;
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a || a.getAttribute('href').charAt(0) === '#' || a.closest('.fk-bar') || a.target === '_blank') return;
    e.preventDefault(); e.stopImmediatePropagation();
    alert('還有錯題，先按「✏️ 訂正錯誤」訂正完才能離開喔！');
  }, true);
  window.addEventListener('beforeunload', function (e) { if (blocking()) { e.preventDefault(); e.returnValue = ''; } });

  // ---- 暫存：每答一題自動存（第一次作答才存，訂正中不存）----
  function dkey() { return 'eqDraft:' + location.pathname + ':' + (who() || '-'); }
  function readD() { try { return JSON.parse(get(dkey()) || '{}') || {}; } catch (e) { return {}; } }
  function writeD(d) { try { if (Object.keys(d).length) localStorage.setItem(dkey(), JSON.stringify(d)); else localStorage.removeItem(dkey()); } catch (e) {} }
  function clearDraft(m) { var d = readD(); delete d[m]; writeD(d); note(''); }
  function saveDraft(manual) {
    if (mode === 'speaking' || (fx && fx.round > 0) || !history.length || history.length >= questions.length) { if (manual) note('還沒有可以暫存的作答'); return; }
    var d = readD(); d[mode] = { h: history, c: correctCount, w: wrongCount, t: Date.now() }; writeD(d);
    var t = new Date(); note((manual ? '✅ 已暫存' : '已自動暫存') + '（' + String(t.getHours()).padStart(2, '0') + ':' + String(t.getMinutes()).padStart(2, '0') + '，做到第 ' + history.length + ' 題），下次打開會從第 ' + (history.length + 1) + ' 題接著做');
  }
  var dbar = document.createElement('div'); dbar.className = 'fk-draftbar';
  dbar.innerHTML = '<button type="button">💾 暫存</button><span></span>';
  card.parentNode.insertBefore(dbar, card);
  dbar.querySelector('button').onclick = function () { saveDraft(true); };
  function note(t) { dbar.querySelector('span').textContent = t; }
  var origHA = handleAnswer;
  handleAnswer = function (i) { origHA(i); saveDraft(false); };
  function resume() {
    if (mode === 'speaking') { dbar.hidden = true; return; }
    dbar.hidden = false;
    var s = readD()[mode];
    if (!s || !s.h || !s.h.length || s.h.length >= questions.length) { note('每答一題會自動暫存，做到一半可以先離開，下次接著做。'); return; }
    history = s.h; correctCount = s.c; wrongCount = s.w; current = s.h.length;
    renderTally(); renderQuestion();
    note('📌 已接續上次暫存的作答，從第 ' + (current + 1) + ' 題接著做（前面答對 ' + correctCount + ' 題）');
  }
  setTimeout(resume, 0);
})();
