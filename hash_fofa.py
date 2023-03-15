import requests
import io
import hashlib
import base64
import mmh3
from typing import Union, Tuple

def get_hash(content):
    def mmh3_hash32(raw_bytes, is_uint32=True):
        h32 = mmh3.hash(raw_bytes)
        
        if is_uint32:
            return str(h32 & 0xffffffff)
        else:
            return str(h32)

    def stand_base64(braw) -> bytes:
        bckd = base64.standard_b64encode(braw)
        buffer = bytearray()
        for i, ch in enumerate(bckd):
            buffer.append(ch)
            if (i+1) % 76 == 0:
                buffer.append(ord('\n'))
        buffer.append(ord('\n'))
        return bytes(buffer)
    
    return mmh3_hash32(stand_base64(content))


def get_ico_hash_from_url(url):
    headers  = {
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.5006.400 QQBrowser/9.7.13114.400",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
    }
    content = requests.get(url,headers=headers,timeout=2).content
    return get_hash(content)

def get_ico_hash_from_file(filename):
    with open(filename,"rb") as f:
        content = f.read()
        return get_hash(content)
    

if __name__ == "__main__":
    import sys
    target = sys.argv[1]
    if "http" in target:
        print(get_ico_hash_from_url(target))
    else:
        print(get_ico_hash_from_file(target))
