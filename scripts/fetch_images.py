#!/usr/bin/env python3
from __future__ import annotations
import json,re,time,sys
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.parse import quote,urljoin
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'image_manifest.json'
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131 Safari/537.36'

def get(url,timeout=45):
    if 'cloudfront.net' in url: ref='https://mabinogimobile.nexon.com/'
    elif 'inven.co.kr' in url: ref='https://www.inven.co.kr/'
    elif 'dcinside.com' in url: ref='https://gall.dcinside.com/'
    else: ref='https://namu.moe/'
    req=Request(url,headers={'User-Agent':UA,'Accept':'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8','Referer':ref})
    with urlopen(req,timeout=timeout) as r: return r.read(),r.headers.get('Content-Type','')

def valid(data,ct=''):
    return len(data)>3000 and (ct.startswith('image/') or data.startswith((b'\x89PNG\r\n\x1a\n',b'\xff\xd8\xff',b'RIFF',b'GIF8')))

def resolve_namu(filename):
    out=[]; q=quote('파일:'+filename,safe='')
    for host in ('https://namu.moe/w/','https://m.namu.moe/w/','https://dark.namu.moe/w/'):
        try:
            raw,_=get(host+q); txt=raw.decode('utf-8','ignore').replace('&amp;','&')
            out += re.findall(r'https://file\.namu\.moe/file/[0-9a-fA-F]+',txt)
            if out: break
        except Exception: pass
    return list(dict.fromkeys(out))

def main():
    assets=json.loads(MANIFEST.read_text(encoding='utf-8'))['assets']; failed=[]
    for x in assets:
        dest=ROOT/x['path']; dest.parent.mkdir(parents=True,exist_ok=True)
        if dest.exists() and dest.stat().st_size>3000:
            print('✓',x['path']); continue
        urls=list(x.get('urls',[]))
        if x.get('namu_filename'): urls += resolve_namu(x['namu_filename'])
        ok=False
        for u in dict.fromkeys(urls):
            try:
                d,ct=get(u)
                if valid(d,ct): dest.write_bytes(d); print('✓',x['path'],len(d)); ok=True; break
            except Exception as e: print('!',x['name'],u,e)
            time.sleep(.4)
        if not ok: failed.append(x['name'])
    if failed:
        print('\n下載失敗：'); [print(' -',x) for x in failed]; sys.exit(1)
    print('\n全部網路圖片已下載到 image/。')
if __name__=='__main__': main()
