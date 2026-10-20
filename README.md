# Python Learning Projects

2024 Python 自學過程中的練習專案，由基礎語法逐步進階到檔案處理，最後完成一個串接外部 API、以 Pipeline 架構設計的影片自動剪輯工具。

各專案原本是獨立的 repo，合併時保留了原始的 commit 歷史。

## 專案一覽

| 階段 | 專案 | 說明 | 練習重點 |
|------|------|------|----------|
| 01 基礎 | [temperature-converter](01-basics/temperature-converter/) | 攝氏轉華氏溫度換算 | 輸入輸出、型別轉換 |
| 01 基礎 | [driving-age-check](01-basics/driving-age-check/) | 依年齡與開車經驗判斷能否考駕照 | 條件判斷、輸入驗證 |
| 01 基礎 | [number-guessing-game](01-basics/number-guessing-game/) | 在指定範圍內猜隨機數字，提示大小並計算次數 | `random` 模組、`while` 迴圈 |
| 02 檔案處理 | [product-price-recorder](02-file-processing/product-price-recorder/) | 讀取既有商品清單、讓使用者新增商品並寫回 CSV | 函式拆分、CSV 讀寫、編碼處理 |
| 02 檔案處理 | [chat-log-analyzer](02-file-processing/chat-log-analyzer/) | 轉換對話紀錄格式，統計 LINE 對話中每人的字數、貼圖與圖片數 | 字串切割、資料統計 |
| 02 檔案處理 | [review-word-count](02-file-processing/review-word-count/) | 讀取大量評論資料，統計字詞出現次數並提供互動查詢 | 字典計數、大型檔案處理 |
| 03 綜合專案 | [youtube-clip-concat](03-youtube-clip-concat/) | 搜尋 YouTube 頻道字幕中的關鍵字，自動下載並剪輯成合輯影片 | 物件導向、Pipeline 設計、API 串接 |

## 執行方式

01 與 02 的專案只使用 Python 標準函式庫，進入資料夾後直接執行：

```bash
cd 01-basics/temperature-converter
python c_to_f.py
```

`02-file-processing` 的部分程式需要自備輸入資料檔（例如對話紀錄、評論文字檔），檔名寫在程式碼中。

03 綜合專案需要額外安裝套件與 YouTube Data API 金鑰，請見該資料夾的 [README](03-youtube-clip-concat/README.md)。

## 環境

- Python 3.10+
