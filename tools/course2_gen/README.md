# 第二期第 16–20 週的產生程式

這些程式產生了 `course2/w16`–`w20` 的投影片與測驗。要做類似的新週次時可以照著改。
**注意：直接執行 `build_all.py` 會用這裡的資料覆蓋 `course2/w16`–`w20`。**

| 檔案 | 用途 |
|---|---|
| `sl.py` | 投影片的小工具（卡片、例句、表格…），輸出和 w14 一樣格式的 slides.html |
| `slides_head.html`、`slides_tail.html` | 投影片的共用開頭（樣式）與結尾（程式），取自 w14 |
| `wNN_slides.py` | 每週投影片內容 |
| `qb.py` | 用 `course2/w14/quiz.html` 當範本，換上每週資料產生 quiz.html |
| `wNN_data.js` | 每週測驗題目（文法、閱讀、克漏字、聽力、單字、口說） |
| `checks.js` | 第 16 週以後新增的口說檢查規則（插進 analyzeSpeaking） |
| `build_all.py` | 一次產生第 16–20 週，並輸出 `audio_jobs.json`（投影片要錄的句子） |
| `tts.py` | 用 Kokoro 把句子錄成 mp3 |

錄音流程：`build_all.py` 產生 `audio_jobs.json` 後，把它轉成 `[[句子, 輸出路徑], …]` 的清單交給
`tts.py`（輸出路徑是 `course2/wNN/audio/slide-NN.mp3`，NN 依投影片中 🔊 按鈕的順序）。
模型檔放在 `models/`（或用環境變數 `KOKORO_DIR` 指定），不要放進 git。
