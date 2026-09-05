這包是修正「首頁圖片沒有上去、排版跑掉」用的最終補丁。

一定要上傳這三個資料夾：
- .github/
- scripts/
- image/

使用方式：
1. 解壓縮 ZIP。
2. 把 .github、scripts、image 三個資料夾拖進 GitHub repo 根目錄上傳。
3. Commit changes。
4. 到 Actions，執行「套用首頁圖片與最終排版」。
5. 等 workflow 綠勾，再等 pages-build-deployment 綠勾。
6. 回網站 Ctrl + F5。

修正內容：
- 首頁上方會放入你給的營火合照與三人合照。
- 主標改成兩行：瑪奇Mobile / 韓服外觀圖鑑。
- 移除 Stories in Erinn、Fantasy Wardrobe Archive、在艾琳...等裝飾文字。
- 分類按鈕移除 icon。
- 搜尋、排序、筆數重新排整齊。
- 寵物頁有 全部 / 常駐 / 限定 / 聯動 篩選，且保留顏色。
- 卡片右側顯示期數框，下半部空白縮小。
