from logging import error
import requests, json, random
import sys, base64
from urllib.parse import quote, unquote
from bs4 import BeautifulSoup
from io import StringIO
import contextlib
from moviepy import editor
import convertapi
import math
from . import pytube
#import pytube
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
def imgUploader(base64_):
    '''
    base64_ : String base64.encode
    '''
    f=requests.post("https://api.imgbb.com/1/upload?key=0c796ce6298f7c15296df06db9fcff86", data={"image":base64_})
    if f.status_code == 200:
        return 'Image : %s\nSize  : %s\nDelete: %s'%(f.json()["data"]["url"], convert_size(f.json()["data"]["size"]), f.json()["data"]["delete_url"])
    else:
        return "Upload Gambar Gagal"
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
def YtVidDownload(url):
    '''
    input YouTube Url
    url : String
    '''
    try:
        hasil=pytube.YouTube(url)
        ret='Judul : %s\nDilihat : %s\nDeskripsi :\n    %s\n\n\n\nDownload : \n'%(hasil.title, hasil.views, hasil.description)
        for i in hasil.streams:
            if i.mime_type == 'video/mp4' and i.resolution:
                ret+='    %s : %s\n'%(i.resolution, shortLink(i.url))
        return ret
    except Exception:
        return "Link Error"
def url2png(url):
    '''
    Input Url website
    url : String
    '''
    convertapi.api_secret = 'Z7Z4HpVF3n7e9I8H'
    x=convertapi.convert('png', {
    'Url': url
    }, from_format = 'web')
    return x.response['Files'][0]['Url']

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old
def doujin(nuklir,driver,chat_id, Msg):
    '''
    nuklir  : String
    driver  : Object
    chat_id : String
    Msg     : Object
    '''
    dujin = json.loads(requests.get('https://terkejoed.herokuapp.com/doujinshi/%s'%(nuklir), timeout=10000).text)
    if dujin['status']:
        open('cache/cover.jpg','wb').write(requests.get('https://terkejoed.herokuapp.com%s'%dujin['cover']).content)
        driver.send_media('cache/cover.jpg',chat_id,'title : %s 🔞\n%s\n🔗 https://terkejoed.herokuapp.com%s'%(dujin['title'], dujin['tags'], dujin['content']))
    else:
        Msg.reply_message('kode Nuklir Salah')
def yt2mp3(urlyt):
    '''
    input YouTube Url
    url : String
    '''
    try:
        hasilObj=pytube.YouTube(urlyt)
        url=''
        size=0
        ret='judul : %s\nDilihat : %s'%(hasilObj.title, hasilObj.views)
        for i in hasilObj.streams:
            if i.type == "audio" and i.abr == "160kbps":
                url=i.url
                size=i.filesize
        if size > 20971520: #max 20mb
            return {"status":"Large"}
        return {"status":True,"info":ret,"url":url,"thumb":hasilObj.thumbnail_url,"judul":hasilObj.title}
    except pytube.exceptions.RegexMatchError:
        return {"status":"url"}
    except KeyError:
        return {"status":"ulang"}
def bacot(chat):
    '''
    chat : String
    '''
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

class Merger:
    def __init__(self, url, num=None):
        self.url = url
        self.num = num
    def parser(self):
        try:
            YT=pytube.YouTube(self.url)
            pesan="Judul : %s\n"%YT.title
            for i in enumerate(YT.streams):
                if i[1].type == "video":
                    pesan+="%s. Res: %s Fps: %s\n"%(i[0],i[1].resolution, i[1].fps)
            return {"status":True,"result":pesan}
        except pytube.exceptions.RegexMatchError:
            return {"status":"url"}
        except KeyError:
            return {"status":"ulang"}
    def ytmp3(self):
        YT=pytube.YouTube(self.url)
        for i in YT.streams:
            if i.type == "audio":
                audio=i
        aud=editor.AudioFileClip(audio.url)
        return aud
    def down(self):
        try:
            YT=pytube.YouTube(self.url)
            if len(YT.streams) > self.num:
                if YT.streams[self.num].filesize > 20971520: #max 20 mencegah limit
                    return {"status":"L"}
                else:
                    vid=editor.VideoFileClip(YT.streams[self.num].url)
                    if vid.audio:
                        vid.audio = vid.audio
                    else:
                        while True:
                            aud=yt2mp3(self.url)
                            print(aud)
                            if aud["status"] == True:
                                vid.audio = editor.AudioFileClip(aud["url"])
                                break
                    return {"status":True,"result":vid}
            else:
                return {"status":False}
        except pytube.exceptions.RegexMatchError:
            return {"status":"url"}
        except KeyError:
            return {"status":"ulang"}


def WhatAnimeIsThis(fn):
    '''
    fn : String (Filename)
    '''
    dat=base64.b64encode(open(fn,"rb").read()).decode()
    reGet=requests.post("https://trace.moe/api/search",data={'image':dat})
    if reGet.status_code == 200:
        anime0=reGet.json()["docs"][0]
        anilist_id=reGet.json()["docs"][0]["anilist_id"]
        filename=quote(reGet.json()["docs"][0]["filename"])
        at=reGet.json()["docs"][0]["at"]
        tokenthumb=reGet.json()["docs"][0]["tokenthumb"]
        video=requests.get("https://media.trace.moe/video/%s/%s?t=%s&token=%s"%(anime0["anilist_id"], quote(anime0["filename"]), anime0["at"], anime0["tokenthumb"]))
        return {
'status':True,
'hasil':'''
Anime   : %s
Season  : %s
Episode : %s
'''%(reGet.json()["docs"][0]["anime"],reGet.json()["docs"][0]["season"],reGet.json()["docs"][0]["episode"]),
'video':video
}
    else:
        return {
            'status':False
        }
