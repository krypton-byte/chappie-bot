import requests, re
from urllib.parse import unquote

def fbvid(url: str):
    try:
        req=requests.get(re.sub("(/mobile.|/www.|/m.)","/mbasic.",url))
        if req.status_code == 200 :
            if re.search("\<a href\=\"/video_redirect/\?src\=(.*?)\"",req.text):
                return {"status":True,"url":unquote(re.search("\<a href\=\"/video_redirect/\?src\=(.*?)\"",req.text)[1])}
            else:
                return {"status":False,"msg":"private_video"}
        else:
            return {"status":False,"msg":"Link Wrong"}
    except:
        return {"status":False,"msg":"Link Tidak Valid"}
