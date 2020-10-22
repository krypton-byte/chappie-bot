import requests, re

def fbvid(url):
    req=requests.get(url)
    if req.status_code == 200:
        try:
            return {"status":True,"url":re.search('hd_src:"(.+?)"', req.text)[1]}
        except TypeError:
            return {"status":False,"msg":"private_video"}
    else:
        return {"status":False,"msg":"Link Wrong"}
