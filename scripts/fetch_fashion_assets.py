#!/usr/bin/env python3
from __future__ import annotations
import json, re, sys, time
from pathlib import Path
from urllib.parse import quote, urljoin
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'assets_manifest.json'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131 Safari/537.36'

def get(url: str, timeout=40) -> tuple[bytes, str]:
    if 'cloudfront.net' in url:
        referer = 'https://mabinogimobile.nexon.com/'
    elif 'inven.co.kr' in url:
        referer = 'https://www.inven.co.kr/'
    elif 'dcinside.com' in url:
        referer = 'https://gall.dcinside.com/'
    else:
        referer = 'https://namu.moe/'
    req = Request(url, headers={
        'User-Agent': UA,
        'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Referer': referer,
    })
    with urlopen(req, timeout=timeout) as r:
        return r.read(), r.headers.get('Content-Type','')

def valid_image(data: bytes, content_type='') -> bool:
    if len(data) < 5000: return False
    sigs = (b'\x89PNG\r\n\x1a\n', b'\xff\xd8\xff', b'RIFF', b'GIF8')
    return content_type.startswith('image/') or any(data.startswith(x) for x in sigs)

def download_direct(url: str, dest: Path) -> bool:
    try:
        data, ct = get(url)
        if not valid_image(data, ct):
            print(f'  ! not an image: {url} ({ct}, {len(data)} bytes)')
            return False
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        print(f'  ✓ {dest.relative_to(ROOT)}  {len(data):,} bytes')
        return True
    except Exception as e:
        print(f'  ! {url}: {e}')
        return False

def resolve_namu_file(filename: str) -> list[str]:
    quoted = quote('파일:' + filename, safe='')
    candidates=[]
    for host in ('https://namu.moe/w/','https://m.namu.moe/w/','https://dark.namu.moe/w/'):
        page = host + quoted
        try:
            html, _ = get(page)
            s = html.decode('utf-8','ignore').replace('&amp;','&')
            # Full-res Namu image host URLs.
            candidates += re.findall(r'https://file\.namu\.moe/file/[0-9a-fA-F]+', s)
            # Some mirrors use relative file links or data-src.
            for m in re.findall(r'(?:src|data-src)=["\']([^"\']+)["\']', s):
                if 'file.namu.moe/file/' in m:
                    candidates.append(urljoin(page,m))
            if candidates: break
        except Exception as e:
            print(f'  ! Namu resolver {page}: {e}')
    # preserve order / unique
    return list(dict.fromkeys(candidates))

def main():
    manifest=json.loads(MANIFEST.read_text(encoding='utf-8'))
    failures=[]
    for item in manifest['assets']:
        dest=ROOT/item['path']
        if dest.exists() and dest.stat().st_size > 5000:
            print(f'✓ already exists: {item["path"]}')
            continue
        print(f'→ {item["name"]}')
        urls=list(item.get('urls',[]))
        if item.get('namu_filename'):
            urls += resolve_namu_file(item['namu_filename'])
        urls += item.get('fallbacks',[])
        ok=False
        for url in list(dict.fromkeys(urls)):
            if download_direct(url,dest):
                ok=True; break
            time.sleep(.5)
        if not ok:
            failures.append(item['name'])
    if failures:
        print('\nFailed:')
        for x in failures: print(' -',x)
        sys.exit(1)
    print('\nAll Abyss/Raid images are now stored locally under assets/.')

if __name__=='__main__': main()
