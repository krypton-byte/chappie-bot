import re, requests, random
def png(sc):
    return filter(lambda x:x if not "gstatic" in x and not "<" in x and not "(" in x else None ,re.findall("(https?://.*?.png)", sc))
def jpg(sc):
    return filter(lambda x:x if not "gstatic" in x and not "<" in x and not "(" in x else None ,re.findall("(https?://.*?.jpg)", sc))
def jpeg(sc):
    return filter(lambda x:x if not "gstatic" in x and not "<" in x and not "(" in x else None ,re.findall("(https?://.*?.jpeg)", sc))
def goimage(query)->dict:
    sc=requests.get("https://www.google.co.in/search", params={"q":query, "source":"lnms","tbm":"isch"}, headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}).text
    return {
        "jpg":list(jpg(sc)),
        "png":list(png(sc)),
        "jpeg":list(jpeg(sc)),
    }
    