瑪奇 Mobile 外觀圖鑑：搜尋 / 圖片載入 / 分類網址修正包

上傳方式：
1. 解壓縮 ZIP。
2. 把 .github 和 scripts 兩個資料夾上傳到 GitHub repo 根目錄並覆蓋。
3. 到 Actions -> 新增搜尋與網址優化 -> Run workflow。
4. 跑完後等 pages-build-deployment 綠勾，再到網站 Ctrl + F5。

新增功能：
- 搜尋框：可搜中文名、韓文名、來源、期數、類型。
- 圖片 lazy loading：圖片滑到附近才載入，手機比較快。
- hash URL：分類與搜尋可分享，例如 #type=pet 或 #type=lucky&q=魅魔。
