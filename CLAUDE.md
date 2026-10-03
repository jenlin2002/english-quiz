# english-quiz 工作紀錄與說明

這個檔案是給「下一次接手的人」看的（包括在家裡電腦開 Claude Code 時，Claude 會自動讀這個檔案）。
最後更新：2026-10-03（在手機上用 Claude Code 雲端版完成的工作）。

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
2. **學習點數換電腦時間／零用錢**（等使用者決定）：
   - 要決定：兌換比例（例如答對 1 題 = 1 點、10 點 = 15 分鐘）、兌換項目（電腦時間、零用錢）、每日上限、
     並把 Google 試算表的 Apps Script 程式碼貼給 Claude 修改（加「點數存摺」與寄 email 通知）。
   - 建議做法：第一階段＝點數存摺＋孩子按「兌換」後寄 email 給家長，家長在 Microsoft Family Safety App
     核准孩子的「要求更多時間」。第二階段（選擇性）＝Home Assistant＋非官方 HAFamilySafety 自動核准。
   - 微軟沒有公開 Family Safety 的 API，無法直接用程式加時間。
   - 防刷分：同一測驗每天只算第一次、每日點數上限、連續學習獎勵。
   - 點數系統要同時用在 english-quiz 和美式生活館（兩邊都已經用同一個試算表網址同步成績）。
