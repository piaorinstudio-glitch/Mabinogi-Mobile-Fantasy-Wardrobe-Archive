# 瑪奇 Mobile 韓服外觀圖鑑 — GitHub image 資料夾版

- `index.html`：GitHub Pages 首頁
- `image/`：實體圖片資料夾
- 已從原本單檔 HTML 拆出 **61 張**實體圖片。
- 另有 **26 張**原本直接引用韓服 CDN／資料來源的圖片，`index.html` 已改成預定讀取 `image/` 本地路徑。
- 第一次 push 到 GitHub 後，`.github/workflows/fetch-images.yml` 會下載這些圖片並 commit 回 `image/`。
- 若要在 Windows 上先抓完，可在解壓後執行 `下載剩餘網路圖片.ps1`。

> 這版不再使用 `assets/abyss` / `assets/raid` 作為網頁主要圖片目錄；統一用 `image/`。
