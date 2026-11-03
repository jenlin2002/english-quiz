# english-quiz 工作紀錄與說明

這個檔案是給「下一次接手的人」看的（包括在家裡電腦開 Claude Code 時，Claude 會自動讀這個檔案）。
最後更新：2026-10-03（在手機上用 Claude Code 雲端版完成的工作）。

## 使用者與工作方式（四個 repo 共用同一段，2026-10-13）

- 使用者在三個地方用 Claude Code：**家裡電腦、公司電腦**（兩台都有 GitHub Desktop，用它 Pull／Push）、**外出用手機 App（雲端版）**。學習成長網站已經做很久了，不用從頭介紹。
- **不用教 git／GitHub Desktop／PowerShell 的操作。** 改完直接開 PR 合併到 `main`（使用者另一台電腦用 GitHub Desktop Pull 就好），只要回報「改了什麼、合併到哪裡」。
- 一律用**繁體中文**回覆。
- **每次結束前**：把這次做的事、待辦更新到這個 CLAUDE.md，合併到 `main`，下一個地方 Pull 後就接得上。
- 學習網站的 repo（都在 jenlin2002 底下，GitHub Pages 從 `main` 發布）：
  `jenlin2002.github.io`（網站首頁＝成長學習館總入口、點數存摺、B&M 學習 App）、`english-quiz`（英文測驗系統）、
  `daily_life_listening`（美式生活館）、`vocab-king`（圖解單字）、`nat-geo-reading`（國家地理風閱讀）、`exam-bank`（段考題庫）。
  雲端版只讀得到這次有載入的 repo；要改的 repo 沒載入時，直接用 add_repo 加進來。
- 股票（`stock`、`stock-dashboard`）和學習網站分開，學習網站裡不要放股票相關的東西。

## 網站與 repo 的關係

| 網址 | repo | 內容 |
|---|---|---|
| jenlin2002.github.io | `jenlin2002.github.io` | 網站首頁（總目錄），有 English quiz、美式生活館等入口 |
| jenlin2002.github.io/english-quiz/ | `english-quiz`（這個 repo） | 英文測驗系統：第一期、第二期、第三期 |
| jenlin2002.github.io/daily_life_listening/ | `daily_life_listening` | 美式生活館（生活實況英語） |

- 網站由 GitHub Pages 從各 repo 的 `main` 分支發布；改完要合併到 `main`，約 1–2 分鐘後上線。
- 學生：BRANDEN、MELISSA。測驗成績透過 Google Apps Script 同步到 Google 試算表（網址寫在每個 quiz.html 的 `DEFAULT_SYNC_URL`）。

## 檔案結構

- `index.html`：英文測驗系統總目錄（第一期、第二期、第三期三張卡片）。
  **注意：這裡不要放美式生活館的連結**（使用者要求移除，美式生活館只從網站首頁進入）。
- `course1.html` 與根目錄的 `第N週投影片.html`、`第N週互動測驗.html`：第一期（已完成）。
- `course2/`：第二期（**已全部完成**）
  - `pre1/`、`pre2/`、`pretest/`：先修 2 週與前測
  - `w01`–`w20/`：每週 `slides.html`（投影片）＋ `quiz.html`（測驗）＋ `audio/`（投影片語音）
  - 複習週 `w05`、`w10`、`w15`、`w20` 只有 quiz.html
  - `img/`：聽力看圖題用的 8 張照片（Pexels，出處在 `img/PHOTO-CREDITS.md`）
- `course3/index.html`：第三期總目錄（**只有規劃，內容還沒做**）
- `tools/course2_gen/`：產生第二期第 16–20 週投影片與測驗的程式（見該資料夾的 README）

## 第二期的頁面格式（做新週次時照這個做）

- **quiz.html**：所有週共用同一套程式，只換資料區塊。
  - 資料在 `const GRAMMAR_QUESTIONS = [` 到 `// ---- 選項重新排列` 之間：
    文法 20．閱讀 10（複習週 5）．克漏字 4．單字 10．聽力 15（5 看圖＋4 問答＋4 對話＋2 進階）．口說 5
  - `WEEK_LABEL`（例如 `"II Week 16"`）會寫進試算表，要改。
  - 口說題的 `checkType` 對應 `analyzeSpeaking()` 裡的檢查規則；新的規則要加進去。
  - 選項會用固定種子重新排列，`answer` 寫原本正確選項的位置即可。
- **slides.html**：16:9 投影片，每個 🔊 按鈕依出現順序對應 `audio/slide-01.mp3`、`slide-02.mp3`…；
  沒有 mp3 時會改用瀏覽器內建語音。
- **語音**：用 Kokoro TTS（`pip install kokoro-onnx soundfile`，加上 ffmpeg）。
  模型檔從 https://github.com/thewh1teagle/kokoro-onnx/releases/tag/model-files-v1.0 下載
  （`kokoro-v1.0.int8.onnx`、`voices-v1.0.bin`）。聲音用 `af_heart`。

## 已完成的工作（2026-10-03）

1. 第二期第四階段：第 16–19 週投影片＋測驗＋語音、第 20 週全期總驗收（PR #1，已合併）
2. 第三期規劃：`course3/index.html`，先修 2 週＋30 週、六個階段（PR #2，已合併）
3. 總目錄曾經加上美式生活館卡片（PR #3），之後依使用者要求移除（PR #4，已合併）

## 待辦事項

1. **第三期內容**：還沒開始。下一步從「先修 1：長句拆解」做起，格式比照第二期。
   第五階段是寫作，現在的測驗系統沒有寫作題，要討論怎麼做。
2. **學習點數存摺（2026-10-03 已做好程式，等使用者部署後端並貼網址）**：
   - 規則（使用者定案）：答對 1 題 = 1 點；同一份測驗每天只算第一次；每人每天最多賺 50 點；
     10 點 = 15 分鐘電腦時間（每人每天最多換 75 分鐘）；100 點 = NT$50（不限次數）；
     兌換後馬上扣點、記存摺、寄 email 通知使用者的 Gmail。微軟沒有公開 Family Safety API，
     所以**不能自動加時間**，由家長收到信後手動加。
   - 前端 `points.js`（根目錄，各專案各一份、內容相同；`POINTS_URL` 空白時整個功能不啟用）。
     測驗頁在 `syncResult()` 開頭呼叫 `Points.earn()`，頁尾載入 `../../points.js`；已用 `patch_quiz_points.py`
     補上 59 頁（course1 的 `第N週…測驗.html`、course2 的 pre1/pre2/pretest/w01–w20）。
   - 後端 `Code.gs` 和完整部署步驟在私人專案 english-quiz-plan 的 `points/`（`README-點數存摺.md`）。
     **使用者要新建一份 Google 試算表、貼上 Code.gs、部署網頁應用程式後，把 `/exec` 網址交給 Claude 填進
     各專案的 `points.js`（`POINTS_URL`）再 Push。** 在那之前線上完全沒有變化。
   - **PIN 版（2026-10-03，本機已做好、尚未部署）**：每台裝置第一次進頁面要先選名字、設定／輸入 4 位數 PIN，後端驗證憑證；部署順序（先更新 Apps Script 並設好 PIN，再 Push）寫在 plan repo points/README-點數存摺.md 最後一節，順序錯了網站會卡在關卡。
   - 網站首頁（jenlin2002.github.io）有「點數存摺」橫幅；美式生活館場景頁／單元頁也會加點。
   - 英文測驗頁模板 `tools/templates/tpl-quiz.html`（plan repo）已含點數；`deploy_site.py` 會複製 `points.js`。
     之後手機端新做的週次（W21 起）要從更新後的模板建，或執行 `patch_quiz_points.py`。
   - 還沒接的：exam-bank（段考題庫）的 `sync.js`；使用者沒提，沒做。
   - **訪客模式（2026-10-04 加入，同一天使用者決定先關閉：`points.js` 的 `GUEST_ENABLED = false`；「有必要之後再開放」，要開放時三個 repo 都改成 true）**：「你是誰？」關卡多了「我是訪客（不用 PIN，不計點數）」，輸入名字就能用；
     存在 localStorage `pointsGuest`，`quizStudentName` 設成「訪客 名字」（成績照樣同步到試算表，但 `Points.earn()` 只認 BRANDEN／MELISSA／PARENT，所以不會加點）。
     有人用 PIN 登入（`setToken`）或按「離開訪客模式」就結束訪客模式。三個 repo 的 `points.js` 已同步更新；
     **plan repo（english-quiz-plan）的主檔 `points/points.js` 還沒同步，回家電腦要把這份複製回去**（雲端版沒有那個私人 repo 的權限）。
     同時修了手機寬度下點數橫幅名字被截斷（BR…）的問題。
3. **B&M 學習 App（2026-10-04）**：放在網站首頁 repo（jenlin2002.github.io）的 `/app/`，可「加入主畫面」的網頁 App（PWA），
   一個入口放英文測驗系統＋美式生活館；登入就是 points.js 的 PIN 關卡（同一個網域，登入一次所有網站都認得）。
   檔案：`app/index.html`、`app/manifest.webmanifest`（scope 是 `/`）、`app/icon-*.png`、根目錄 `sw.js`（只處理 `/app/` 底下）。

## 2026-10-04 手機雲端版的工作紀錄

- 已合併 english-quiz PR #6（訪客模式＋手機版點數橫幅）；網站首頁 PR #1 新增 B&M 學習 App（`jenlin2002.github.io/app/`）。
- 還沒在真的手機上驗證 App 安裝與 PIN 登入（雲端環境連不到網站與點數後端）。
- **回家電腦第一件事**：把 `points.js` 複製回 english-quiz-plan 的 `points/points.js`（主檔），三份公開副本已一致。
- 詳細說明見網站首頁 repo（jenlin2002.github.io）的 CLAUDE.md。

- **其他人＝家長開帳號（2026-10-04）**：除了 BRANDEN、MELISSA、家長，其他人要由家長在「家長管理 → 帳號管理」建立帳號（學生＝有存摺可賺點；只能練習＝不計點數），PIN 由家長設定；本人在關卡按「其他帳號登入」。訪客模式關閉（`GUEST_ENABLED = false`）。**要先更新 Apps Script 後端（貼新版 Code.gs → 部署新版本）才能用**，步驟在 plan repo `points/README-點數存摺.md` 最後一節。points.js 主檔與三個網站的副本已同步一致。

## 測驗規則統一以段考題庫為準（2026-10-18 使用者要求，以後新做的測驗也照做）

- **成長學習館各單元有測驗的地方，作答、送出、計分、訂正方式一律以國中英語段考題庫（exam-bank `sync.js`）為準**（使用者已測試驗證 OK）：
  送出成績（全部作答才送）→ 馬上對答案（綠對紅錯＋正解）→ 有錯題時上方「✏️ 訂正錯誤」＋「錯誤全部訂正完畢再另加補送 1 點」（答對的鎖住、錯題清空重答）→「送出訂正」直到全對 → 補送 1 點（`Points.earn` `kind:'fix-bonus'`）；
  沒訂正完不能離開這一頁（擋連結、關分頁跳確認）；測試帳號 TEST、家長 PARENT 有「🚪 立即離開」；試算表每次訂正 mode／單元名稱註明「【第 N 次訂正】」、完成記「【全部訂正完成】補送 1 點」；點數只算第一次作答；「💾 暫存」＋自動暫存接續作答。
- 各站的做法：段考題庫 `sync.js`；圖解單字 `topic.html`；國家地理閱讀 `fixkit.js`（`points-glue.js` 載入）；英文測驗系統 `eqfix.js`；美式生活館 `lifefix.js`（engine.js、index.html 用）。
  英文測驗系統、美式生活館是「一題一題做、答完看解說」的形式，使用者選擇保留，只把結果頁改成訂正規則（只重做錯題、直到全對）。
- 這個 repo：`eqfix.js`（根目錄），course2 的 23 個 `quiz.html` 與 course1 的 18 個 `第N週…測驗.html` 在 `</body>` 前載入它（在 points.js 後面）。它包住頁面的 `renderResult`／`syncResult`／`switchMode`／`handleAnswer`／`resetQuiz`／`renderQuestion`：成績頁上方「✏️ 訂正錯誤」只重做錯題（一題一題、一樣有解說），訂正中不能換分頁、不能重新測驗、不能離開；每答一題自動暫存（`eqDraft:頁面:登入者`），下次打開或切回該測驗從下一題接著做。**新做的週次（W21 起）也要在 `</body>` 前加 `<script src="../../eqfix.js"></script>`**（plan repo 的模板 `tpl-quiz.html` 已加）。口說練習不適用。

- **快取（2026-10-18）**：各頁用 `eqfix.js?v=20261018b` 載入共用程式；**改了共用程式要把所有頁面的 v 一起改**（sed 全部替換），不然手機瀏覽器會繼續用舊版（使用者 10-18 看到沒有「訂正錯誤」）。

## 國中文法分科區 `grammar2/`（2026-11-02 開始，公司電腦）

- 照翰林《國中英語文法特快車》20 個單元順序，一個單元三頁：`uNN.html` 講解（觀念 → 句型整理表 → 常見錯誤 → 自我練習，不計點）、`uNN-quiz.html` 單元測驗、（之後）投影片。講解與題目一律自己重寫，不可照抄課本。
- 已做：Unit 1 時態、Unit 2 被動語態、Unit 3 動名詞、Unit 4 不定詞、Unit 5 特殊動詞句型、Unit 6 助動詞、Unit 7 片語動詞、Unit 8 名詞、Unit 9 代名詞（講解＋投影片＋語音＋測驗）＝課本第 1 份（p1–100）全部做完；Unit 10 起在第 2 份（p101–200）。Unit 10 形容詞、Unit 11 副詞、Unit 12 介系詞、Unit 13 連接詞、Unit 14 附加問句、Unit 15 附和句、Unit 16 倒裝句、Unit 17 形容詞子句、Unit 18 疑問句、Unit 19 直接問句與間接問句、Unit 20 假設語氣（2026-11-03）也做好了＝**20 個單元全部完成**，Week 14 連到 u20.html#real，Week 4 的「📘 詳細講解」連到 u10.html#forms，Week 8 連到 u13.html，Week 13 連到 u17.html，Week 15 連到 u18.html，Week 16 連到 u19.html#report（Unit 19 多補了轉述 said that／asked if）。Unit 18 疑問句起在課本第 2 份 p188（hi2 第 88 頁）以後，Unit 20 後半在第 3 份（p201–206）。
- 英文測驗系統總目錄 `index.html`（2026-11-03 使用者要求）：「國中文法．分科詳解」當成第四張卡片，和第一、二、三期並排（寬螢幕 4 欄、中等 2 欄、手機 1 欄）。Week 7 的「📘 詳細講解」連到 u08.html#count。Week 6 的「📘 詳細講解」連到 u06.html。Week 9 的「📘 詳細講解」連到 u04.html#compare（to V vs V-ing 比較）。新單元的投影片要在 `build_slides.py` 的 `UNITS` 加上。`index.html` 是 20 單元目錄，沒做的標「製作中」。
- 測驗只出文法題，四層由易到難：①選擇 ②填空（給原形）③找錯改正 ④改寫／合併＋短文填空。共用程式 `gquiz.js`，流程照段考題庫規則（全部作答才送出、對答案、`Points.earn`、同步試算表 label `G8 Grammar UN`、訂正到全對補送 1 點、訂正中不能離開、暫存 `gqDraft:`）。改了 `gquiz.js`／`grammar.css` 要把各頁的 `?v=` 一起改。
- 第一期 `course1.html` 的週卡有「📘 詳細講解」連到對應單元（W1/2/3/11 → u01 的 #s1/#s2/#s3/#s6，W12 → u02），之後做出單元再補其他週。
- 課本：`I:\興雅\英文\115二上翰林\…文法特快車_課本_教用_切割\`，是掃描圖檔，用 PyMuPDF 轉圖片看。
- 投影片 `uNN-slides.html`（2026-11-02 做好 Unit 1、2）：由 `tools/grammar2_gen/build_slides.py` 產生（內容在 `uNN_slides.py`，沿用第二期 `tools/course2_gen` 的樣式與 sl.py），會輸出 `audio_jobs.json`；語音 mp3 放 `grammar2/audio/uNN/slide-NN.mp3`。Unit 1、2 已錄好（103 句）。錄音用 `tools/grammar2_gen/tts_mp3.py`（soundfile 直接寫 mp3，不需要 ffmpeg；已存在的 mp3 會跳過）。公司電腦已裝 kokoro-onnx，模型檔在 `C:\Users\jenlin2002\kokoro-models`（不在 repo 裡），執行前設 `$env:KOKORO_DIR` 指到那裡。
- 待辦：文法 20 單元已完成 → 下一步單字區（單字2000活用練習＋LaLa Word）→ 克漏字區 → 閱讀區（各自獨立一區，不混進文法區；每區先做 1～2 單元給使用者看）。之後可考慮給題目標考點代號、做 links.js 讓克漏字詳解連到文法單元（2026-11-02 提過，使用者未決定）。

## 國中單字分科區 `vocab/`（2026-11-03 開始，試做中）

- 使用者定案：兩個小區——「主題 2000 字」照翰林《單字2000活用練習》40 單元（`vocab/w2000/`）、「一字多義・易混淆・字首字尾」照《LaLa Word 小單字大視野》18 單元（還沒做）；每單元三頁：`uNN.html` 單字卡、`uNN-slides.html` 投影片、`uNN-quiz.html` 測驗；**不標 KK 音標**，每個字和例句都有 🔊。例句、說明、題目自編，只參考字表與單元。
- 已做：主題 2000 字 Unit 1 People（18 字，測驗 29 題）、Unit 2 Personal characteristics（51 字，測驗 34 題，45 張照片＋6 個 emoji）。使用者 2026-11-03 看過照片版說「可以，繼續做」。
- 形容詞 fat／ugly／stupid／poor 這類字不用人的照片（避免標籤化），改用動物、物品；照片不合適的字（抽象字）保留 emoji。資料檔的 `focus` 可用 dict（title／head／rows／note）做比較級、-ed／-ing 等整理表。
- 單字測驗的「例句填空」（寫單字的題目）**每一題都要附中文提示**，例如 `（鄰居）`；2026-11-03 使用者發現有的有、有的沒有。
- 圖片（2026-11-03 使用者要求「投影片要有單字圖片」，看過 emoji 後選「換成照片」）：照片放 `vocab/<book>/img/uNN/<單字>.jpg`（Pexels，裁 4:3、640×480，出處在同資料夾 `PHOTO-CREDITS.md`）；`build_vocab.py` 有照片就用照片，沒有才用資料檔的 `'pic'` emoji。投影片每頁 4 張圖卡（照片＋單字🔊＋中文＋例句🔊），單字卡上方是 4:3 照片。選照片時要逐張看過（不要恐怖、暴露、黑白太暗的），在內建瀏覽器用 Pexels 搜尋頁的 fetch 抓候選。改了投影片按鈕順序要先刪掉該單元 `audio/uNN/slide-*.mp3` 再重錄（tts_mp3 會跳過已存在的檔）。
- 產生程式 `tools/vocab_gen/build_vocab.py`，每單元一個資料檔（`w2000_u01.py`：UNIT 字表＋QUIZ），在 `UNITS` 加上；錄音同文法區（`tts_mp3.py tools/vocab_gen/audio_jobs.json`），音檔在 `vocab/w2000/audio/uNN/`（w-NN 單字、e-NN 例句、slide-NN）。單字卡用 `vocab/vocab.css`、`vocab/vocab.js`（遮中文／遮英文自我測驗、全部播放）；樣式與測驗程式共用 `grammar2/grammar.css`、`grammar2/gquiz.js`。測驗 label `Vocab W2000 UN`。
- 總目錄 `index.html` 第五張卡片「國中單字．分科練習」（寬螢幕 5 欄、1300px 以下 3 欄、900px 以下 2 欄、手機 1 欄）。

## 連續學習紅利＋稱讚畫面（2026-10-18）

- 送出測驗後跳出稱讚卡（得幾點、連續第幾天、還差幾點到 100 點）；每跨過 100 點跳出大的恭喜兌換畫面。
- 連續學習紅利：第 2 天 +2、第 3、4 天 +3、第 5 天起每天 +4（2026-10-18 使用者改），中斷就重算；不算在每天 50 點上限內；存摺分頁記成類型「紅利」。
- **答對率計分（2026-10-18）**：答對 1 題得幾點看答對率（第三版，2026-10-18 使用者定）：低於 30% 0.25、30～50% 0.5、50～60% 0.8、60～70% 1、70～90% 1.2、90% 以上 1.5、全對 2，四捨五入成整數（80～90% 使用者沒另外寫，同 7～8 成）；後端 `Code.gs` 的 `CONFIG.RATE_TIERS`，要重新部署 Apps Script 才生效。
- **段考訂正完成補送 1 點（2026-10-18）**：段考題庫錯題全部訂正完成後 `Points.earn({kind:'fix-bonus'})`，後端 `fixBonus_()` 記一筆類型「訂正獎勵」+`CONFIG.FIX_BONUS`（1）點，同一份考卷每天一次、不算每天上限與連續天數；要重新部署 Apps Script 才生效（舊版後端會當成一般賺點、全對每題 2 點＝給 2 點）。
- 程式在 `points.js`（7 份副本內容一致，主檔在 english-quiz-plan `points/points.js`）與後端 `Code.gs`（`CONFIG.STREAK_BONUS`）。
- **要先更新 Apps Script 後端（貼新版 Code.gs → 部署新版本）紅利才會開始算**，步驟在 english-quiz-plan `points/README-點數存摺.md` 最後一節。
