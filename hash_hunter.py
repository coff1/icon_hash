import requests
import io
import hashlib
class R:
    res = list()


def get_hash(data):
    return hashlib.md5(data).hexdigest()

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
    data = requests.get(f"{url}/favicon.ico",headers=headers,timeout=2).content
    return get_hash(data)

def get_ico_hash_from_file(file_name):
    with open(file_name,"rb") as f:
        data = f.read()
        return(get_hash(data))


if __name__  == "__main__" :
    import sys
    target = sys.argv[1]
    if "http" in target:
        print(get_ico_hash_from_url(target))
    else:
        print(get_ico_hash_from_file(target))

