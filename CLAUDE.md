# english-quiz 工作紀錄與說明

這個檔案是給「下一次接手的人」看的（包括在家裡電腦開 Claude Code 時，Claude 會自動讀這個檔案）。
最後更新：2026-11-21（新做「寫作園地」`writing/`：Unit 1 我的週末、Unit 2 我的寵物，說→寫五步驟＋英檢造句練習＋短文自動檢查／文法拼字／AI 建議，見「寫作園地」一節）；2026-11-20（單字區新開「LaLa Word 一字多義」區，18 個單元全部做好；英文測驗系統 5711 個小音檔合併成每單元一個 all.mp3，網站檔案數從約 19,417 降到約 13,902，見「國中單字分科區」的「音檔合併」；單字區投影片改用單字卡的音檔、刪掉 2722 個重複的 slide 音檔，網站檔案數回到 Cloudflare 上限以下；u21～u40 音檔也放大音量，見「國中單字分科區」的「投影片音檔共用」）；2026-11-19（公司電腦：單字區新做 Unit 21 語言、22 節日、23 職業、24 天氣與大自然、25 地理名詞、26 動物與昆蟲、27 冠詞與限定詞、28 代名詞、29 疑問詞、30 be 動詞與助動詞、31～40 介系詞到副詞＝主題 2000 字全部完成）；2026-11-18（家裡電腦：單字區新做 Unit 17 地點與位置、Unit 18 交通、Unit 19 尺寸與測量、Unit 20 國家與區域，見「國中單字分科區」；同一天電腦版讀了 BRANDEN 的 WORD UP 熟悉度＋GEPT 成績，見「WORD UP（已購買的網頁版）整合」一節）。

## ⭐ 最新進度與回家要做的事（2026-11-04 公司電腦，回家電腦先讀這節）

**今天在公司做的（english-quiz，已 Push）**
1. 單字區（國中2000字）新做 **Unit 13 顏色、14 運動興趣嗜好、15 房子與公寓、16 學校**（單字卡＋投影片＋測驗＋照片＋語音），測驗都用正確答案驗證過滿分。細節見下面「國中單字分科區」。
2. 單字區名稱改成「**國中2000字．分科練習**」（總目錄卡片與單字區標題）。
3. **單字學習進度功能**（使用者要求，細節見「國中單字分科區」最後的說明）：每個登入者各自——答錯的字紅色、答對的字暗灰色；下次測驗只考還沒答對的字；全部答對整單元變灰、不用再背；單字卡上方和單字區目錄顯示答對率、答對幾個、還有幾個紅字。**進度只存在作答那台裝置**（localStorage），還沒存到雲端；使用者若要跨裝置要改成存試算表（要改 Apps Script 後端）。
4. 圖解單字（vocab-king）：目錄 14 張分類卡、居家 10 主題、校園 4 主題、醫院 3 主題的單字換成照片（細節在 vocab-king 的 CLAUDE.md）。**vocab-king 還有 4 筆 commit 在公司電腦沒 Push**——公司電腦要先 Push，家裡才 Pull 得到。

**回家電腦要做的事**
1. GitHub Desktop：english-quiz、vocab-king 都先 **Pull**。
2. ✅（2026-11-04 晚上家裡電腦已處理）查過家裡電腦：**`w2000_u03.py`～`w2000_u12.py` 從來不存在**——11-03 晚上那次（在 `H:\2000單字` 開的 Claude）是拿 Unit 2 的 HTML 當模板直接做 u03～u12 的網頁，沒有用 `build_vocab.py`。所以 `UNITS` 現在是 u01、u02、u13～u16（快取版本照公司的 `20261104e`），重跑 `build_vocab.py` 6 個單元都能產生，網頁內容和 repo 一致。家裡另外做的一份 Unit 13 以公司版為準，舊的家裡版備份在家裡電腦 `H:\githubdata\english-quiz-本機備份-20261104`（不在 repo）。**u03～u12 之後若要改，直接改 HTML，或另外補資料檔。**
3. （已做，見上一項）
4. ✅（2026-11-18 家裡電腦已照課本做完 **Unit 17 Places & locations**、**Unit 18 Transportation**、**Unit 19 Sizes & measurements**、**Unit 20 Countries and areas**，見「國中單字分科區」）下一個是 **Unit 21 Languages 語言**（印刷頁第 69 頁下半，只有 Chinese、English 2 個字）。以下是當時的說明：**2026-11-18 在公司電腦曾照教育部 2000 字試做 Unit 17（當時 I: 槽沒連上，找不到課本），使用者要求全部退回，改在家裡電腦照課本做**（**家裡電腦的課本在本機 H: 槽**，11-03 就是在 `H:\2000單字` 做 u03～u12，從那裡找；找不到再問使用者。注意 `H:\2000單字\vocab\`（w2000 資料夾＋index.html，11-04 01:13）是 11-03 那次做網頁的**舊工作副本，不是最新版**，網頁一律以 repo 為準，不要從那裡複製回 repo。公司電腦的 H: 是 Google 雲端硬碟，不是這個；公司電腦要等 I: 槽連上才讀得到課本）。照片做法：在內建瀏覽器開 Pexels 搜尋頁，用頁面內 `fetch('/search/<關鍵字>/?orientation=landscape')` 一次抓所有字的候選，Python 下載縮圖（`https://images.pexels.com/photos/<id>/pexels-photo-<id>.jpeg?auto=compress&w=400`）拼成對照表逐張看過再挑。
5. 之前就有的：把 `points.js` 複製回 english-quiz-plan 的主檔（見下方待辦）。**11-04 points.js 又改了（Cloudflare 登入），複製最新版。**
6. Cloudflare 登入（見下一節「登入改成 Cloudflare Access＋Google 帳號」）：使用者照首頁 repo `CLOUDFLARE-SETUP.md` 設後台；第二階段要改 plan repo 的 Code.gs（加 `cfUser_`）。

## 登入改成 Cloudflare Access＋Google 帳號（2026-11-04 規劃，程式已做好、等使用者設定後台）

- **2026-11-04 晚上**：後台已設好，新網址 `https://learn-6td.pages.dev`（2026-11-05 改成 `https://bmlearn.pages.dev`），家長 Gmail 登入後 `/api/me` 回 `PARENT` ✅；還沒用孩子帳號、測驗、點數實測。詳細進度在首頁 repo 的 CLAUDE.md。

- 使用者選定：學習網站跟股票網站一樣用 Cloudflare 保護（但兩邊完全分開），BRANDEN、MELISSA 用自己的 Google 帳號、家長用自己的 Gmail 登入，不再「選名字＋4 位數 PIN」。
- 6 個 repo 由首頁 repo（jenlin2002.github.io）的 GitHub Actions「部署到 Cloudflare Pages」合成一個網站（Pages 專案 `bmlearn`，網址 **https://bmlearn.pages.dev**，路徑和 GitHub Pages 一樣；2026-11-05 從 learn-6td.pages.dev 改名，舊網址和 jenlin2002.github.io 都轉到這裡，後台步驟在首頁 repo `CLOUDFLARE-SETUP.md` 第七節），`functions/api/me.js` 用 Access 憑證＋`USER_MAP`（Cloudflare 變數，email 不放 repo）回傳登入者名字。
- `points.js`（各站副本內容相同）：在 Cloudflare 網址打開時問 `/api/me`，自動設定 `quizStudentName`、不出現「你是誰？」關卡；第一階段每台裝置第一次只問一次自己的 PIN；第二階段（Code.gs 加 `cfUser_`、Cloudflare 設 `POINTS_SECRET`）點數改走 `/api/points`，不用 PIN。登出會連 Google 登入一起登出。在 jenlin2002.github.io 舊網址一切照舊。
- 後台設定步驟、測試方法、第二階段 Code.gs 改法都在首頁 repo 的 `CLOUDFLARE-SETUP.md`。密碼、金鑰一律使用者自己在 Cloudflare／GitHub／Google 後台輸入。
- 之後新做的頁面照舊用相對路徑；子站寫死的 `https://jenlin2002.github.io/` 部署時會自動改成 `/`。Cloudflare Pages 單檔上限 25 MB、整站 20000 個檔（2026-11-04 約 15300 個；2026-11-20 一度到約 20035 個、超過上限，單字區投影片改共用音檔後約 17300 個。**新增大量音檔前先估總數**，六個 repo 去掉 tools／.git 後的檔案數加起來），大檔（>24 MB）部署時自動改由 `/api/big` 轉給登入的人（2026-11-05 起；要有 `REPOS_TOKEN`，repo 改 Private 也能讀；金鑰到期要重做，見首頁 repo `CLOUDFLARE-SETUP.md` 第八節）。寫頁面照舊連原本的相對路徑，不用改。
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

- **先選、送出成績才對答案（2026-11-10 使用者要求）**：每題點選項只是「選」（藍框，可以改），按「送出成績」才判對錯；答對馬上出現「下一題」，答錯要聽完中文解說語音才出現「下一題」（解說前按鈕隱藏）；最後一題送出後按鈕是「看成績」。單字測驗照舊還要完成句子重組。程式在 `eqfix.js` 的 `gate()`＋card 的 capture 點擊攔截（不用改各頁）。

- **快取（2026-10-18；2026-11-10 改成 `v=20261110a`）**：各頁用 `eqfix.js?v=…` 載入共用程式；**改了共用程式要把所有頁面的 v 一起改**（sed 全部替換），不然手機瀏覽器會繼續用舊版（使用者 10-18 看到沒有「訂正錯誤」）。

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
- **Unit 3–12（2026-11-03 晚上在家裡電腦做的）**：網頁、照片、語音都已上傳；這 10 個單元是拿 Unit 2 的 HTML 當模板直接做的，**沒有 `w2000_u03.py`～`u12.py` 資料檔**（11-04 晚上在家裡電腦確認過），不在 `build_vocab.py` 的 `UNITS` 裡。
- **Unit 13 Colors 顏色（2026-11-04 公司電腦）**：12 字、測驗 24 題、12 張照片、48 個音檔。資料檔 `w2000_u13.py`。為了不和家裡沒上傳的 `build_vocab.py` 打架，這次**沒有改 `build_vocab.py`**，是用一行指令只產生 Unit 13：`python -c "import sys,json; sys.path.insert(0,'tools/vocab_gen'); import build_vocab as b, w2000_u13 as m; json.dump(b.build(m), open('jobs.json','w',encoding='utf-8'), ensure_ascii=False)"`，再用 `tts_mp3.py jobs.json` 錄音。**家裡把 `build_vocab.py` 上傳時，`UNITS` 要記得加上 `w2000_u13`**。課本 Unit 13 在 `…單字2000活用練習_課本_教用_1of3_p1-93.pdf` 第 37 頁；Unit 14 運動嗜好在第 40 頁、15 房屋第 44 頁、16 學校第 30 頁附近、17 地點第 56 頁（PDF 頁序有點亂，用縮圖找）。
- **Unit 14 Sports, interests & hobbies 運動、興趣與嗜好（2026-11-04 公司電腦）**：45 字、測驗 34 題、44 張照片（doll 用 emoji）、180 個音檔；重點整理 play + 球類／play the + 樂器、go + V-ing、V-ing 拼法。產生方式同 Unit 13（一行指令只產生這個單元，`build_vocab.py` 沒改），**家裡上傳 `build_vocab.py` 時 `UNITS` 也要加 `w2000_u14`**。Unit 13、14 的測驗都在本機用正確答案作答過，得滿分。
- **Unit 15 Houses & apartments 房子與公寓（2026-11-04 公司電腦）**：51 字、測驗 32 題、47 張照片（room、yard、bath、umbrella 用 emoji）、204 個音檔；重點整理房間、-y／-ch／-o 複數、go home。產生方式同 Unit 13，**`UNITS` 也要加 `w2000_u15`**。課本 Unit 16 School 在 PDF 第 50 頁附近（縮圖第 49–54 張），17 地點第 56 頁。
- **Unit 16 School 學校（2026-11-04 公司電腦）**：76 字、測驗 34 題、49 張照片（抽象動詞、名詞用 emoji）、304 個音檔；重點整理科目不可數、不規則動詞 say／speak／teach／understand／write／read、-ies 複數。**`UNITS` 也要加 `w2000_u16`**。課本 Unit 16 實際在 PDF 第 1 份的第 50–53 頁（PDF 索引 49–52）；Unit 17 Places & locations 從第 56 頁起。
- **Unit 17 Places & locations 地點與位置（2026-11-18 家裡電腦）**：照課本字表 41 字（課本「學用」PDF 印刷頁第 58–59 頁；家裡電腦的課本在 `H:\2000單字\115[翰林]國中英語單字2000活用練習_課本_學用.pdf`，單一檔案，PDF 頁序＝印刷頁碼－1）。測驗 32 題（①②③④複數⑤例句填空⑥用法；登入後還會自動補⑦），沒登入時用正確答案作答得 32/32；31 張照片（here、there、back、front、left、middle、right、south、north、place 用 emoji）、164 個音檔；重點整理：位置片語（in front of、in the middle of…）、東西南北、問路。`build_vocab.py` 的 `UNITS` 已加 `w2000_u17`（產生時仍用一行指令只產生 Unit 17），已重跑 `build_wordup_index.py`。照片對照表是家裡電腦 `H:\2000單字\tools\cand_sheet.py`（`{"字":[id…]}` → 縮圖拼圖）和 `get_photos.py`（下載、裁 4:3、640×480、寫 PHOTO-CREDITS.md），不在 repo。課本 Unit 18 Transportation 交通從印刷頁第 62 頁開始。
- **Unit 18 Transportation 交通（2026-11-18 家裡電腦）**：照課本字表 27 字（印刷頁第 62–63 頁）。測驗 33 題（①②③④動詞變化⑤例句填空⑥用法），沒登入時用正確答案作答得 33/33；27 張照片（全部有照片）、108 個音檔；重點整理：by bus／on foot／take／ride／drive、drive／fly／ride 等三態、fast／quickly／slowly／soon。做法同 Unit 17（`UNITS` 已加 `w2000_u18`，已重跑 `build_wordup_index.py`）。課本 Unit 19 Sizes & measurements 尺寸與測量從印刷頁第 65 頁開始。
- **Unit 19 Sizes & measurements 尺寸與測量（2026-11-18 家裡電腦）**：照課本字表 40 字（印刷頁第 65–66 頁；foot、cup、glass、little、light、short 和前面單元重複，這裡用測量／數量的意思）。測驗 33 題，沒登入時用正確答案作答得 33/33；37 張照片（foot、small、height 用 emoji）、160 個音檔；重點整理：長度重量單位與縮寫、相反詞與比較級、a dozen／a pair of／a piece of。做法同 Unit 17（`UNITS` 已加 `w2000_u19`，已重跑 `build_wordup_index.py`）。課本 Unit 20 Countries and areas 國家與區域從印刷頁第 69 頁開始（短單元，同頁接 Unit 21 Languages）。
- **Unit 20 Countries and areas 國家與區域（2026-11-18 家裡電腦）**：照課本字表 7 字（country、world、America、China、Taiwan、R.O.C.、U.S.A.）。測驗 22 題，沒登入時用正確答案作答得 22/22；5 張照片（R.O.C.、U.S.A. 用 emoji）、28 個音檔；重點整理：國家／人／語言、國名縮寫、Where are you from?。
  - `build_vocab.py` 新增兩個功能（舊單元的輸出不變，重跑 u01、u02、u13～u19 內容都相同；git 只會因為換行符號顯示 M，`git checkout` 掉就好）：① 資料檔的字可以加 `'say'`／`'exsay'` 指定語音唸法（R.O.C. 唸成「R O C」，畫面上照樣顯示 R.O.C.）；② 8 個字以下的小單元，投影片快問快答平分成兩頁（原本是前 8 個字一頁、9～16 個字一頁，7 個字的單元「英文 → 中文」會是空的）。
  - 課本 Unit 21 Languages 只有 Chinese、English 兩個字（印刷頁第 69 頁下半）；Unit 22 從第 70 頁起，做之前先轉圖確認。
- **單字區音檔放大音量（2026-11-18 家裡電腦，使用者反映「點單字聲音太小」）**：Kokoro 錄出來平均約 -22 dB（一般影音約 -14～-16 dB）。新增 `tools/vocab_gen/boost_audio.py`（numpy＋soundfile，不用 ffmpeg）：目標平均 -16 dB、最大音量不超過 -1 dB（不破音），差不到 0.5 dB 的檔跳過，所以重跑不會越來越大聲。已處理 `vocab/*/audio/` 全部 2996 個檔（主題 2000 字 u01～u20、WORD UP u01～u02），平均放大 +5 dB。**以後新錄的單元，`tts_mp3.py` 錄完要接著跑 `python tools/vocab_gen/boost_audio.py vocab/w2000/audio/uNN`**。文法區、美式生活館等其他地方的音檔也一樣偏小聲（約 -22 dB），還沒處理（使用者只要求單字區）。
- **Unit 21 Languages 語言（2026-11-19 公司電腦，I: 槽已接上）**：照課本字表 2 字（Chinese、English）。測驗 16 題，沒登入時用正確答案作答得 16/16；2 張照片（毛筆與中文字、拼出 ENGLISH 的字母珠）、8 個音檔；重點整理：Chinese／English 當語言、人、形容詞，語言不可數、in English，國家／人／語言對照。`UNITS` 已加 `w2000_u21`，已重跑 `build_wordup_index.py`。
  - **公司電腦的課本**：`I:\興雅\英文\115二上翰林\115[翰林]國中英語單字2000活用練習_課本_學用.pdf`（208 頁，單一檔案，PDF 頁序＝印刷頁碼－1，和家裡那份一樣）；用 PyMuPDF 轉圖看。
- **Unit 22～25（2026-11-19 公司電腦）**：照課本字表做，例句、中文、題目自編；四份測驗沒登入時用正確答案作答都全對；`UNITS` 已加 `w2000_u22`～`u25`，已重跑 `build_wordup_index.py`。
  - **Unit 22 Holidays & festivals 節日與慶典**（印刷頁第 70 頁）：7 字（Christmas、Easter、Halloween、festival、holiday、vacation、celebrate）。測驗 22 題 22/22；7 張照片、28 個音檔；重點整理：常見節日（含春節、元宵、端午、中秋）、holiday／vacation／festival、celebrate 變化。
  - **Unit 23 Occupations 職業**（第 72–73 頁）：30 字。測驗 31 題 31/31；30 張照片、120 個音檔；重點整理：-er／-or／-man／-ess 造字、特別的複數（-men、housewives、secretaries）、問職業、job 可數／work 不可數。cook 前面出現過，這裡是「廚師」。
  - **Unit 24 Weather & nature 天氣與大自然**（第 76–77 頁）：29 字。測驗 28 題 28/28；29 張照片、116 個音檔；重點整理：名詞＋y（sunny 多一個 n）、問天氣、相反詞、blow／shine 三態。cold、cool、hot 前面出現過，這裡是天氣的意思。
  - **Unit 25 Geographical terms 地理名詞**（第 80 頁）：12 字（area、bank、beach、hill、island、lake、mountain、pond、pool、river、sea、spring）。測驗 22 題 22/22；12 張照片、48 個音檔；重點整理：比大小（hill／mountain、pond／lake）、臺灣地名、on／in／by。bank、beach、pool、spring 前面出現過，這裡是河岸、泉水等意思；mountain 的例句用 `exsay` 讓 Mt. 唸成 Mount。
  - 照片挑選：每個字 4 張候選拼成對照表逐張看，不選有槍、法官假髮、太暗或恐怖的；工具（cand／sheet／pick 腳本）放在 scratchpad，不在 repo，做法同 Unit 17 的說明。
- **Unit 26～30（2026-11-19 公司電腦，同一天接著做）**：照課本字表做；五份測驗沒登入時用正確答案作答都全對；`UNITS` 已加 `w2000_u26`～`u30`，已重跑 `build_wordup_index.py`。
  - **Unit 26 Animals & insects 動物與昆蟲**（印刷頁第 82–84 頁）：38 字。測驗 29 題 29/29；38 張照片、152 個音檔；重點整理：特別的複數（mice、geese、sheep、fish）、叫聲與寶寶、bite 三態。
  - **Unit 27 Articles & determiners 冠詞與限定詞**（第 87 頁）：14 字（a、every、the、this、that、these、those、my、our、your、his、her、its、their）。字 `a` 用 `say='a, an'`。測驗 24 題 24/24；56 個音檔。
  - **Unit 28 Pronouns & reflexives 代名詞與反身代名詞**（第 88–89 頁）：21 字（all … something）；課本的人稱代名詞表放在重點整理。測驗 25 題 25/25；84 個音檔。
  - **Unit 29 Wh-words 疑問詞**（第 91 頁）：9 字。測驗 19 題 19/19；36 個音檔；重點整理：問什麼答什麼、how 家族、間接問句。
  - **Unit 30 Be & auxiliaries be 動詞與助動詞**（第 92 頁）：22 字。測驗 24 題 24/24；88 個音檔；重點整理：be 動詞配主詞、do／have 變化、助動詞＋原形。
  - Unit 27～30 是功能詞，沒有適合的照片，全部用 emoji（沒有 img 資料夾）。
- **Unit 31～40（2026-11-19 公司電腦，同一天接著做）＝主題 2000 字 40 個單元的 u01、u02、u13～u40 都有資料檔了**（u03～u12 仍是直接改 HTML）。照課本字表做，例句、中文、題目自編；`UNITS` 已加 `w2000_u31`～`u40`。
  - 31 Prepositions 介系詞（印刷頁第 94–96 頁）38 字；32 Conjunctions 連接詞（第 98 頁）12 字；33 Interjections 感嘆詞（第 98 頁下半）4 字；34 Other nouns 其他名詞（第 100–104 頁）**111 字**，41 張照片；35 Other verbs (1)（第 107–108 頁）33 字，4 張照片；36 Other verbs (2)（第 111–112 頁）37 字，17 張照片；37 Other verbs (3)（第 115–116 頁）38 字，16 張照片；38 Other verbs (4)（第 119–121 頁）54 字，10 張照片；39 Other adjectives 其他形容詞（第 124–126 頁）66 字；40 Other adverbs 其他副詞（第 129–130 頁）36 字。功能詞、抽象名詞、形容詞、副詞用 emoji。
  - 課本重複收的字（like、since、than、that、check、treat、correct、other、own…）照課本保留，各單元用該單元的意思。
  - **⚠️ 測試事故（2026-11-19）**：用正確答案自動作答 u31～u40 測驗時，內建瀏覽器的 localhost:8765 **已經用 MELISSA 登入**（有她的點數憑證），結果 10 份測驗以 MELISSA 的名義全對送出——**試算表多了 10 筆 Vocab W2000 U31～U40 的成績，點數存摺也幫 MELISSA 記了點（當天上限 50 點＋連續紅利）**，要由家長到試算表刪掉這 10 筆、在存摺扣回點數。本機（localhost）的 vocabProgress／vocabWords 已清掉。**以後自動測驗前先確認沒有登入**（`quizStudentName` 是空的，或改用沒登入過的網址），有登入就不要按送出。
  - u31～u38 測驗在送出前確認全對；u39、u40 只用程式檢查題目資料（答案位置、空格數），沒有在瀏覽器作答。
  - 單字區主題 2000 字 40 個單元全部完成；之後可做 LaLa Word 18 單元（一字多義・易混淆・字首字尾，見本節開頭）。
- **音檔合併（2026-11-20，整個英文測驗系統）**：Cloudflare Pages 上限 20000 個檔，原本 5711 個小 mp3 合併成每個單元一個 `all.mp3`（＋對照表 `all.json`），全站檔案數從約 19,417 降到約 13,902。工具 `tools/vocab_gen/sprite_audio.py`：
  - 範圍：單字區（w2000 u01～u40、lala u01～u18、wordup u01～u02 的單字卡＋投影片）、文法區 `grammar2/uNN-slides.html`、第二期 `course2/*/slides.html`。`python tools/vocab_gen/sprite_audio.py --all [--delete]` 一次全部；單一單元見檔頭說明。
  - 做法：每段之間 0.6 秒靜音，固定位元率約 64 kbps（原本約 43 kbps）；頁面 `data-src` 改成 `audio/uNN/all.mp3#t=開始,結束`。合併後會逐段和原檔比對響度起伏（全部 ≥0.99），不通過就不刪小檔。使用者 11-20 試聽 w2000 Unit 14 後同意全部套用。
  - 播放：`vocab/vocab.js` 和投影片的 `play()` 會在 `#t` 結尾停（timeupdate＋pause 兩種都處理，瀏覽器自己停時只觸發 pause）。存字卡時 `vocab.js`／`gquiz.js` 的路徑保留 `#t=`。快取版本 `vocab.js`、`gquiz.js?v=20261120a`。
  - 「我的字卡」（首頁 repo `cards/index.html`）：播 `#t=` 片段；**舊字卡存的小檔路徑**讀不到時，查同資料夾 `all.json` 找合併檔的位置。
  - **之後改單元／新做單元**：照舊用 build_vocab／build_lala／build_slides 產生頁面、錄音（小檔），**最後一定要再跑 `sprite_audio.py`（加 `--delete`）**：頁面上的小檔名會照 all.json 換回 `#t=`，已刪的小檔從舊 all.mp3 切回，新錄的一起合併。注意錄音清單會包含已刪的舊句子（tts_mp3 會全部重錄、比較久）；只想錄新句子時，先把清單裡已在 all.json 的刪掉。
- **投影片音檔共用（2026-11-20）**：網站總檔案數超過 Cloudflare Pages 20000 個上限（部署會失敗），原因是單字區投影片每個 🔊 都有自己的 `slide-NN.mp3`，內容和單字卡的 `w-NN`／`e-NN` 一模一樣。新增 `tools/vocab_gen/link_slide_audio.py`：投影片按鈕加 `data-src` 指到單字卡音檔，播放程式有 `data-src` 就用它（沒有才用 slide-NN）；`--delete` 刪掉不再用的 slide 音檔。已處理 42 個投影片頁（含 u03～u12、WORD UP u01～u02），刪掉 2722 個檔，只剩 u01 的 slide-37～40（two children 等複數唸法）。`build_vocab.py` 產生投影片時也會自動連，`audio_jobs` 只錄沒有對應的 slide 句子。同一天也跑了 `boost_audio.py`，u21～u40 的 1205 個檔放大音量（和 u01～u20 一致）。
- **LaLa Word 一字多義區 `vocab/lala/`（2026-11-20 開始，使用者說「另一區做 LaLa Word」）**：照翰林《LaLa Word 小單字大視野》18 單元。課本在公司電腦 `I:\興雅\英文\115二上翰林\115[翰林]國中英語LaLa Word小單字大視野_課本_學用.pdf`（228 頁、掃描圖檔，PDF 頁序＝印刷頁碼－1；目錄在 PDF 第 4、5 頁）。每單元：主題閱讀＋一字多義（主題單字＋更多單字）＋（部分單元）易混淆字、字首字尾＋單字力檢測。**只用課本的字表和每個字有哪些意思；例句、中文、題目都自編，主題閱讀文章不搬。**
  - 產生程式 `tools/vocab_gen/build_lala.py`（借用 build_vocab.py 的模板、照片、投影片外框），資料檔 `lala_uNN.py`：`W(字, emoji, [S(詞性, 中文, 例句, 例句中文, 片語)…], 變化形, key=主題單字)`。單字卡沿用 `.vc-card`／`.vc-word`／`.vc-zh`／`.vc-en` 結構（多個意思排成 `ol.vs-list`），所以學習進度、我的字卡、自動補「看中文選英文」都照常。音檔 `vocab/lala/audio/uNN/w-NN.mp3`（單字）、`e-NN-K.mp3`（第 K 個意思的例句）；投影片一個字一頁，直接用這些音檔（不錄 slide 檔）。測驗 label `Vocab LALA UN`；題目 `<b>字</b>` 會自動記成考哪個字（`it.w`）。
  - 題型：① 這個字在句子裡是什麼意思（選中文）② 選出可以同時填入兩句的字 ③ 例句填空（中文提示）。
  - 產生：一行指令 `build(m)` 輸出錄音清單 → `tts_mp3.py` → `boost_audio.py vocab/lala/audio/uNN`；照片照主題 2000 字的做法（`vocab/lala/img/uNN/`）。
  - **Unit 1 Colors Can Talk!（2026-11-20）**：印刷頁第 7–19 頁，30 字（主題單字 color～down 7 個＋更多單字 23 個）、94 個意思、30 張照片、124 個音檔；測驗 22 題，在 127.0.0.1（確認沒登入）用正確答案作答 22/22，成績沒有回傳。Unit 2 The Secret Clothes of Animals 從印刷頁第 20 頁起（有「易混淆字」look／watch／see／read）。
  - **Unit 2～10（2026-11-20 同一天）**：字表照目錄（PDF 第 4、5 頁）和各單元字表頁；易混淆字、字首字尾（un-、-ist、-ous）做成重點整理表（`focus`），字首字尾的字（unhappy、artist、famous…）也做成單字卡；有易混淆字的單元，測驗多一節「易混淆字」選擇題。字數／意思數／題數：U2 22／87／27、U3 13／51／26、U4 17／64／20、U5 18／65／24、U6 20／70／20、U7 16／52／26、U8 27／81／26、U9 23／79／26、U10 16／57／26；照片共 177 張（抽象字、負面形容詞如 mean 用 emoji）。9 份測驗在 127.0.0.1（沒登入）用正確答案作答全對、沒有回傳；所有單字卡／投影片的 2198 個音檔、照片連結都存在。
  - **Unit 11～18（2026-11-20 同一天）＝LaLa Word 18 單元全部完成**。字數／意思數／題數：U11 23／87／24、U12 23／84／20、U13 32／84／25、U14 19／60／25、U15 30／97／26、U16 25／58／26、U17 10／42／24、U18 21／77／20；全區 349 張照片、1674 個音檔。8 份測驗在 127.0.0.1（沒登入）作答全對、沒有回傳；所有 4046 個音檔、照片連結都存在。易混淆字：U11 let／have／make、U13 wish／hope、U14 cross／across、take／bring／carry、U15 probably／possible／perhaps、except／besides／beside、U16 quiet／quite、along／alone／lonely、U17 gift／present；字首字尾：U13 -er／-or、-ess、inter-、U15 im-、-less、U16 -ful、re-。
  - 自動作答注意：內建瀏覽器的分頁在背景時計時器會被放慢，用 `await sleep()` 的作答程式會逾時；改成不用等待、每題重新 querySelector，送出用 `setTimeout(()=>btn.click(),0)`，再用另一個呼叫讀結果。**不要在使用者正在看的分頁跑**（11-20 曾誤把使用者 bmlearn 分頁導到 u11 測驗頁，當時還沒上線、沒作答，已導回），一律自己開新分頁。
  - `build_lala.py` 改成自動抓 `tools/vocab_gen/lala_uNN.py`（不用再改 `UNITS`），可指定單元：`python tools/vocab_gen/build_lala.py 11 12`（只產生 Unit 11、12；錄音清單寫到 `audio_jobs.json`）。
  - 讀課本的做法：scratchpad 的 `lpages.py 起頁 迄頁 輸出資料夾` 把兩頁拼一張圖讀（印刷頁碼）；照片同主題 2000 字（Pexels 候選 → 拼圖逐張看 → `pick.py uNN 選擇檔 lala`）。
  - **全站檔案數**：LaLa 18 單元做完後六個 repo 約 19,417 個（上限 20,000）；同一天做了「音檔合併」（見下面）降到約 **13,902 個**。美式生活館（4,670 個 mp3）、圖解單字（2,552 個）還沒合併，需要時可用同樣做法。
  - 本機測試注意：`localhost:8765` 的瀏覽器還是 MELISSA 登入，**測驗一律在 `127.0.0.1:8765` 測，送出前先確認 `quizStudentName` 是空的**。
- **網站沒更新時**：Cloudflare 部署由首頁 repo 的 Actions 每 15 分鐘檢查，但 GitHub 的定時工作常常延遲好幾小時（2026-11-19 16:45 之後就沒跑）；急的話到首頁 repo GitHub → Actions →「部署到 Cloudflare Pages」→ Run workflow 手動跑。
- **單字學習進度：紅字複習、答對變灰（2026-11-04 使用者要求，取代同一天早先的「答錯標紅」）**：
  - 每個登入者各自的進度存在這台裝置 localStorage `vocabProgress:<單字卡頁路徑>:<登入者>` = `{mastered:[第一次就答對的字], wrong:[答錯的字], total, at}`（沒有存到雲端）。
  - `gquiz.js`（label 開頭 `Vocab` 的測驗、有登入時）先 fetch 單字卡頁取得全部單字，`wordsOf()` 找出每題考到哪些字（選擇題看正解與單字題目、填空看正解、「swim → (V-ing)」算原形，允許複數／V-ing）。**第一次測驗每個字都要考到**：課本題目沒考到的字自動補「⑦ 其他單字：看中文選英文」（所以大單元第一次題數多，例如 Unit 16 有 81 題）。之後**只出還有沒答對的字的題目**；對不到單字的題目（the／不填）只在第一次出。只看第一次作答：答對的字變 mastered（灰）、答錯變 wrong（紅），訂正後仍是紅，下次再考。全部答對時測驗頁顯示「全部答對、不用再背」，可「清除紀錄、全部重新測驗」。
  - 單字卡頁 `vocab.js` 的 `showProgress()`：紅框紅字＝要複習、暗灰色＝已答對、上方「📊 我的學習進度」顯示答對率、答對幾個、還有幾個紅字（列出來）、幾個還沒考到；全部答對整頁變灰。PARENT／TEST 看 BRANDEN、MELISSA 兩人的統計（卡片只標紅）。
  - 單字區目錄 `vocab/index.html` 底部的 script 在各單元卡片顯示「答對率 ％、紅字 N 個」或「✅ 全部答對」，全部答對的單元卡片變灰。
  - 快取版本 `gquiz.js?v=20261104c`、`vocab.css`／`vocab.js?v=20261104c`（`build_vocab.py` 模板已改）。改了這些檔要把所有頁面的 v 一起改。
- **WORD UP 整合（2026-11-04 試做 A-I）**：孩子另外用付費的 WORD UP（app.wordup.com.tw，教材「全民英檢初級單字一本通」，實詞篇 59 個單元 A-I、A-II…）。WORD UP 沒有匯出、沒有 API；做法是**家長在內建瀏覽器自己登入**後，Claude 讀單元頁的字卡：字卡上方色條＝熟悉度（沒色條＝熟記、`bg-green-500`＝不太熟、`bg-yellow-500`＝很模糊、`bg-peach-500`＝沒印象），星號按鈕 aria-label 以「取消」開頭＝有星號。**只讀英文單字、熟悉度、星號，不抄 WORD UP 的中文、例句、發音**。
  - 讀到的資料寫在 `vocab/wordup/status.json`（`units`：53 個單元字表 u01＝A-I … u53＝W+Y+Z-II，共 2071 字；`users.<學生>.words`：單字 → [熟悉度, 星號]）。由 `tools/vocab_gen/build_wordup_status.py 學生=讀取檔` 產生（讀取檔每行一個單元：`單元|熟記/不太熟/很模糊/沒印象|單字~等級[*],…`，還沒開始背的單元 `|U|單字,…`）。**還沒開始背的單元（熟記、不太熟、很模糊都是 0）只記字表、不記熟悉度**，不然整單元都會被標紅。
  - 讀取方法：在 deck 頁用 JS 抓字卡，按「下一單元」一頁一頁讀，**每讀幾個單元就把結果存出來**（整頁換址會清掉頁面裡的變數）；最後一個單元的「下一單元」會進到 WORD UP 的題目頁，讀到非 /decks/ 網址就退回。每個單元都比對過 WORD UP 側欄的熟悉度統計。
  - 2026-11-04：**兩人全部 53 單元都已讀**。BRANDEN 已背 51 單元（記錄 1989 字：已會 795、要複習 1194）；MELISSA 已背 23 單元 A-I～H-II（記錄 864 字：已會 229、要複習 635）。之後要更新：家長登入該學生的 WORD UP → 讀取 → `build_wordup_status.py 學生=讀取檔` → `build_wordup_index.py`。
  - WORD UP 複習單元（自編內容的單字卡／投影片／測驗）照 A→Z 順序一個一個做：已做 A-I（u01）、A-II（u02）；其餘還沒做，對照表上標「（製作中）」。做法：資料檔 `tools/vocab_gen/wordup_uNN.py`（字表照 status.json 的 `units.uNN`，課本題目只出 10～15 題，其餘由測驗自動補「看中文選英文」）→ 照片 `vocab/wordup/img/uNN/` → 一行指令 `build(m)` 產生 → 錄音 → 重跑 `build_wordup_index.py` → 單字區目錄加卡片。對照表最右欄「本站在哪裡複習」列出主題單元和 WORD UP 複習單元。
  - WORD UP 複習區 `vocab/wordup/uNN.html`（Unit 1＝A-I）：用 `build_vocab.py` 的 book `wordup` 產生（資料檔 `tools/vocab_gen/wordup_u01.py`，中文、例句、題目自編；照片 `vocab/wordup/img/u01/`）。對照表 `vocab/wordup/index.html` 由 `tools/vocab_gen/build_wordup_index.py` 產生（每個字的熟悉度＋在本站哪個主題單元；新做主題單元或新增 WORD UP 單元後重跑）。單字區目錄有「WORD UP 單字複習」一區。
  - **進度共用**：本站答題紀錄改存 `vocabWords:<登入者>`（小寫單字 → 'm' 答對／'w' 答錯，所有單元共用）；`gquiz.js`／`vocab.js` 判斷每個字：本站答過的優先，沒答過才看 WORD UP。主題單元裡同一個字也會一起變紅／灰。
  - **以本站測驗為準（2026-11-04 使用者決定）**：WORD UP 的熟悉度是孩子自己按的，只當參考——WORD UP 不熟（不太熟／很模糊／沒印象）→ 紅色＋「WORD UP：沒印象」標籤，提醒先複習；WORD UP 熟記 → **不變灰**，只標藍色小標籤「WORD UP 熟記（待測驗）」，測驗照樣要考。**只有本站測驗答對才變灰、才算已會**（答對率也只算本站答對）。A–Z 對照表統計分成：本站答對、要複習、WORD UP 熟記待測驗、還沒背。快取版本 `gquiz.js`／`vocab.js`／`vocab.css?v=20261104e`。
- 總目錄 `index.html` 第五張卡片「國中2000字．分科練習」（寬螢幕 5 欄、1300px 以下 3 欄、900px 以下 2 欄、手機 1 欄）。

## 寫作園地 `writing/`（2026-11-21 使用者要求「主題、引導式、跟『說』結合、生活化、英檢能力範圍內，讓 BRANDEN 和 MELISSA 思考造句」）

- 首頁 Hub 卡片「Writing Hub｜寫作園地」連到 `/english-quiz/writing/`（目錄：已做的主題＋規劃中的主題標「製作中」，卡片顯示這台裝置的完成狀態）。
- 每個主題 5 步（`uNN.html`）：① 聽一段對話（兩種聲音）＋回答 4 個問題（🎤 語音轉文字，`SpeechRecognition`，不支援的瀏覽器隱藏麥克風）② 字詞庫 14 個（🔊、☆ 存字卡）③ 句型填空 6 句（看例句）④ 造句練習 `uNN-quiz.html`（英檢初級寫作第一部分：句子合併、改寫、重組各 5 題，用 `grammar2/gquiz.js`＝段考題庫規則、計點、訂正，label `Writing UN`，整句作答寬鬆比對：大小寫、句尾標點、縮寫都不計較）⑤ 寫短文：★ 30 字／用 2 個字詞，★★ 50 字（英檢段落寫作長度）／3 個字詞／要有連接詞；步驟 ①③ 寫的句子可按「＋」放進短文。
- ⑤ 的檢查（使用者選定的免費組合）：程式自動檢查（字數、句首大寫與 I、句尾標點、用到字詞庫幾個、★★ 連接詞），全部通過才能送出；「🔍 檢查我的作文」→ `/api/write-check`（首頁 repo `functions/api/write-check.js`）回傳 LanguageTool 文法拼字＋Cloudflare Workers AI 老師建議（繁中讚美、最多 3 個修改、加細節的點子）；後端沒有或連不上時，前端直接呼叫 LanguageTool（本機測試就是這樣）。LanguageTool 的建議可按「改成…」直接套用。每篇每天最多檢查 10 次。**AI 要家長在 Cloudflare 加 Workers AI 綁定（變數名稱 `AI`）**，步驟在首頁 repo `CLOUDFLARE-SETUP.md` 第九節；沒開時顯示「AI 建議還沒啟用」。
- 送出：存到測驗同一份試算表（`week` = `Writing UN`、`mode` = `寫作短文 ★／★★`，details 第一筆是整篇作文，另有字數、剩下的文法提醒、AI 建議），`Points.earn`（correct = 通過的檢查數＋文法零錯誤 1，total = 檢查數＋1）；送出後看兩級範文（🔊）。草稿存這台裝置 `wr:<頁面>:<登入者>`。沒登入只顯示範文、不送出。
- 產生：內容在 `tools/writing_gen/wr_uNN.py`（UNIT：dialog／speak／words（含比對用 regex）／frames／write（prompt、引導問題、兩級範文）＋QUIZ），`python tools/writing_gen/build_writing.py` 產生頁面與錄音清單 → `tts_mp3.py tools/writing_gen/audio_jobs.json`（清單第 3 欄可指定聲音，對話第二人用 `am_michael`）→ `boost_audio.py writing/audio/uNN` → `sprite_audio.py writing uNN.html audio/uNN --delete`（`--all` 也包含寫作園地）。
- 已做：Unit 1 My Weekend 我的週末、Unit 2 My Pet 我的寵物（各 48 段語音、合併成 all.mp3）。兩份造句練習在 127.0.0.1（沒登入）用正確答案作答 15/15；短文的自動檢查、LanguageTool、套用修改、送出（沒登入）都在瀏覽器測過；手機寬度沒有超出。**Workers AI 那一段還沒實測**（要部署＋家長開綁定後，在 bmlearn 登入測）。
- 規劃中的主題（目錄上「製作中」）：我的家人、學校的一天、我最喜歡的食物、生日派對、去買東西、問路、臺灣的節日、一次旅行、我的夢想、寫邀請卡、寫道歉卡片（`build_writing.py` 的 `PLANNED`）。
- 家長看作文：目前在測驗試算表看；之後可考慮做「家長評語」回寫給孩子（要改 Apps Script）。

## 我的字卡（2026-11-17 使用者要求，手機雲端版）

- 登入者可以把單字／句子存成字卡、自己分類；字卡存在點數存摺同一份 Google 試算表的「字卡」「字卡分類」分頁（每人一份，手機、平板、電腦同步）。後端是 english-quiz-plan `points/Code.gs` 的 `cardlist／cardsave／carddel／cardmove／cardstatus／deckadd／deckrename／deckdel`（用存摺的登入憑證；同一人同一個英文只存一張；答錯再加入時「錯次」+1）。**要重新部署 Apps Script 才能用**，沒部署前按 ☆ 會提示「後端還沒更新」。
- 全站共用前端 `/cards/cards.js`（首頁 repo）：`Cards.btn(card)` 產生「☆」按鈕（點了選分類／新分類存起來，已存的變 ★，可改分類或移除）；`Cards.addWrong([card…])` 把測驗答錯的字自動放進「錯題」。card 欄位：en、zh、pos、ex、exzh、img、audio（網站根目錄開頭的絕對路徑）、src（來源名稱）、url。需要 `points.js`（它開放了 `Points.call／Points.auth／Points.who` 給字卡用，7 份副本一致）。
- 「我的字卡」頁 `/cards/`（首頁 repo；首頁右上角「📇 我的字卡」、App 入口頁都有連結）：分類（新增、改名、刪除→卡片移到未分類）、字卡列表（多選後移動、刪除、標會了／還不會）、🔄 翻卡複習（可只看還不會的）、✏️ 小測驗（看中文選英文＋拼字，照段考題庫規則用 `/cards/fixkit.js`：送出、對答案、訂正、補送 1 點、暫存；答錯的字再加進錯題；點數 label `Cards｜分類名`）、🖨️ 印出（左正面右背面，對摺剪下）。
- 各站接法：圖解單字 `topic.html`（單字卡 ☆、三種測驗答錯自動加入）；英文測驗系統 `vocab/vocab.js`（國中2000字單字卡頁 ☆，會自動載入 points.js）、`grammar2/gquiz.js`（單字區測驗答錯自動加入）、`eqfix.js`（每週測驗的單字題 ☆、答錯自動加入）；國家地理閱讀 `points-glue.js`（Vocabulary 卡 ☆、克漏字答錯自動加入）；美式生活館 `engine.js`、`units.html`（場景單字、你要說的、你會聽到的句子 ☆）。段考題庫沒有接（題型不是單字卡）。
- 這個 repo：`vocab.js?v=20261117a`、`gquiz.js?v=20261117a`、`eqfix.js?v=20261117a`（各頁 v 已一起改，`build_vocab.py` 模板也改了）。

## 全站字典（2026-11-18 使用者要求，手機雲端版）

- 各單元的英文（文章、文法講解、對話、投影片、單字卡、測驗解答）都能查字典：電腦**點兩下**英文字、手機平板**長按**（選取 1～3 個英文字會出現「🔍 查字典」按鈕）→ 小框顯示中文意思、程度（國中／高中）、原形（went→go、bears→bear）、🔊 發音（瀏覽器語音，沒有語音的裝置不會出錯）、☆ 存字卡、劍橋／Yahoo 外部字典、📖 字典頁、✏️ 自己加字卡（外部字典查到的意思可以貼上、改好再存成字卡）。
- **測驗還沒送出成績時不能查**（跳出「🔒 測驗還沒送出成績，先不能查字典喔！」）；送出後看解答、訂正中可以查（一題一題的英文測驗系統、美式生活館是「這一題還沒送出」不能查）。判斷寫在 `/dict/dict.js` 的 `blocked()`：段考題庫 `#examSubmitBtn`＋body `exam-locked`／`.q.fixing`、文法與單字測驗 `[data-act="submit"]`、每週測驗 `#nextBtn` 的 `data-fk-stage="pick"`、圖解單字 `#go`「送出成績」、fixkit 的 `kit.status==='open'`＋`kit.box`、美式生活館 `.qtop` 那一題的 `button.next` 還沒啟用。**新做的測驗**：照這些既有寫法就會自動擋；不一樣的寫法用 `(window.DictGuard = window.DictGuard || []).push(el => 要擋就回 true)`。不想被查的區塊加 `data-dict-off`。
- 字典資料 `/dict/data/a.json～z.json`（首頁 repo，約 3.6 萬個常用字＋2.8 萬個變化形，共 2.7 MB，查哪個字母才下載那一份）、`zh.json`（中文查英文用）；由首頁 repo `tools/dict/build_dict.py` 從 ECDICT（MIT 授權，`dict/data/LICENSE-ECDICT.txt`）產生，中文用 OpenCC s2twp 轉台灣繁體。
- 字典頁 `/dict/`（首頁右上角「🔍 查字典」、App 入口、我的字卡頁上方都有連結）：輸入英文（列出開頭相同的字）或中文（列出意思裡有這個詞的字）查；「🕘 查詢紀錄」（`/dict/#hist`）看自己查過哪些字、查了幾次，可排序、存字卡、刪除。
- 查詢紀錄：先存這台裝置（localStorage `dictHist:<登入者>`），有登入憑證時批次送到存摺試算表「查詢紀錄」分頁（Code.gs `dictlog／dictlist／dictdel`，`dictQ:<登入者>` 是還沒送出的佇列）。**要重新部署 Apps Script 才會同步到雲端**，沒部署前只記在各裝置。
- 載入方式：`points.js` 會自動載入 `/dict/dict.js?v=20261118a`（7 份副本一致；也開放了 `Points.tokenOf`）；沒載入 points.js 的頁面（文法講解、各種投影片、目錄頁）直接在 `</body>` 前加 `<script src="/dict/dict.js?v=20261118a" defer></script>`。查字典不會跳出登入關卡，按 ☆ 存字卡時才載入 points.js／cards.js。改 dict.js 要把 v 一起改。
- 這個 repo：96 個沒有 points.js 的頁面（文法講解 `grammar2/uNN.html`、投影片、單字投影片、目錄）加了 dict.js 的 script；投影片共用的 `tools/course2_gen/slides_tail.html` 也加了（文法、單字投影片產生器都用它），重新產生不會掉。

## WORD UP（已購買的網頁版）整合（2026-11-18 手機雲端版）

- 使用者在 WORD UP 網頁版（app.wordup.com.tw）有兩本書：《全民英檢初級單字一本通》（背單字）、《準！GEPT 新制全民英檢初級初試 10 回》（聽力＋閱讀模擬試題，2026-11-18 進度 12%）。使用者說的「全民英檢」就是第二本，也在 WORD UP 裡。
- WORD UP 沒有匯出、沒有 API，題目、中文、例句、音檔有版權，不搬進學習館；做法是放入口連結，加上家長在**電腦**的內建瀏覽器登入後讀取進度（雲端版不能登入使用者的帳號）。
- 已做：首頁卡片「WORD UP｜全民英檢單字＋模擬試題」、App 入口一張（都連到 app.wordup.com.tw，另開分頁，`sw.js` CACHE `bm-app-v5`）；字典小框顯示「🃏 WORD UP 單元名稱＋熟悉度」（讀 `/english-quiz/vocab/wordup/status.json`；學生看自己的，PARENT／TEST 看兩人的；本站測驗答對的字加註「本站測驗已答對」），程式在 `dict/dict.js` 的 `wordupHtml()`，dict.js 內部版本 `V = '20261118b'`。
- **2026-11-18（電腦版）讀了 BRANDEN 的 WORD UP**（帳號 brandenlin，家長在內建瀏覽器登入）：
  - 單字熟悉度：53 個單元全部重讀，每個單元都和側欄統計核對過，寫進 `status.json`（`build_wordup_status.py BRANDEN=讀取檔`）→ 重跑 `build_wordup_index.py`。已背 51 單元、記錄 1989 字（F-III、W+Y+Z-II 還沒背）。MELISSA 也在同一天重讀了（見下面）。
  - 讀取的 JS 做法：deck 頁是 SPA，按「下一單元」不會清掉 `window` 變數；每張字卡是 `article`，單字在 `span.type-title`，色條 class 判斷熟悉度，星號看 aria-label「取消 … 的星號」，讀到的行存在 `sessionStorage` 防掉。
  - **GEPT 10 回成績**：使用者選定做法＝新增 `vocab/wordup/gept.json`（每回聽力 4 部分、閱讀 3 部分的 [答對, 已做, 總題數]、`date`、`read` 讀取日期），WORD UP 對照表頁（`vocab/wordup/index.html`）上方加「📝 GEPT 初級模擬試題成績」表（登入後顯示；學生看自己的，PARENT／TEST 看兩人；第 1～10 回，答對率 ≥80% 綠、≥60% 橘、其餘紅）。表格由頁面 JS 讀 gept.json 畫，**之後只要更新 gept.json**，不用重跑產生程式。
  - 讀法：教材頁 `materials/1230`，各單元下方「正確率 x/y」＝有錯題；**全對的單元不顯示正確率**（側欄實心藍＝完成、橘框＝有錯題、空白＝未完成）；用頁面上方「做對的題目 N / 600」核對總數。WORD UP 沒顯示作答日期，所以 `date` 是 null（表上寫「—」）。
  - BRANDEN 2026-11-18：第 1 回聽力 22/30（看圖 4/5、問答 4/10、對話 9/10、短文 5/5）、閱讀 30/30；第 2 回只做了聽力 1–5（0/5）；第 3～10 回還沒做。分數換算表是書的內容，沒有抄進來，只記答對題數。
  - **MELISSA（同一天）**：單字 53 單元重讀並核對，已背 23 單元 A-I～H-II（F-III 還沒背）、記錄 864 字。GEPT 第 1 回聽力 22/30（看圖 3/5、問答 8/10、對話 8/10、短文 3/5）、閱讀 19/30（詞彙 6/10、段落填空 5/8、閱讀理解 8/12）；第 2 回聽力 21/30（2/5、8/10、7/10、4/5）、閱讀只做了詞彙 1–5（5/5）；合計 67 題＝WORD UP「做對的題目 67 / 600」。只讀已背單元時，可以用 status.json 的字表補上還沒背的單元（`U` 行），再跑 `build_wordup_status.py`（單元順序要照 status.json）。
  - `build_wordup_index.py` 模板補上了 `/dict/dict.js` 的 script（11-18 手動加在 index.html 的，重跑才不會掉）。
  - 已知問題（沒動）：對照表頁在手機寬度會比螢幕寬約 50px，是原本 A–Z 單字表造成的。
- 待辦（等使用者選）：① WORD UP 剩下 51 個複習單元（自編內容）② ~~GEPT 成績整理進學習館~~（11-18 已做，之後定期更新 gept.json）③ 自己出題的全民英檢初級形式練習（聽力、閱讀，照段考題庫規則）④ 熟悉度、GEPT 成績定期更新（電腦；兩人都是 2026-11-18 的資料）。

## 連續學習紅利＋稱讚畫面（2026-10-18）

- 送出測驗後跳出稱讚卡（得幾點、連續第幾天、還差幾點到 100 點）；每跨過 100 點跳出大的恭喜兌換畫面。
- 連續學習紅利：第 2 天 +2、第 3、4 天 +3、第 5 天起每天 +4（2026-10-18 使用者改），中斷就重算；不算在每天 50 點上限內；存摺分頁記成類型「紅利」。
- **答對率計分（2026-10-18）**：答對 1 題得幾點看答對率（第三版，2026-10-18 使用者定）：低於 30% 0.25、30～50% 0.5、50～60% 0.8、60～70% 1、70～90% 1.2、90% 以上 1.5、全對 2，四捨五入成整數（80～90% 使用者沒另外寫，同 7～8 成）；後端 `Code.gs` 的 `CONFIG.RATE_TIERS`，要重新部署 Apps Script 才生效。
- **段考訂正完成補送 1 點（2026-10-18）**：段考題庫錯題全部訂正完成後 `Points.earn({kind:'fix-bonus'})`，後端 `fixBonus_()` 記一筆類型「訂正獎勵」+`CONFIG.FIX_BONUS`（1）點，同一份考卷每天一次、不算每天上限與連續天數；要重新部署 Apps Script 才生效（舊版後端會當成一般賺點、全對每題 2 點＝給 2 點）。
- 程式在 `points.js`（7 份副本內容一致，主檔在 english-quiz-plan `points/points.js`）與後端 `Code.gs`（`CONFIG.STREAK_BONUS`）。
- **要先更新 Apps Script 後端（貼新版 Code.gs → 部署新版本）紅利才會開始算**，步驟在 english-quiz-plan `points/README-點數存摺.md` 最後一節。

## 單字卡「全部播放」加暫停／停止（2026-11-22 使用者回報）
- 問題：按「▶ 全部播放」後停不下來、畫面一直往下捲。
- `vocab/vocab.js`：播放中畫面下方中間出現控制列（第幾個字／共幾個、⏸ 暫停 ↔ ▶ 繼續、⏹ 停止）；「全部播放」按鈕播放中變「⏹ 停止播放」，再按一次就停；Esc、離開頁面、點單字的 🔊 也會停。暫停後繼續會從暫停的那個字重唸。用 `gen` 計數避免停止後舊的播放回呼又接下一個字。
- 國中2000字、拉拉、WORD UP 共 62 頁 `vocab.js?v=20261122a`（`build_vocab.py` 模板也改了）。

## WORD UP 複習區獨立、主題 2000 字 PART 2（2026-11-22 公司電腦）
- **WORD UP 單字複習搬出單字區目錄**（使用者要求「放到上一層 Vocabulary Hub，成為獨立，不要跟國中2000字放一起」）：新目錄頁 `vocab/wordup/units.html`（對照表＋到 WORD UP 網站＋各複習單元卡片）；首頁 repo `/vocab/` 多一張卡「03 WORD UP 單字複習」；`vocab/index.html` 拿掉 WORD UP 那一區。WORD UP 各頁（uNN、slides、quiz、對照表）的返回連結改成 `units.html`「← WORD UP 目錄」；`build_vocab.py` 產生 book `wordup` 時自動換（`back()`），`build_wordup_index.py` 模板也改了。**之後新做 WORD UP 複習單元，卡片加在 `units.html`。**
- **主題 2000 字 PART 2**：翰林《單字2000活用練習》其實分兩部分——PART 1「1～1200 字彙」（印刷頁約 4–141，網站原本的 40 單元就是這部分）、PART 2「1201～2000 字彙」（印刷頁 144 起，同樣照 Unit 1–40 主題）。PART 2 原本完全沒做。課本 PDF 在公司電腦 `I:\興雅\英文\115二上翰林\115[翰林]國中英語單字2000活用練習_課本_學用.pdf`（掃描圖檔，PDF 頁序＝印刷頁碼－1）。
  - 新 book `w2000p2`（`BOOKS['w2000p2'] = '主題 2000 字 PART 2'`），資料檔 `tools/vocab_gen/w2000p2_uNN.py`，頁面在 `vocab/w2000p2/`，測驗 label `Vocab W2000P2 UN`。單字區目錄 `vocab/index.html` 新增「主題 2000 字 PART 2」一區（PART 1 標題改成「PART 1：1～1200 字」）。
  - 已做 Unit 1 People（16 字：adult…youth，測驗 23 題）、Unit 2 Personal characteristics（41 字：chubby…talkative，測驗 27 題；書上 over-weight／under-weight 用 overweight／underweight）。沒登入時用正確答案作答都全對。照片 51 張（Pexels，`vocab/w2000p2/img/uNN/`，PHOTO-CREDITS.md）；deaf、dishonest、humble、impolite、patient、selfish 用 emoji。音檔已錄、已放大、已合併成 all.mp3（`sprite_audio.py` 的 `--all` 清單加了 `vocab/w2000p2`）。
  - 產生方式（不動 `UNITS`）：`python -c` 匯入 `build_vocab` 和 `w2000p2_uNN` 後 `B.build(m)`，把回傳的 jobs 存成 json → `tts_mp3.py` → `boost_audio.py vocab/w2000p2/audio/uNN` → `sprite_audio.py vocab/w2000p2 uNN --delete` → `build_wordup_index.py`（對照表也會對到 PART 2）。選照片：內建瀏覽器在 pexels.com 用 fetch 搜尋頁抓候選 id → 下載縮圖拼成對照圖逐張看 → 下載選定的裁 4:3、640×480（腳本在 scratchpad，不在 repo）。
  - **PART 2 全部完成（2026-11-22，使用者看過 Unit 1、2 後說「照這樣繼續做」）**：39 頁、838 字（課本 PART 2 沒有 Unit 7、21、27、29、33；Unit 34 其他名詞 163 字拆成 34-1～34-4〔u34a～u34d〕、Unit 35～38 動詞 133 字照順序分四頁、Unit 39 形容詞 68 字拆成 39-1／39-2〔u39a、u39b〕）。每頁測驗沒登入時用正確答案作答都全對。照片約 520 張（抽象字、動詞、形容詞、副詞多用 emoji）。和 PART 1 或其他單元重複的字（sheet、shrimp、judge、complete、guide、memory 等）照課本保留，意思不同。
  - 工具（都在 tools/vocab_gen/）：`p2kit.py`（`W()` 建字、`auto_quiz()` 自動出「看中文選英文／看英文選中文／拼字」＋手寫的例句填空 `F()`；干擾選項排除同義字）、`build_p2.py u03 u34a …`（產生頁面→錄音→放大→合併 all.mp3→重跑對照表→重寫目錄卡片）、`p2_index.py`（`vocab/index.html` 的 P2-START～P2-END 區塊自動產生，不要手改）、`p2_check.py`（檢查資料檔）。拆頁：資料檔 UNIT 加 `'tag': 'u34a', 'part': 1`；`build_vocab.py`、`sprite_audio.py`、`build_wordup_index.py` 都支援 `uNN[a-z]`。
  - 課本字表讀法：公司電腦 I: 槽 PDF 是掃描圖，用 PyMuPDF 轉圖、左右欄切開逐頁看（Windows OCR 只有中文，英文抓不準，只當參考）。

- 2026-11-22 投影片上一頁鍵修正：第一期「第N週投影片」的上一頁鈕被投影片圖片蓋住（沒有 z-index）、看不到也按不到；其他投影片的箭頭是深灰半透明、在深色投影片上幾乎看不見。所有投影片頁（第一期、course2、grammar2、vocab、english-quiz-plan 的 course2 與 slidekit.py、tools/course2_gen/slides_head.html）在 </head> 前加一段 <style>/* arrow-visible 2026-11-22 */：箭頭改米白底深綠字、z-index:6、停用時 opacity .3。新做投影片沿用 slidekit／slides_head 就會帶到。

- **WORD UP u03～u05（2026-11-24 公司電腦，含錄音）**：A-III（38 字）、B-I（34 字）、B-II（34 字），資料檔 `tools/vocab_gen/wordup_u03.py`～`u05.py`（中文、例句、題目自編；照片沒找，全部用 emoji）。新增一行指令 `tools/vocab_gen/build_wordup.py u03 u04 u05`（產生頁面→錄音→放大→合併 all.mp3→重跑對照表；要先設 `KOKORO_DIR`，**公司電腦模型在 `C:\Users\jenlin2002\kokoro-models`，可以錄音**）。`units.html` 已加三張卡片。接下來照 A→Z 做 u06（B-III）起。
