# 瑪奇 Mobile 韓服外觀圖鑑 — GitHub Pages 版

截至 2026-09-05 的網站資料包。

## 本版調整

- 已移除：`坐騎`
- 已移除：`活動免費衣服`
- 新增：`深淵副本時裝` 3 套
- 新增：`團隊副本時裝` 5 套
- 保留：通行證、幸運箱、寵物、全套套組

## 深淵副本時裝

1. 失落月景 / 로스트 문스케이프 — 2025-04-03
2. 惡魔暗影 / 데모닉 섀도 — 2025-10-02
3. 莫爾海盜 / 모르 코르세어 — 2026-07-02

## 團隊副本時裝

1. 咆哮之魂 / 포효하는 영혼 — 2025-04-24
2. 蝕影 / 이클립스 셰이드 — 2025-06-23
3. 奧秘金屬 / 아케인 메탈릭 — 2025-11-13
4. 奇異小丑 / 오드 클라운 — 2026-01-15
5. 卡拉格龍騎兵 / 카라그 드라군 — 2026-07-16

## GitHub Pages 使用方式

1. 將這個資料夾的所有檔案上傳到 Repository 根目錄。
2. 第一次 push 後，GitHub Actions 的 **「下載圖鑑圖片到 Repository」** 會執行 `scripts/fetch_fashion_assets.py`。
3. 8 張深淵／團隊副本時裝圖片會被下載到：
   - `assets/abyss/`
   - `assets/raid/`
4. Action 會自動將圖片 commit 回 Repository；`index.html` 之後固定讀取這些 Repository 內的相對路徑圖檔，而不是每次瀏覽時才向外站抓圖。
5. Repository → **Settings → Pages**，將部署來源設為你的主分支根目錄即可。

如果 GitHub Actions 因 Repository 權限未自動執行，可到 **Actions** 頁面手動執行一次「下載圖鑑圖片到 Repository」。

## 結構

```text
index.html
.nojekyll
assets_manifest.json
assets/
  abyss/
  raid/
scripts/
  fetch_fashion_assets.py
.github/
  workflows/
    fetch-assets.yml
```
