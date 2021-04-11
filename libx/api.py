import requests, json, psutil, platform
import sys, base64
from urllib.parse import quote
from bs4 import BeautifulSoup
from io import StringIO
import contextlib
from moviepy import editor
import convertapi
import math
from youtube_dl import YoutubeDL
import re
init=YoutubeDL({})
def CCGenrate(cc: str):
    position=[]
    for i in re.compile("x").finditer(cc):
        position.append(i.span()[0])
    for i in range(10**(len(position))-1):
        op='0'*(len(position)-len(str(i)))+str(i)
        lst=list(cc)
        for xi in enumerate(position):
            lst[xi[1]] = op[xi[0]]
        yield "".join(lst)
def hundred_to_k(v):
    size_name=[" ","K","M","G","T","P","E","Z","Y"]
    i = int(math.floor(math.log(v, 1000)))
    p = math.pow(1000, i)
    s = round(v / p, 2)
    return "%s %s" % (s, size_name[i])
def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])
def system_info():
    Msg=f"""
*Network:*"""
    for i in enumerate(psutil.net_if_addrs().get("docker0") if psutil.net_if_addrs().get("docker0") else []):
        Msg+=f"""
    *Docker {i[0]}:*
        - Family : {i[1].family.__str__()}
        - Alamat : {i[1].address}
        - Netmask: {i[1].netmask}
        - Broadcast: {i[1].broadcast}
        - PTP : {i[1].ptp }"""
    for i in enumerate(psutil.net_if_addrs().get("lo") if psutil.net_if_addrs().get("lo") else []):
        Msg+=  f"""
    *Localhost {i[0]}:*
        - Family : {i[1].family.__str__()}
        - Alamat : {i[1].address}
        - Netmask: {i[1].address.__str__()}
        - Broadcast: {i[1].broadcast}
        - PTP : {i[1].ptp}"""
    Msg+=f"""
*CPU:*
    - Inti  : {psutil.cpu_count()}
    - Sekarang: {psutil.cpu_freq().current} 
    - Minimal : {psutil.cpu_freq().min}
    - Maksimal: {psutil.cpu_freq().max}
*VMemory:* 
    - Total : {convert_size(psutil.virtual_memory().total)}
    - Persentase : {psutil.virtual_memory().percent} %
    - Terpakai :  {convert_size(psutil.virtual_memory().used)}
    - Active   : {convert_size(psutil.virtual_memory().active)}
    - Inactive : {convert_size(psutil.virtual_memory().inactive)}
    - Bebas    : {convert_size(psutil.virtual_memory().free)}
    - Tersedia : {convert_size(psutil.virtual_memory().available)}
    - Cache    : {convert_size(psutil.virtual_memory().cached)}
    - Buffers  : {convert_size(psutil.virtual_memory().buffers)}
    - Shared   : {convert_size(psutil.virtual_memory().shared)}
    - Slab     : {convert_size(psutil.virtual_memory().slab)}
*SMemory:*
    - Total : {convert_size(psutil.swap_memory().total)}
    - Terpakai: {convert_size(psutil.swap_memory().used)}
    - Bebas : {convert_size(psutil.swap_memory().used)}
*Uname:*
    - System : {platform.uname().system}
    - Node   : {platform.uname().node}
    - release: {platform.uname().release}
    - Version: {platform.uname().version}
    - Machne : {platform.uname().machine}
    - Processor: {platform.uname().processor}
    - Architecture: {', '.join(platform.architecture())}
    - Machine: {platform.machine()}"""
    return Msg.strip()
def imgUploader(base64_):
    f=requests.post("https://api.imgbb.com/1/upload?&key=0c796ce6298f7c15296df06db9fcff86", data={"image":base64_})
    if f.status_code == 200:
        return {"msg":'Image : %s\nSize  : %s\nDelete: %s'%(f.json()["data"]["url"], convert_size(f.json()["data"]["size"]), f.json()["data"]["delete_url"]),"url":f.json()["data"]["url"]}
    else:
        return "Upload Gambar Gagal"
def searchWithImage(url):
    me=BeautifulSoup(requests.get("https://www.google.com/searchbyimage",params={"site":"search","sa":"X","image_url":url},headers={'user-agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4183.102 Safari/537.36"}).text, "html.parser")
    return me.find_all("input",attrs={"type":"text"})[0]["value"]
def shortLink(url):
    '''
    input YouTube Url
    url : String
    '''
    hasil=requests.get('https://v.gd/create.php',params={'format':'simple','url':url})
    if 'error' in hasil.text.lower():
        return "gagal"
    else:
        return hasil.text
@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old
"""def doujin(nuklir,driver,chat_id, Msg):
    '''
    nuklir  : String
    driver  : Object
    chat_id : String
    Msg     : Object
    '''
    dujin = json.loads(requests.get('https://doujin2pdf.herokuapp.com/doujinshi/%s'%(nuklir), timeout=10000).text)
    if dujin['status']:
        open('cache/cover.jpg','wb').write(requests.get('https://doujin2pdf.herokuapp.com%s'%dujin['cover']).content)
        driver.send_media('cache/cover.jpg',chat_id,'')
        Msg.reply_message('title : %s 🔞\n%s\n🔗 https://doujin2pdf.herokuapp.com%s'%(dujin['title'], dujin['tags'], dujin['content']))
    else:
        Msg.reply_message('kode Nuklir Salah')"""
def yt2mp4(url: str):
    try:
        parser=init.extract_info(url, download=False)
        for i in parser["formats"]:
            if i.get("format_note") == '360p' and i.get("ext") =='mp4' and not i.get("acodec") == 'none' and i.get("filesize"):
                if i.get("filesize") > 20971520:
                    return {"status":"Large"}
                else:
                    return {"status":True,"size":convert_size(i.get("filesize")),"result":i.get("url"),"title":parser["title"],"view":hundred_to_k(parser["view_count"]), "thumb":parser["thumbnails"][-1].get("url")}
        for i in parser["formats"]:
            if i.get("format_note") == '360p' and i.get("acodec") == 'none':
                if i.get("filesize") > 20971520:
                    return {"status":"Large"}
                vid=editor.VideoFileClip(i.get("url"))
                aud=Yt2Mp3(url=url)
                if aud["status"] == "Large":
                    return {"status":"Large"}
                vid.audio = editor.AudioFileClip(aud["url"])
                return {"status":True,"object":True,"size":"Tidak Diketahui","result":vid,"title":parser["title"],"view":hundred_to_k(parser["view_count"]), "thumb":parser["thumbnails"][-1].get("url")}
        else:
            return {"status":False}
    except Exception as e:
        print(f"Error -> {e}")
        return {"status":False}
def Yt2Mp3(query=None, url=None):
    try:
        if query:
            yt = init.extract_info(f"ytsearch:{query}", download=False)["entries"][0]
        elif url:
            yt = init.extract_info(url, download=False)
        else:
            return False
        audio=list(filter(lambda x:x["acodec"] and x["vcodec"] == "none" , yt["formats"]))
        i =list(filter(lambda am:am["filesize"]==max(map(lambda x:x["filesize"], audio)), audio))[0] #best audio
        print(len(i))
        url = i["url"]
        ret='*Judul* : %s\n*Dilihat* : %s\n*Ukuran* : %s'%(yt.get("title"), hundred_to_k(yt.get("view_count")), convert_size(i["filesize"]))
        if i["filesize"] > 20971520: #max 20mb
            return {"status":"Large"}
        return {"status":True,"info":ret,"url":url,"thumb":yt.get("thumbnail"),"judul":yt.get("title")}
    except Exception as e:
        print(e)
        return {"status":"Tidak Di Temukan"}
def bacot(chat):
    pesan=[]
    for i in chat:
        if i.lower() in ['a','u','e','o']:
            if i.isupper():
                pesan.append('I')
            elif i.islower():
                pesan.append('i')
            else:
                pesan.append(i)
        else:
            pesan.append(i)
    return ''.join (pesan)
def waifu():
    f=BeautifulSoup(requests.get('http://randomwaifu.altervista.org/').text,'html.parser')
    return {
        'title':f.p.text,
        'image':'http://randomwaifu.altervista.org/%s'%(f.img['src'])
    }



def WhatAnimeIsThis(fn):
    '''
    fn : String (Filename)
    '''
    dat=base64.b64encode(open(fn,"rb").read()).decode()
    reGet=requests.post("https://trace.moe/api/search",data={'image':dat})
    if reGet.status_code == 200:
        anilist_id=reGet.json()["docs"][0]["anilist_id"]
        filename=quote(reGet.json()["docs"][0]["filename"])
        at=reGet.json()["docs"][0]["at"]
        tokenthumb=reGet.json()["docs"][0]["tokenthumb"]
        video=requests.get("https://media.trace.moe/video/%s/%s?t=%s&token=%s"%(anilist_id, quote(filename), at, tokenthumb))
        return {
'status':True,
'hasil':'''
*Anime*   : %s
*Season*  : %s
*Episode* : %s
'''%(reGet.json()["docs"][0]["anime"],reGet.json()["docs"][0]["season"],reGet.json()["docs"][0]["episode"]),
'video':video
}
    else:
        return {
            'status':False
        }
