這是不用 Actions 的直接覆蓋修正版。

修正內容：
- 深淵副本時裝圖片改讀 image/abyss-1.png、image/abyss-2.png、image/abyss-3.png
- 團隊副本時裝圖片改讀 image/raid-1.png、image/raid-2.jpg、image/raid-3.png、image/raid-4.png、image/raid-5.png
- 也同步把通行證、幸運箱、套組、寵物路徑改回 image/ 資料夾
- 如果圖片檔名不一致，卡片會顯示「圖片檔案未上傳或檔名不一致」

使用方式：
1. 上傳 index.html 到 GitHub repo 根目錄，覆蓋原本 index.html。
2. Commit changes。
3. 等 pages-build-deployment 綠勾。
4. 網站 Ctrl + F5。

如果深淵/團隊仍然看不到，請檢查 GitHub 的 image 資料夾是否真的有：
image/abyss-1.png
image/abyss-2.png
image/abyss-3.png
image/raid-1.png
image/raid-2.jpg
image/raid-3.png
image/raid-4.png
image/raid-5.png
