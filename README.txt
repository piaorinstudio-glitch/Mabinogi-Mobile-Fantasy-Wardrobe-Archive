這包會把網站 UI 改成參考圖那種「手帳拼貼 / 紙張 / 便利貼」排版。

使用方式：
1. 解壓縮。
2. 把 .github 和 scripts 兩個資料夾上傳到 GitHub repo 根目錄並覆蓋。
3. 到 Actions → 套用最終拼貼版 UI → Run workflow。
4. 等 workflow 綠勾，再等 pages-build-deployment 綠勾。
5. 網站 Ctrl + F5 強制刷新。

這版主要修改：
- 大型紙張 Hero 區
- 彩色貼紙分類按鈕
- 標題、搜尋、排序、預測按鈕分層
- 4 欄 Polaroid 卡片網格
- 手機版改成橫向分類列 + 單欄卡片
