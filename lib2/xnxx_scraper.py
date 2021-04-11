import requests
import re, math
def convert_size(size_bytes):
    '''
    size_bytes : String
    '''
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])
def scrapX(url: str):
    try:
        http = requests.get(url)
        size=int(requests.get(re.search("setVideoUrlLow\(\'(.*?)\'\)",http.text)[1], stream=True).headers["Content-Length"])
        if size > 15728640:
            return {"msg":"max"}
        else:
            return {"judul" : re.search("setVideoTitle\(\'(.*?)\'",http.text)[1],
            "thumb": re.search("setThumbUrl\(\'(.*?)\'",http.text)[1],
            "desc" : re.search("desc\":\"(.*?)\"",http.text)[1] if re.search("desc\":\"(.*?)\"",http.text) else "",
            "size":convert_size(size),
            "vid" : re.search("setVideoUrlLow\(\'(.*?)\'\)",http.text)[1]}
    except Exception:
        return {}
