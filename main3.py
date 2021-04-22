#!/usr/bin/python
"""
 @AUTHOR : KRYPTON-BYTE
 @DATE   : TUE OCT 13, 2020

" Wahai Orang-orang Yg Beriman Mengapakah Kamu Mengatakan Sesuatu Yg Tidak Kamu Kerjakan? Amat Besar Kebencian Di Sisi Allah Bahwa Kamu Mengatakan Apa-apa Yang Tidak Kmau Kerjakan." (QS asg-shaff: 2-3)
"""

import difflib
from openwa.helper import convert_to_base64
from openwa import WhatsAPIDriver
from moviepy import editor
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TIT2
import locale
import  time
from concurrent.futures import ThreadPoolExecutor
locale.setlocale(locale.LC_ALL, 'C')
from googletrans import Translator
import  base64, os, pickle, hashlib,datetime, wikipedia, re,secrets , pyqrcode, hashlib, json, requests, random, subprocess, asyncio
from gtts import gTTS
import tesserocr
from PIL import Image
from pyzbar.pyzbar import decode
from ast import literal_eval
from gtts import gTTS
from io import BytesIO
import threading, math, psutil
#------------Module--------------#
#----------------
from lib2 import desain, EditR, cordIndo, QuoteTrans, scrapX, pinterest, findSurah, detect, SpeechToText, spam, tiktok, vidPinDownload, ListLang, langExecute, url2png, img2ascii, goimage, twettdownload, pitch, setDriver, setCountDown, parser_nuklir, nsearch, tiktok2
from lib2 import stickerSave, getListSticker, getSticker, deleteSticker, downloadDrive, get_AntiToxic, get_nsfw, get_prefix, set_AntiToxic, set_prefix, set_nsfw, stickerExif, get_male, get_female, isUsers, set_user, driver_, broadcast_serv, t_sticker, eight_bit, instagram_filter, alay, morse, blackpink, orange, Convert, paste_transparant_layer
from libx import *
from data import update_toxic, resert_toxic
from setting import author,  BotName, proxy, MenuList, prefix
from javascript.pitnah import FakeReply, hidetag
from flask import Flask, render_template
import socketio, eventlet
#-----------setting----------------------#
wikipedia.set_lang('id')
TempSelf    = []
tra         = Translator()
mutiara     = json.loads(open("assets/mutiara.json").read())
stop        = 0
running     = []
afk         = {}
starttime   = time.time()
Kasar       = open("assets/badword.txt","r").read().splitlines()
FullCommand = ["notoxic","dadu","wasted","iphone","simi","grup","cmd","refresh","morse","attp","alay","blackpink","fdeface","countdown","ifilter","8bit","nsearchs","nsearch","afk","sticker2","sclear","tele_sticker","runtime","gf","bf","cimage","pitnah","other_bots","check","reg","set_prefix","twitter_download","pitch","cari_gambar","pyexec","toimg","hidetag","img2ascii","play","save_sticker", "get_sticker", "delete_sticker", "list_sticker","tstiker","tp","status","tiktok","tiktok2","kquote","execute","pintdown","join","transcript","whoisthis","whatimage","set","ping","quran","yt2mp4","pembersihan","pinterest","sendmessage","xnx2mp4","author","nsfw","gif","menu","help","chord","igstalk","report","replyreport","sticker","stiker","fb","quote1","kusonime","otakudesu","delete","upimg","ig","cari","support","tulis","waifu","qrmaker","gambar","intro","kitsune","qrreader","?","wait","url2png","run","ocr","doujin","film","ts","cc","tts","quotemaker","yt2mp3","yt","wiki","list-admin","admin","unadmin","kick","add","owner","linkgroup","revoke","dog","mentionall","neko","quote","gambar","bc","joke","bct", "ph"]
global driver
driver     = WhatsAPIDriver(client='Chrome', headless=True, loadstyles=False ,chrome_options=["--no-sandbox",'--disable-dev-shm-usage'])
#kpatch = krypton_patch(driver)
driver_(driver)
setDriver(driver)
isAdmin    = lambda _:driver.wapi_functions.getMe()["wid"] in driver.wapi_functions.getGroupAdmins(_)
class GetRepMedia:
    def __init__(self, js):
        self.obj = js._js_obj["quotedMsg"]
        self.client_url = self.obj.get('deprecatedMms3Url')
        self.media_key = self.obj.get("mediaKey")
        self.type = self.obj.get("type")
        self.crypt_keys= {'document': '576861747341707020446f63756d656e74204b657973','image': '576861747341707020496d616765204b657973','video': '576861747341707020566964656f204b657973','ptt': '576861747341707020417564696f204b657973','audio': '576861747341707020417564696f204b657973','sticker': '576861747341707020496d616765204b657973'}
def main(TextObject):
    global afk
    try:
        if (af:=set(TextObject.get_js_obj()["mentionedJidList"])):
            for i in list(set(afk.keys()) & af):
                TextObject.reply_message(f"{i[:-5]} Sedang Afk\nReason : {afk[i]}")
        if afk.pop(TextObject.sender.id, None):
            TextObject.reply_message(f"Wellcome Back {TextObject.sender.id[:-5]}")
        if TextObject.type == 'chat':
            if set(TextObject.content.lower().split())&set(Kasar):
                if '@g.us' in TextObject.chat_id:
                    if (value:=get_AntiToxic(TextObject.chat_id)):
                        if (melanggar:=update_toxic(TextObject.chat_id, TextObject.sender.id, value)) == "kick":
                            driver.wapi_functions.sendMessage(TextObject.chat_id,"Terpaksa Saya Mengkick Anda Karna Anda Melanggar Peraturan")
                            driver.remove_participant_group(TextObject.chat_id,TextObject.sender.id)
                        else:
                            driver.wapi_functions.sendMessage(TextObject.chat_id,f"Saya Telah Memperingati Anda Sebanyak : {melanggar}")
            if driver.wapi_functions.getMe()["wid"] in TextObject.get_js_obj()["mentionedJidList"]:
                TextObject.reply_message("Ketik *!help* Untuk Menampilkan Menu")
            if TextObject.content[len(prefix):].split()[0] in FullCommand and TextObject.content[:len(prefix)] == prefix:
                replyCommand(TextObject)
                #executor.submit(replyCommand, (TextObject),(chatObject.chat))
            elif '@c.us' in TextObject.chat_id:
                TextObject.reply_message(chatbot(TextObject.content))
            elif (not TextObject.content[len(prefix):].split()[0] in FullCommand ) and TextObject.content[:len(prefix)] == prefix:
                if (pil:=difflib.get_close_matches(TextObject.content[len(prefix):].split()[0], FullCommand, n=1)):
                    TextObject.reply_message(f"Mungkin Yg Anda Maksud Adalah *{prefix}{pil[0]}*")
        elif TextObject.type == 'image' and TextObject.caption[0][:len(prefix)] == prefix:
            recImageReplyCommand(TextObject)
            #executor.submit(recImageReplyCommand, (TextObject),(chatObject.chat))
        elif TextObject.type == "video" and TextObject.caption[0][:len(prefix)] == prefix:
            videoHandlr(TextObject)
            #executor.submit(videoHandlr,(TextObject))
        elif TextObject.type == 'vcard':
            if isAdmin(TextObject.chat_id):
                member=driver.wapi_functions.getGroupParticipantIDs(TextObject.chat_id)
                masuk='---------➤SELAMAT DATANG \n'
                for i in TextObject.contacts:
                    for u in re.findall('waid\=(.*?):',i.decode()):
                        try:
                            if u in member:
                                True
                            else:
                                driver.add_participant_group(TextObject.chat_id,'%s@c.us'%(u))
                                masuk+='➤ @%s'%(u)
                        except Exception as e:
                            print(f"Error -> {str(e)}")
                            True
            else:
                driver.wapi_functions.sendMessageWithMentions(TextObject.chat_id,masuk,'')
    except Exception as e:#selenium.common.exceptions.InvalidSessionIdException:
        print(f"Error -> {str(e)}")
        pass    
def recImageReplyCommand(Msg):
    caption = Msg.caption[len(prefix):]
    args=caption.split()[1:]
    ran=secrets.token_hex(7)
    if Msg.caption:
        kpt = caption.lower().split()[0]
        if kpt == "wait":
            fn=Msg.save_media('./cache',Msg.media_key)
            res=WhatAnimeIsThis(fn)
            if res["status"]:
                driver.wapi_functions.sendImage(convert_to_base64(BytesIO(res["video"].content)), Msg.chat_id, "wait.mp4")
                Msg.reply_message(res["hasil"])
            else:
                Msg.reply_message("Gagal di cari")
            os.remove(fn)
        elif kpt == "wasted":
            fn=Msg.save_media('./cache',Msg.media_key)
            paste_transparant_layer(Image.open(fn)).save(fn)
            driver.send_media(fn, Msg.chat_id, "sukses")
            os.remove(fn)
        elif kpt == "ifilter":
            fn=Msg.save_media('./cache',Msg.media_key)
            if args:
                tp=instagram_filter(fn, args[0])
                if isinstance(tp, str):
                    Msg.reply_message(tp)
                else:
                    Image.open(tp).save(f"cache/{ran}.png")
                    driver.send_media(f"cache/{ran}.png", Msg.chat_id, f"*Filter* : {args[0]}")
                    #driver.wapi_functions(convert_to_base64(tp), Msg.chat_id, "ig.png", f"Filter: {args[0]}")
            else:
                Msg.reply_message("Masukan Nama Filter")
        elif kpt =="reg": #!reg name|age|gender|bio
            capt=caption[len(kpt)+1:].split('|')
            fn=Msg.save_media('./cache',Msg.media_key)
            if ((nama:=capt[0]) and (umur:=capt[1]).isnumeric() and (gender:= capt[2] if capt[2] in ["male","female"] else None) and (bio:=capt[3])):
                set_user(nama=nama, umur=umur, gender=capt[2], bio=bio, profile=imgUploader(base64.b64encode(open(fn,"rb").read())).get("url"), chat_id=Msg.sender.id[:-5], from_bot=driver.wapi_functions.getMe()["wid"], from_id=Msg.chat_id)
            else:
                Msg.reply_message(f"*e.g:*\n  {prefix}reg name|age|gender[male|female]|bio")
        elif kpt == "whatimage":
            fn=Msg.save_media('./cache',Msg.media_key)
            Msg.reply_message(searchWithImage(imgUploader(base64.b64encode(open(fn,"rb").read())).get("url")))
            os.remove(fn)
        elif kpt == "whoisthis":
            fn=Msg.save_media('./cache',Msg.media_key)
            res=imgUploader(base64.b64encode(open(fn,"rb").read()).decode()).get("url")
            if res:
                Msg.reply_message(detect(res))
            else:
                Msg.reply_message("Gagal Mengindetifikasi Gambar")
        elif kpt == "quote1":
            arg=caption[7:].split('|')
            for i in range(arg.count('')):
                arg.remove('')
            if len(arg) == 3:
                color = (0, 0, 0) if arg[2] == "1" else (255, 255, 255)
                fn=Msg.save_media("./cache",Msg.media_key)
                desain(fn, katakata=arg[0], author=arg[1], col=color)
                driver.send_media(fn, Msg.chat_id, "Quote Berhasil Di Buat")
                os.remove(fn)
        elif kpt in ['stiker','sticker']:
            try:
                fn=Msg.save_media('./cache',Msg.media_key)
                os.rename(fn,"cache/%s.png"%ran)
                pasteLayer("cache/%s.png"%ran, packname= caption[len(kpt)+1:] if args else driver.wapi_functions.getMe().get('pushname'))
                driver.wapi_functions.sendImageAsSticker(convert_to_base64("cache/%s.png.webp"%ran)[23:],Msg.chat_id,{})
                os.remove("cache/%s.png"%ran)
            except Exception as e:
                print(f"Error -> {str(e)}")
                False
        elif kpt == "upimg":
            fn=Msg.save_media("./cache", Msg.media_key)
            Msg.reply_message(imgUploader(base64.b64encode(open(fn,"rb").read()).decode())["msg"])
        elif kpt == 'qrreader':
            img=decode(Image.open(Msg.save_media('./cache',Msg.media_key)))
            Msg.reply_message('Text : %s\nType : %s'%(img[0][0].decode(), img[0][1])) if img else Msg.reply_message('Gambar Tidak Valid')
        elif kpt == "ocr":
            fn=Msg.save_media("./cache", Msg.media_key)
            Msg.reply_message(tesserocr.file_to_text(fn, lang="eng+ind+jap+chi").strip())
            os.remove(fn)
        elif kpt == "return":
            Msg.reply_message(json.dumps(Msg._js_obj, indent=4))
def videoHandlr(Msg):
    caption = Msg.caption[len(prefix):]
    if caption.lower().split()[0] == "gif":
        ran=Msg.save_media('./cache',Msg.media_key).split('/')[-1][:-4]
        try:
            mv=editor.VideoFileClip("cache/%s.mp4"%ran)
            if int(mv.duration) <= 10:
                if mv.size[0] < 512 or mv.size[1] < 512:
                        pattern=patternRes(mv.size[0], mv.size[1])
                        sticker=mv.resize(width=pattern[0], height=pattern[1])
                        sticker.write_videofile(f"{ran}.mp4")
                os.system(f"""ffmpeg -i cache/{ran}.mp4 -y -vcodec libwebp -filter_complex "scale='min(512,512)':min'(512,512)':force_original_aspect_ratio=decrease,fps=15, pad=512:512:-1:-1:color=white@0.0,split[a][b];[a]palettegen=reserve_transparent=on:transparency_color=ffffff[p];[b][p]paletteuse" -f webp {ran}.webp""") #pasteLayer("cache/%s.png"%ran,packname="".join(filter(lambda ch:ord(ch)<256,)))
                open(f"cache/{ran}.exif","wb").write(stickerExif(packname="".join(filter(lambda ch:ord(ch)<256,caption[len(caption.lower().split()[0])+1:] if caption[len(caption.lower().split()[0])+1:] else driver.wapi_functions.getMe().get('pushname')))))
                os.system(f"webpmux -set exif cache/{ran}.exif {ran}.webp -o {ran}.webp")
                if len(open(f"{ran}.webp","rb").read()) > 1024*1024:
                    Msg.reply_message("Sticker Melebihi Batas Maksimal")
                else:
                    driver.wapi_functions.sendImageAsSticker(convert_to_base64("%s.webp"%ran)[23:],Msg.chat_id,{})
                os.remove(f"{ran}.webp")
                os.remove(f"cache/{ran}.exif")
        except Exception as e:
            print(f"Error -> {str(e)}")
    elif caption.lower().split()[0] == "iphone":
        ran=Msg.save_media('./cache',Msg.media_key).split('/')[-1][:-4]
        Convert(f"cache/{ran}.mp4").Merge(f"cache/{ran}.mp4")
        driver.send_media(f'cache/{ran}.mp4',Msg.chat_id,"SUKSES")
def replyCommand(Msg):
    global prefix, stop
    chat     = Msg.content[len(prefix):]
    args     = chat.split(' ')[1:]
    kpt      = chat.lower().split(' ')[0].lower()
    chat_id  = Msg.chat_id
    kpt      = chat.lower().split(' ')[0].lower()
    ran      = secrets.token_hex(7)
    spams    = spam(Msg.sender.id).check()
    if spams:
        Msg.reply_message(f"Spam Terdeteksi Silahkan Tunggu *{spams.get('s')}* Detik")
    elif kpt == 'qrmaker':
        if len(args) == 0:
            Msg.reply_message('*salah*')
        else:
            pyqrcode.create(chat.replace(kpt+' ','')).png('cache/bar.png', scale=6)
            driver.send_media('cache/bar.png',chat_id,'text : %s'%(chat.replace(kpt,'')))
    elif kpt == "afk":
        afk.update({Msg.sender.id:sh if (sh:=chat[len(kpt)+1:]) else "Tanpa Alasan"})
        Msg.reply_message(f"Afk Berhasil Reason {sh if (sh:=chat[len(kpt)+1:]) else 'Tanpa Alasan'}")
    elif kpt == "countdown":
        if args[0].isnumeric():
            setCountDown({"chat_id":chat_id, "time":time.time()+int(args[0])})
            Msg.reply_message(f"Hitung Berhasil Di Set {args[0]} Detik")
        else:
            Msg.reply_message("Argumen Berupa Angka (detik)")
    elif kpt == "tele_sticker":
        if args:
                x=t_sticker(chat[len(kpt)+1:])
                if x=="error":
                    Msg.reply_message("Nama Sticker Tidak Di Temukan")
                else:
                    Msg.reply_message("Sticker Ditemukan Harap Tunggu Proses converting.....")
                    for i in enumerate(x):
                        if stop:
                            stop=0
                            break
                        else:
                            open(f"cache/{ran}_{i[0]}.tgs" if i[1]["anim"] else f"cache/{ran}_{i[0]}.webp","wb").write(i[1]["content"].content)
                            if i[1]["anim"]:
                                os.system(f"lottie_convert.py cache/{ran}_{i[0]}.tgs cache/{ran}_{i[0]}.gif")
                                (im:=Image.open(f"cache/{ran}_{i[0]}.gif")).save(f"cache/{ran}_{i[0]}.webp", transparency=im.info.get("transparency"), duration=im.info.get("duration",0), quality=20, save_all=True, exif=stickerExif(packname="Telegram"))
                            else:
                                (im:=Image.open(f"cache/{ran}_{i[0]}.webp")).resize(tuple(patternRes(im.width, im.height)))
                                polosan=Image.new("RGBA", (512, 512), color=(0, 0, 0, 0))
                                polosan.paste(im, (256-(int(im.width/2)), 256-(int(im.height/2))))
                                polosan.save(f"cache/{ran}_{i[0]}.webp", exif=stickerExif(packname="Telegram"))
                            if len(open(f"cache/{ran}_{i[0]}.webp","rb").read()) > 1024*1024:
                                Msg.reply_message("Sticker melebihi batas max")
                            else:
                                threading.Thread(target=driver.wapi_functions.sendImageAsSticker, args=(convert_to_base64(f"cache/{ran}_{i[0]}.webp")[23:],Msg.chat_id,{})).start()
        else:
            Msg.reply_message("Masukan Nama Stciker")
    elif kpt == "nsearchs":
        if get_nsfw(chat_id) or "@c.us" in chat_id:
            if args:
                if (ada:=nsearch(chat[len(kpt)+1:])):
                    Msg.reply_message("\n".join(map(lambda x:f"Title: {x['title']}\nNuclear: {x['nuklir']}", ada)))
                else:
                    Msg.reply_message("Not Found")
            else:
                Msg.reply_message("input nuclear code")
        else:
            Msg.reply_message("NSFW Tidak Aktif Harap Private Chat Untuk Menggunakan Perintah ini")
    elif kpt == "tiktok2":
        if args:
            tik=tiktok2(args[0]).download()
            driver.wapi_functions.sendImage(convert_to_base64(BytesIO(tik[0].get(tik[1]["url"][0], headers=tik[2]).content)), chat_id, "hasil.mp4", f"*Judul:*: {tik[1]['title']}\n*Pada*: {tik[1]['date']}")
        else:
            Msg.reply_message("Masukan URL")
    elif kpt == "wasted":
        rep=GetRepMedia(Msg)
        if rep.type in ["image", "sticker"]:
            buf=BytesIO()
            paste_transparant_layer(Image.open(BytesIO(driver.download_media(rep).read()))).save(buf, format="jpg")
            driver.wapi_functions.sendImage(convert_to_base64(buf), chat_id, "wasted.jpg", "berhasil")
        else:
            Msg.reply_message("Masukan Gambar")
    elif kpt == "refresh":
        if Msg.sender.id in author:
            Msg.reply_message("BOT Sedang Merefresh Halaman Whatsapp")
            driver.driver.refresh()
        else:
            Msg.reply_message("Anda Bukan Author Bot")
    elif kpt == "ifilter":
        rep=GetRepMedia(Msg)
        if rep.type == "image":
            if args:
                tp=instagram_filter(BytesIO(driver.download_media(rep).read()), args[0])
                if isinstance(tp, str):
                    Msg.reply_message(tp)
                else:
                    Image.open(tp).save(f"cache/{ran}.png")
                    driver.send_media(f"cache/{ran}.png", chat_id,f"*Filter*: {args[0]}")
                    #driver.wapi_functions(convert_to_base64(tp), Msg.chat_id, "ig.png", f"Filter: {args[0]}")
            else:
                Msg.reply_message("Masukan Nama Filter")
        else:
            Msg.reply_message("Reply Gambar Untuk Di Filter")
    elif kpt == "iphone":
        rep=GetRepMedia(Msg)
        if rep.type == "video":
            open(f"cache/{ran}.mp4", "wb").write(driver.download_media(rep).read())
            Convert(f"cache/{ran}.mp4").Merge(f"cache/{ran}.mp4")
            driver.send_media(f'cache/{ran}.mp4',chat_id,"SUKSES")
        else:
            Msg.reply_message("Untuk Video")
    elif kpt == "nsearch":
        if get_nsfw(chat_id) or "@c.us" in chat_id:
            if args:
                if (ada:=random.choice(nsearch(chat[len(kpt)+1:]))):
                    driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(ada['thumbnail']).content)),chat_id, f"{ada['title']}.jpg",f"Title: {ada['title']}\nNuklir: {ada['nuklir']}")
                else:
                    Msg.reply_message("Not Found")
            else:
                Msg.reply_message("input nuclear code")
        else:
            Msg.reply_message("NSFW Tidak Aktif Harap Private Chat Untuk Menggunakannya")
    elif kpt == "pyexec":
        if Msg.sender.id in author:
            ret=""">>> """
            try:
                with stdoutIO() as e:
                    exec(chat[len(kpt)+1:])
                Msg.reply_message(f"{ret}{chat[len(kpt)+1:]}\n{e.getvalue()}")
            except Exception as e:
                Msg.reply_message(f"{ret}{chat[len(kpt)+1:]}\nError: {e}")
        else:
            Msg.reply_message("Anda Bukan Author Bot")
    elif kpt == "dadu":
        driver.wapi_functions.sendImageAsSticker(convert_to_base64(f"assets/dadoo/_{random.randint(1,6)}.webp")[23:],Msg.chat_id,{})
    elif kpt == "blackpink":
        blackpink(chat[len(kpt)+1:]).save(f"cache/{ran}.jpg")
        driver.send_media(f"cache/{ran}.jpg",chat_id, "*Berhasil Dibuat*")
    elif kpt == "save_sticker":
        rep=GetRepMedia(Msg)
        open(f"cache/{ran}.webp","wb").write(driver.download_media(rep).read())
        if rep.type == "sticker":
            if args:
                Msg.reply_message(stickerSave(user=Msg.sender.id, name=chat[len(kpt)+1:], url=f"cache/{ran}.webp"))
            else:
                Msg.reply_message("Masukan Nama Sticker")
        else:
            Msg.reply_message("Tag Sticker Yg ingin Di Simpan")
    elif kpt == "get_sticker":
        if args:
            hasil=getSticker(Msg.sender.id,chat[len(kpt)+1:])
            if hasil.get("status"):
                downloadDrive(hasil.get("konten"),f"cache/{ran}.webp")
                ocke=Image.open(f"cache/{ran}.webp")
                if "ANMF" in open(f"cache/{ran}.webp","rb").read().decode("latin"):
                    os.mkdir(f"cache/{ran}")
                    fn=[]
                    for i in range(ocke.n_frames):
                        ocke.seek(i)
                        ocke.save(f"cache/{ran}/{i}.png")
                        fn.append(f"cache/{ran}/{i}.png")
                    editor.ImageSequenceClip(fn, fps=15, durations=ocke.info["duration"]).write_videofile(f"cache/{ran}/{ran}.mp4")
                    os.system(f"""ffmpeg -i cache/{ran}/{ran}.mp4 -y -vcodec libwebp -filter_complex "scale='min(512,512)':min'(512,512)':force_original_aspect_ratio=decrease,fps=15, pad=512:512:-1:-1:color=white@0.0,split[a][b];[a]palettegen=reserve_transparent=on:transparency_color=ffffff[p];[b][p]paletteuse" -f webp cache/{ran}.webp""")
                    os.system(f"rm -rf cache/{ran}")
                    open(f"cache/{ran}.exif","wb").write(stickerExif(packname=driver.wapi_functions.getMe().get('pushname')))
                    os.system(f"webpmux -set exif cache/{ran}.exif cache/{ran}.webp -o cache/{ran}.webp")
                    driver.wapi_functions.sendImageAsSticker(convert_to_base64("cache/%s.webp"%ran)[23:],Msg.chat_id,{})
                    #driver.wapi_functions.sendImage(convert_to_base64(f"cache/{ran}/{ran}.mp4"), chat_id, "pitch.mp4","Sticker Berhasil Di Download")
                else:
                    ocke.save(f"cache/{ran}.webp", exif=stickerExif(packname=driver.wapi_functions.getMe().get('pushname')))
                    driver.wapi_functions.sendImageAsSticker(convert_to_base64("cache/%s.webp"%ran)[23:],Msg.chat_id,{})
            else:
                Msg.reply_message("Nama Sticker Tidak Di Temukan")
        else:
            Msg.reply_message("Masukan Nama Sticker")
    elif kpt == "delete_sticker":
        if args:
            Msg.reply_message(deleteSticker(Msg.sender.id, chat[len(kpt)+1:]))
        else:
            Msg.reply_message("Masukan Nama Sticker")
    elif kpt == "list_sticker":
         Msg.reply_message(getListSticker(Msg.sender.id))
    elif kpt == "status":
        Msg.reply_message(system_info())
    elif kpt == "cari_gambar":
        res=goimage(chat[len(kpt)+1:])
        for i in range(5):
            img=requests.get(random.choice(res[random.choice(["png","jpeg","jpg"])]))
            if img.status_code == 200:
                driver.wapi_functions.sendImage(convert_to_base64(BytesIO(img.content)), chat_id, "cari_gambar.jpg", f"*Query:* {chat[len(kpt)+1:]}")
                break
    elif kpt == "pitch":
        rep=GetRepMedia(Msg)
        if rep.type in ["audio","ptt"]:
            open(f"{ran}.mp3","wb").write(driver.download_media(rep).read())
            if rep.type == "ptt":
                editor.AudioFileClip(f"{ran}.mp3").write_audiofile(f"{ran}.mp3")
            if args:
                try:
                    level=float(args[0])
                except ValueError:
                    level=0.5
                pitch(f"{ran}.mp3", f"{ran}.mp3", level_pitch=level)
            else:
                pitch(f"{ran}.mp3",f"{ran}.mp3")
            driver.wapi_functions.sendImage(convert_to_base64(f"{ran}.mp3"), chat_id, "pitch.mp3","")
            os.remove(f"{ran}.mp3")
        else:
            Msg.reply_message("Tag Audio Yg Ingin Di Pitch")
    elif kpt == 'toimg':
        rep=GetRepMedia(Msg)
        if rep.type == "sticker":
            open(f"cache/{ran}.webp","wb").write(driver.download_media(rep).read())
            if 'ANMF' in open(f"cache/{ran}.webp","rb").read().decode('latin'):
                Image.open(f"cache/{ran}.webp").save(f"cache/{ran}.gif", save_all=True)
                editor.VideoFileClip(f"cache/{ran}.gif").write_videofile(f"cache/{ran}.mp4")
                driver.wapi_functions.sendImage(convert_to_base64(f"cache/{ran}.mp4"), chat_id, "toimg.mp4", "*Berhasil*")
                os.remove(f"cache/{ran}.gif")
                os.remove(f"cache/{ran}.mp4")
            else:
                Image.open(f"cache/{ran}.webp").save(f"cache/{ran}.png")
                driver.wapi_functions.sendImage(convert_to_base64(f"cache/{ran}.png"), chat_id, "toimg.png", "*Berhasil*")
                os.remove(f"{ran}.png")
            os.remove(f"{ran}.webp")
    elif kpt == "other_bots":
        broadcast_serv(chat_id, "activate_bot")
        Msg.reply_message("Please Wait")
    elif kpt == "runtime":
        runtime=time.time()-starttime
        Msg.reply_message(f"*Bot Berjalan Selama {int(runtime//3600)} Jam {int(runtime%3600//60)} Menit {int(runtime%60)} Detik*")
    elif kpt == "pembersihan":
        if Msg.sender.id in author:
            for i in driver.get_all_groups():
                threading.Thread(target=driver.wapi_functions.sendMessage, args=(i.id,f"Bot akan Keluar dikarnakan {driver.wapi_functions.getMe().get('pushname')} sedang pembersihan, Harap Tunggu 20 menit lagi untuk menginvite kembali")).start()
                threading.Thread(target=driver.wapi_functions.leaveGroup, args=(i.id)).start()
                threading.Thread(target=driver.wapi_functions.deleteConversation, args=(i.id)).start()
            for i in driver.get_all_chats():
                threading.Thread(target=driver.delete_chat, args=(i.id)).start()
    elif kpt == "sclear":
        if Msg.sender.id in author:
            for i in driver.get_all_chats():
                threading.Thread(target=driver.wapi_functions.leaveGroup, args=(i.id)).start()
            for i in driver.get_all_groups():
                threading.Thread(target=driver.wapi_functions.deleteConversation, args=(i.id)).start()
        else:
            Msg.reply_message("Anda Bukan Author Bot")
    elif kpt == "twitter_download":
        if args:
            res=twettdownload(args[0])
            if res:
                Sum=list(map(lambda x:int(x["res"][0])+int(x["res"][1]), res["url"]))
                driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(res["url"][Sum.index(max(Sum))]["url"]).content)), chat_id, "tweet.mp4", f"""
*Author :* {res.get("author")}
*Caption:* {res.get("caption")}
                """.strip())
            else:
                Msg.reply_message("masukan url video yg valid")
        else:
            Msg.reply_message("Masukan Url Video Twitter")
    elif kpt == "execute":
        if args:
            if args[0].isnumeric():
                ex=langExecute(int(args[0]),chat[len(kpt)+len(args[0])+2:])
                if '{' in ex.__str__():
                    Msg.reply_message(f"""
*Output:*
{ex.get('output')}

*CpuTime:*
{ex.get('cpuTime')}

*Memory:*
{ex.get('memory')}

*ExecuteTime:*
{ex.get('executeTime')}""")
                else:
                    Msg.reply_message(ex)
            else:
                Msg.reply_message(ListLang())
        else:
            Msg.reply_message(ListLang())
    elif kpt == "cmd":
        if Msg.sender.id in author:
            Msg.reply_message(os.popen(chat[len(kpt)+1:]).read())
        else:
            Msg.reply_message("Anda Bukan Author Bot")
    elif kpt == "ping":
        try:
            res = subprocess.Popen(["/bin/ping", "-c1","web.whatsapp.com"], stdout=subprocess.PIPE).stdout.read().decode()
            Exp, js =re.search("time\=([0-9]{1,9}.[0-9]{1,4} ms)",res), requests.get("https://api.myip.com").json()
            Msg.reply_message(f"Kecepatan: {Exp[1]}\nIp: {js['ip']}\nNegara: {js['country']}" if Exp else "Gagal Menyambung Koneksi")
        except Exception as e:
            print(f"error -> {str(e)}")
    elif kpt == "kquote":
        if args:
            pilih=difflib.get_close_matches(chat[len(kpt)+1:], [i for i in mutiara.keys()], n=1)
            if pilih:
                Msg.reply_message(f"*Tag:* ```{pilih[0]}```\n    _{random.choice(mutiara[pilih[0]])}_")
            else:
                Msg.reply_message("*Tags Tidak Di Temukan*")
        else:
            tags=random.choice([i for i in mutiara.keys()])
            Msg.reply_message(f"*Tag:* ```{tags}```\n    _{random.choice(mutiara[tags])}_")
    elif kpt == "pintdown":
        try:
            if args:
                vid=vidPinDownload(args[0])
                vid.download().write_videofile(f"{ran}.mp4",threads=8)
                driver.send_media(f"{ran}.mp4",chat_id,"*Berhasil*")
                os.remove(f"{ran}.mp4")
            else:
                Msg.reply_message(f"{prefix}pintdown [Pinterest Url Video]")
        except Exception as e:
            Msg.reply_message("*Mengambil Video Gagal*")
            print(f"Error -> {str(e)}")
    elif kpt == "check":
        if args:
            if Msg.sender.id in running:
                Msg.reply_message("Harap Tunggu Yg Tadi")
            elif args[0].count('x') < 3:
                running.append(Msg.sender.id)
                pesan=""
                for i in CCGenrate(f"{args[0]}@c.us"):
                    if driver.wapi_functions.checkNumberStatus(i).get("status") == 200:
                        pesan+=f"https://wa.me/{i[:-5]}\n"
                Msg.reply_message(pesan.strip())
                running.remove(Msg.sender.id)
            else:
                Msg.reply_message("Masukan Nomer dengan x")
    elif kpt == "whatimage":
        rep=GetRepMedia(Msg)
        if rep.type == "image":
            Msg.reply_message(searchWithImage(imgUploader(base64.b64encode(driver.download_media(rep).read())).get("url")))
    elif kpt == "img2ascii":
        rep=GetRepMedia(Msg)
        if rep.type == "image":
            open(f"{ran}.jpg", "wb").write(driver.download_media(rep).read())
            driver.wapi_functions.sendImage(convert_to_base64(img2ascii(f"{ran}.jpg")), chat_id, "jp2a.png","*berhasil*")
            os.remove(f"{ran}.jpg")
        else:
            Msg.reply_message("Tag Gambar Yg ingin di konversi")
    elif kpt == "8bit":
        rep=GetRepMedia(Msg)
        if rep.type == "image":
            open(f"{ran}.jpg", "wb").write(driver.download_media(rep).read())
            driver.wapi_functions.sendImage(convert_to_base64(eight_bit(f"{ran}.jpg")), chat_id, "jp2a.png","*berhasil*")
            os.remove(f"{ran}.jpg")
        elif rep.type == "sticker":
            im=Image.open(BytesIO(driver.download_media(rep).read()))
            im.seek(0)
            im.save(f"{ran}.jpg")
            driver.wapi_functions.sendImage(convert_to_base64(eight_bit(f"{ran}.jpg")), chat_id, "jp2a.png","*berhasil*")
            os.remove(f"{ran}.jpg")
        else:
            Msg.reply_message("Tag Gambar Yg ingin di konversi")
    elif kpt == "whoisthis":
        rep=GetRepMedia(Msg)
        if rep.type == "image":
            res=imgUploader(base64.b64encode(driver.download_media(rep).read())).get("url")
            if res:
                Msg.reply_message(detect(res))
            else:
                Msg.reply_message("Gagal Mengindetifikasi Gambar")
        else:
            Msg.reply_message("Tag Gambar YG Ingin Di Indentifikasi")
    elif kpt == "transcript":
        rep=GetRepMedia(Msg)
        if rep.type == "ptt":
            open(f"{ran}.ogg","wb").write(driver.download_media(rep).read())
            if args:
                Msg.reply_message(SpeechToText(os.path.abspath(f"{ran}.ogg"), lang=args[0]))
            else:
                Msg.reply_message(SpeechToText(os.path.abspath(f"{ran}.ogg")))
        else:
            Msg.reply_message("Hanya Berlaku Untuk Pesan Suara")
    elif kpt == "tstiker":
        QuoteTrans(chat[len(kpt)+1:]).save(f"cache/{ran}.png")
        driver.send_image_as_sticker(f"cache/{ran}.png",Msg.chat_id)
        os.remove(f"cache/{ran}.png")
    elif kpt == "report":
        pesan=f"""
---------➤REPORT
*Dari*  : {Msg.sender.id.replace("@c.us","")}
*Pesan* : {''.join(filter(lambda x:ord(x) < 600, chat[len(kpt)+1:]))}
"""
        pyqrcode.create(base64.b64encode(pickle.dumps({"chat_id":chat_id,"msg_id":Msg.id})).decode()).png('cache/report.png', scale=6)
        for i in author:
            driver.send_media('cache/report.png',i,pesan)
        Msg.reply_message("Report Terkirim")
    elif kpt == "cimage":
        rep=GetRepMedia(Msg)
        arg=chat[len(kpt)+1:].split("|")
        if rep.type in ["image","sticker"]:
            open("cache/%s.png"%ran,"wb").write(driver.download_media(rep).read())
            if len(arg) == 3:
                resizeTo("cache/%s.png"%ran).save("cache/%s.png"%ran)
                EditR(fn="cache/%s.png"%ran,top=arg[0],bot=arg[1],color=((0,0,0) if arg[2] == "1" else (255, 255, 255))).ExecuteCommand()
                pasteLayer("cache/%s.png"%ran,packname="".join(filter(lambda ch:ord(ch)<256, chat[len(kpt)+1:] if args else driver.wapi_functions.getMe().get('pushname') )))
                driver.wapi_functions.sendImageAsSticker(convert_to_base64("cache/%s.png.webp"%ran)[23:],Msg.chat_id,{})
                os.remove("%s.png"%ran)
            else:
                Msg.reply_message(f"{prefix}cimage Atas|Bawah|1\n1:hitam\n0: putih")
    elif kpt == "replyreport":
        if Msg.sender.id in author:
            rep=GetRepMedia(Msg)
            if rep.type == "image":
                img=decode(Image.open(driver.download_media(rep)))
                info = pickle.loads(base64.b64decode(img[0][0].decode()))
                chatId,msgId=info["chat_id"], info["msg_id"]
                driver.wapi_functions.reply(chatId,f"""
---------➤REPLY REPORT
*Dari*  : Author
*Pesan* : {chat[len(kpt)+1:]}
""", msgId) if img else Msg.reply_message('Gambar Tidak Valid')
                Msg.reply_message("Berhasil Terkirim")
        else:
            Msg.reply_message("Anda Bukan Author")
    elif kpt == "tiktok":
        if args:
            TikTok=tiktok()
            tk=TikTok.download(args[0])
            if tk.get("video"):
                driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(tk.get("video")[0]).content)), chat_id, "stalk.mp4", '*Berhasil*')
            else:
                Msg.reply_message("Url YG Anda Masukan Salah")
    elif kpt == "igstalk":
        if args:
            driver.wapi_functions.sendMessage(chat_id,"Sedang Mencari 🔍")
            userProperty=igstalker(args[0].replace("@",""))
            if userProperty:
                driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(userProperty["pic"]).content)), chat_id, "stalk.jpg", f'''
*Nama Pengguna* : {userProperty["username"]}
*Mengikuti*     : {userProperty["following"]}
*Di Ikuti*     : {userProperty["follower"]}
*Jumlah Post*   : {userProperty["post"]}
----------➤BIO
{userProperty["bio"]}
''')
            else:
                Msg.reply_message("Nama Pengguna Tidak Ada ❌")
        else:
            Msg.reply_message("Masukan Nama Pengguna Yg Ingin Di Stalk")
    elif kpt  == "simi":
        Msg.reply_message(chatbot(chat[len(kpt)+1:]))
    elif kpt == "quote1":
        rep=GetRepMedia(Msg)
        if rep.type == "image":
            arg=chat[7:].split('|')
            for i in range(arg.count('')):
                arg.remove('')
            if len(arg) == 3:
                color = (0, 0, 0) if arg[2] == "1" else (255, 255, 255)
                wri = driver.download_media(rep)
                open("cache/%s.jpg"%ran,"wb").write(wri.read())
                desain("cache/%s.jpg"%ran, katakata=arg[0], author=arg[1], col=color)
                driver.send_media("cache/%s.jpg"%ran, chat_id, "Apakah Kamu Suka")
            else:
                Msg.reply_message("Perintah Salah")
    elif kpt == 'qrreader':
        rep=GetRepMedia(Msg)
        if rep.type == "image":
            wri = driver.download_media(rep)
            img=decode(Image.open(wri))
            Msg.reply_message('Text : %s\nType : %s'%(img[0][0].decode(), img[0][1])) if img else Msg.reply_message('Gambar Tidak Valid')
    elif kpt == "wait":
        rep=GetRepMedia(Msg)
        if rep.type == "image":
            wri = driver.download_media(rep)
            open("cache/%s.jpg"%ran,"wb").write(wri.read())
            res=WhatAnimeIsThis("cache/%s.jpg"%ran)
            if res["status"]:
                driver.wapi_functions.sendImage(convert_to_base64(BytesIO(res["video"].content)), Msg.chat_id, "wait.mp4")
                Msg.reply_message(res["hasil"])
            else:
                Msg.reply_message("Gagal di cari")
            os.remove("cache/%s.jpg"%ran)
    elif kpt == "grup":
        if '@g.us' in Msg.chat_id:
            desc=(js_obj:=driver.get_chat_from_id(chat_id)._js_obj)["groupMetadata"].get("desc")
            owner=js_obj["groupMetadata"]["owner"].replace("@c.us","")
            cht=js_obj["contact"].get("formattedName")
            create=datetime.datetime.fromtimestamp(js_obj["groupMetadata"].get("creation")).strftime("%H:%M:%S %A %e %B %Y")
            pesan=f"""
*Name  :* {cht}
*created by:* {owner}
*On  :* {create}
*Desc  :* {desc}
*AntiToxic:* { at if (at:=get_AntiToxic(chat_id)) else 'Nonaktif'}
*Nsfw  :* {['Nonaktif', 'Aktif'][get_nsfw(chat_id)]}
""".strip()
            driver.wapi_functions.sendImage(convert_to_base64(BytesIO(res if (res:=driver.get_profile_pic_from_id(chat_id)) else requests.get('https://cdn4.iconfinder.com/data/icons/small-n-flat/24/user-group-512.png').content)), chat_id, "grup.jpg",pesan)
        else:
            Msg.reply_message("Hanya Berlaku Di Dalam Grup")
    elif kpt == "set_prefix":
        #Msg.reply_message("Fitur Ini Dinonaktifkan karna menggangu performa bot")
        """if Msg.sender.id in driver.wapi_functions.getGroupAdmins(chat_id):
            if args:
                set_prefix(chat_id,args[0], driver.get_chat_from_id(chat_id)._js_obj["contact"].get("formattedName"))
                Msg.reply_message(f"Awalan berhasil di set ke *{args[0]}*")
            else:
                Msg.reply_message("Masukan Parameter contoh : ! % * #")
        else:
            Msg.reply_message("Anda Bukan Admin Grup")"""
    elif kpt == "set":
        if Msg.sender.id in author:
            prefix = chat[len(kpt)+1:]
            Msg.reply_message(f"Awalan Perintah Berhasil Diganti dengan {prefix}")
        else:
            Msg.reply_message("Anda Bukan Author Bot")
    elif kpt == "tulis":
        tulisan=tulis(chat[len(kpt)+1:])
        for i in tulisan:
            ran=secrets.token_hex(7)
            i.save("cache/%s.jpg"%ran)
            driver.send_media("cache/%s.jpg"%ran, chat_id,"Berhasil Ditulis 📝")
            os.remove("cache/%s.jpg"%ran)
    elif kpt == "upimg":
        rep=GetRepMedia(Msg)
        if rep.type == "image":
            wri = driver.download_media(rep)
            Msg.reply_message(imgUploader(base64.b64encode(wri.read()).decode()).get("msg"))
    elif kpt == "ocr":
        rep=GetRepMedia(Msg)
        if rep.type == "image":
            wri = driver.download_media(rep)
            open("%s.jpg"%ran, "wb").write(wri.read())
            Msg.reply_message(tesserocr.file_to_text("%s.jpg"%ran, lang="eng+ind+jap+chi").strip())
            os.remove("%s.jpg"%ran)
    elif kpt == "gf":
        if isUsers(Msg.sender.id[:-5]):
            hasil=get_female()
            pesan=f"""
╭───────「 PROFILE 」─────
│ Name  : {hasil.get('nama')}
│ Gender: Female
│ Age   : {hasil.get('umur')}
│ Bio   : {hasil.get('bio')}
│ Whatsapp: {hasil.get('chat_id')}
╰──────────────────────
            """
            driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(hasil.get("profile")).content)), chat_id, "profile.jpg", pesan.strip())
        else:
            Msg.reply_message(f"type *{prefix}reg* to use this feature")
    elif kpt == "bf":
        if isUsers(Msg.sender.id[:-5]):
            hasil=get_male()
            pesan=f"""
╭───────「 PROFILE 」──────
│ Name  : {hasil.get('nama')}
│ Gender: Male
│ Age   : {hasil.get('umur')}
│ Bio   : {hasil.get('bio')}
│ Whatsapp: {hasil.get('chat_id')}
╰──────────────────────
            """
            driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(hasil.get("profile")).content)), chat_id, "profile.jpg", pesan.strip())
        else:
            Msg.reply_message(f"type *{prefix}reg* to use this feature")
    elif kpt == "reg":
        rep=GetRepMedia(Msg)
        if rep.type =="image":
            capt=chat[len(kpt)+1:].split('|')
            fn=Msg.save_media('./cache',Msg.media_key)
            if ((nama:=capt[0]) and (umur:=capt[1]).isnumeric() and (gender:= capt[2] if capt[2] in ["male","female"] else None) and (bio:=capt[3])):
                set_user(nama=nama, umur=umur, gender=capt[2], bio=bio, profile=imgUploader(base64.b64encode(driver.download_media(rep).read())).get("url"), chat_id=Msg.sender.id[:-5], from_bot=driver.wapi_functions.getMe()["wid"], from_id=Msg.chat_id)
            else:
                Msg.reply_message(f"*e.g:*\n  {prefix}reg name|age|gender[male|female]|bio")
        else:
            Msg.reply_message("captions and images are required")
    elif kpt == "gif":
        rep= GetRepMedia(Msg)
        try:
            if rep.type == "video":
                wri = driver.download_media(rep)
                open("%s.mp4"%ran, "wb").write(wri.read())
                mv=editor.VideoFileClip("%s.mp4"%ran)
                if int(mv.duration) <= 10:
                    if mv.size[0] < 512 or mv.size[1] < 512:
                        pattern=patternRes(mv.size[0], mv.size[1])
                        sticker=mv.resize(*pattern)
                        sticker.write_videofile(f"{ran}.mp4")
                    os.system(f"""ffmpeg -i {ran}.mp4 -y -vcodec libwebp -filter_complex "scale='min(512,512)':min'(512,512)':force_original_aspect_ratio=decrease,fps=15, pad=512:512:-1:-1:color=white@0.0,split[a][b];[a]palettegen=reserve_transparent=on:transparency_color=ffffff[p];[b][p]paletteuse" -f webp {ran}.webp""")
                    open(f"cache/{ran}.exif","wb").write(stickerExif(packname="".join(filter(lambda ch:ord(ch)<256, chat[len(kpt)+1:] if args else driver.wapi_functions.getMe().get('pushname')))))
                    os.system(f"webpmux -set exif cache/{ran}.exif {ran}.webp -o {ran}.webp")
                    if len(open(f"{ran}.webp","rb").read()) > 1253376:
                        Msg.reply_message("Sticker Melebihi Batas Maksimal")
                    else:
                        driver.wapi_functions.sendImageAsSticker(convert_to_base64("%s.webp"%ran)[23:],Msg.chat_id,{})
                    os.remove(f"{ran}.mp4")
                    os.remove(f"{ran}.webp")
                    os.remove(f"cache/{ran}.exif")
                else:
                    Msg.reply_message("Max 10 Detik")
            else:
                Msg.reply_message("Masukan Video Max 10 Detik")
        except Exception as e:
            print(f"Error -> {str(e)}")
    elif kpt == "url2sticker":
        try:
            if args:
                img=Image.open(BytesIO(requests.get(args[0]).content))
                patt=patternRes(*img.size)
                fr_=[]
                if not (img.width == 512 and img.height == 512):
                    if "is_animated" in dir(img):
                        for i in range(img.n_frames):
                            img.seek(i)
                            fr_.append(img.resize(tuple(patt)))
                        fr_[0].save(f"cache/{ran}.webp", save_all=True, quality=20, duration=img.info.get("duration",0),append_images=fr_[1:], exif=stickerExif(packname=chat[len(kpt)+1+len(args[0])+1:]))
                    else:
                        img.resize(tuple(patt)).save(f"cache/{ran}.webp", exif=stickerExif(packname=chat[len(kpt)+1+len(args[0])+1:]))
                else:
                    img.save(f"cache/{ran}.webp", save_all=True, quality=20, duration=img.info.get("duration",0), exif=stickerExif(packname=chat[len(kpt)+1+len(args[0])+1:]))
                if len(open(f"cache/{ran}.webp",'rb').read()) > 1253376:
                    Msg.reply_message("Sticker Melebihi Batas Maksimal")
                else:
                    driver.wapi_functions.sendImageAsSticker(convert_to_base64("cache/%s.webp"%ran)[23:],Msg.chat_id,{"width":patt[0], "height":patt[1]})
            else:
                Msg.reply_message("Masukan Url Gambar")
        except Exception as e:
            print(f"Error->{str(e)}")
            Msg.reply_message("Masukan Url ")
    elif kpt in ["sticker","stiker"]:
        rep = GetRepMedia(Msg)
        if rep.type == "image":
            wri = driver.download_media(rep)
            open("cache/%s.png"%ran,"wb").write(wri.read())
            pasteLayer("cache/%s.png"%ran,packname="".join(filter(lambda ch:ord(ch)<256, chat[len(kpt)+1:] if args else driver.wapi_functions.getMe().get('pushname') )))
            driver.wapi_functions.sendImageAsSticker(convert_to_base64("cache/%s.png.webp"%ran)[23:],Msg.chat_id,{})
            os.remove("cache/%s.png.webp"%ran)
    elif kpt == 'fb':
        try:
            link=fbvid(args[0])
            driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(link["url"]).content)), chat_id, "fb.mp4","") if link["status"] else Msg.reply_message("Kemungkinan Link video salah/ video di privasikan") 
        except Exception as e:
            print(f"Error -> {str(e)}")
            pass
    elif kpt == 'intro':
        Msg.reply_message(f"---------➤INTRO\n➤🙋‍♂Hallo Saya {driver.wapi_functions.getMe().get('pushname')} Saya Di Bangun 🛠️ Dengan Bahasa Python3.8 🐍 Dan Beberapa API🔥")
    elif kpt in ['menu','help']:
        driver.wapi_functions.sendMessage(chat_id, MenuList(prefix,driver.wapi_functions.getMe().get('pushname'), author, Msg.sender.push_name))
    elif kpt == 'joke':
        ffff=None
        _help, dat=f'''
-------------➤JOKE
{prefix}joke [CATEGORY] [FLAGS]
-------➤CATEGORY
1: Programming
2: Miscellaneous
3: Dark
4: Funny
-------➤FLAGS
1: Nsfw
2: Religious
3: Political
4: Racist
5: Sexist

*Masukan Categori Flags Dengan Pilihan Angka*''', {'flags':{'1':'nsfw','2':'religious','3':'political','4':'racist','5':'sexist'},'category':{'1':'Programming','2':'Miscellaneous','3':'Dark','4':'Pun'}}
        if(len(args) == 2 and args[0].isnumeric()) and (args[1].isnumeric()):
            try:
                ffff=requests.get('https://sv443.net/jokeapi/v2/joke/%s?blacklistFlags=%s'%(dat['category'][args[0]],dat['flags'][args[0]])).json()
            except:
                Msg.reply_message(_help)
            if ffff['error']:
                Msg.reply_message(_help)
            else:
                if ffff["type"] == "single":
                    Msg.reply_message(tra.translate(text=ffff['joke'], dest='id').text)
                elif ffff["type"] == "twopart":
                    Msg.reply_message(tra.translate(text='%s\n%s'%(ffff['setup'], ffff['delivery']), dest='id').text)
                else:
                    Msg.reply_message("Harap Ulangi Terjadi Kesalahan Dalam System")
        else:
            Msg.reply_message(_help)
    elif kpt == 'bct':
        try:
            Msg.reply_message(bacot(chat[len(kpt)+1:]))
        except:
            Msg.reply_message('masukan Text')
    elif kpt == "xnx2mp4":
        if ("@g.us" in Msg.chat_id and get_nsfw(chat_id) == 1) or "@c.us" in Msg.chat_id:
                result=scrapX(args[0])
                if not result:
                    Msg.reply_message("*Video Tidak Di Temukan Harap Masukan Url Dengan Benar !*")
                elif result.get("msg") == "max":
                    Msg.reply_message("*Video Melebihi Batas Maksimum*")
                else:
                    driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(result["thumb"]).content)), chat_id, "bo.jpg",f'*Title* : {result["judul"]}\n*Size*  : {result["size"]}\n*Desc*  : {result["desc"]}\n\n\n*Harap Tunggu Proses Uploadnya*')
                    driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(result["vid"]).content)), chat_id, "bo.mp4","*Note* : Dosa Di Tanggung Sendiri")
        else:
            Msg.reply_message("Mode Nsfw Nonaktif Atau Anda Bisa Chat Pribadi Dengan Saya")
    elif kpt == "nsfw":
        if "@g.us" in Msg.chat_id:
            if Msg.sender.id in driver.wapi_functions.getGroupAdmins(chat_id):
                if args[0].isnumeric():
                    if int(args[0]) == 1:
                        set_nsfw(Msg.chat_id, 1, driver.get_chat_from_id(chat_id)._js_obj["contact"].get("formattedName"), from_bot=driver.wapi_functions.getMe()["wid"])
                    elif int(args[0]) == 0:
                        set_nsfw(Msg.chat_id, 0, driver.get_chat_from_id(chat_id)._js_obj["contact"].get("formattedName"), from_bot=driver.wapi_functions.getMe()["wid"])
                    else:
                        driver.wapi_functions.sendMessage(chat_id,"Masukan 1 untuk *mengaktifkan* dan 0 untuk *menonaktifkan*")
                else:
                    driver.wapi_functions.sendMessage(chat_id,"Masukan 1 untuk *mengaktifkan* dan 0 untuk *menonaktifkan*")
            else:
                Msg.reply_message('Anda Bukan Admin Group')
        else:
            Msg.reply_message("Group Only")
    elif kpt == "chord":
        hasil=cordIndo(chat[len(kpt)+1:])
        driver.wapi_functions.sendMessage(chat_id, hasil if args else "Masukan Judul Lagu")
    elif kpt == "notoxic":
        if Msg.sender.id in driver.wapi_functions.getGroupAdmins(chat_id):
            if isAdmin(chat_id):
                if int(args[0]) == 1:
                    if len(args) == 2:
                        if args[1].isnumeric():
                            set_AntiToxic(chat_id, int(args[1]), driver.get_chat_from_id(chat_id)._js_obj["contact"].get("formattedName"), from_bot=driver.wapi_functions.getMe()["wid"])
                        else:
                            driver.wapi_functions.sendMessage(chat_id, "Masukan Jumlah Max peringatan")
                    else:
                        driver.wapi_functions.sendMessage(chat_id, "Masukan Jumlah Max peringatan")
                elif int(args[0]) == 0:
                    set_AntiToxic(chat_id, 0, driver.get_chat_from_id(chat_id)._js_obj["contact"].get("formattedName"))
                    driver.wapi_functions.sendMessage(chat_id, "Menonaktifkan Anti Toxic Berhasil")
                else:
                    driver.wapi_functions.sendMessage(chat_id, "Masukan 1 untuk *mengaktifkan* dan 0 untuk *menonaktifkan*")
            else:
                driver.wapi_functions.sendMessage(chat_id, "Jadikan Saya Menjadi Admin Terlebih Dahulu")
        else:
            Msg.reply_message('Anda Bukan Admin Group')
    elif kpt == 'kick':
        if "@g.us" in Msg.chat_id:
            for i in args:
                try:
                    if Msg.sender.id in driver.wapi_functions.getGroupAdmins(chat_id):
                        if isAdmin(chat_id):
                            if driver.remove_participant_group(chat_id, args[0].replace("@","")+"@c.us"):
                                Msg.reply_message("Berhasil")
                            else:
                                Msg.reply_message("Kick Gagal") 
                        else:
                            driver.wapi_functions.sendMessage(chat_id, "Bot Belum Jadi Admin")
                    else:
                        Msg.reply_message('Anda Bukan Admin') 
                except Exception as e:
                    print(f"Error -> {str(e)}")
                    Msg.reply_message("Gagal")
        else:
            Msg.reply_message("Hanya Berlaku Di Dalam Grup")
    elif kpt == "delete":
        if "@g.us" in Msg.chat_id:
            if Msg._js_obj["quotedMsgObj"]:
                id_ = Msg._js_obj["quotedMsgObj"]["id"]
                chat_id = Msg.chat_id
                Msg.reply_message("Hanya Pesan Bot Yg Bisa Di Hapus")  if not driver.wapi_functions.deleteMessage(chat_id,id_,True) else True if Msg.sender.id in driver.wapi_functions.getGroupAdmins(chat_id) else Msg.reply_message("Tag Pesan Bot Yg Ingin Di Hapus")
        else:
            Msg.reply_message("Hanya Berlaku Di Dalam Grup")

    elif kpt == "pinterest":
        if args:
            try:
                shr=gsearch(f"'{chat[len(kpt)+1:]}' site:pinterest.com inurl:/pin")[:-1]
                if shr:
                    sh=pinterest(random.choice(shr))
                    if sh:
                        if sh[-4:] == ".gif":
                            editor.VideoFileClip(sh).write_videofile(f"{ran}.mp4")
                            driver.send_media(f"{ran}.mp4", chat_id,f"*{chat[len(kpt)+1:]}*")
                            os.remove(f"{ran}.mp4")
                        elif sh[-4:] == ".mp4":
                            driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(sh).content)), chat_id, "pin.mp4",f"*{chat[len(kpt)+1:]}*")
                        else:
                            driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(sh).content)), chat_id, "pin.jpg",f"*{chat[len(kpt)+1:]}*")
                    else:
                        Msg.reply_message("Gambar Tidak Di Temukan")
                else:
                    Msg.reply_message("Query Tidak Ditemukan")
            except Exception as e:
                print(f"Error -> {str(e)}")
        else:
            Msg.reply_message("Masukan Query Gambar")
    elif kpt == 'admin':
        try:
            (driver.promove_participant_admin_group(chat_id,args[0].replace('@','')+'@c.us') if len(args) == 1 else Msg.reply_message(f'{prefix}admin @tag')) if Msg.sender.id in driver.wapi_functions.getGroupAdmins(chat_id) else Msg.reply_message('Anda Bukan Admin Group') if isAdmin(chat_id) else driver.wapi_functions.sendMessage(chat_id, "Jadikan Saya Menjadi Admin Terlebih Dahulu") if '@g.us' in Msg.chat_id else Msg.reply_message("Hanya Berlaku Di Dalam Grup")
        except Exception as e:
            print(f"Error -> {str(e)}")
            Msg.reply_message("Admin Gagal")
    elif kpt == 'unadmin':
        try:
            (driver.demote_participant_admin_group(chat_id,args[0].replace('@','')+'@c.us') if len(args) == 1 else Msg.reply_message(f'{prefix}unadmin 62xxxxx')) if Msg.sender.id in driver.wapi_functions.getGroupAdmins(chat_id) else Msg.reply_message('Anda Bukan Admin Group') if isAdmin(chat_id) else driver.wapi_functions.sendMessage(chat_id, "Jadikan Saya Menjadi Admin Terlebih Dahulu") if '@g.us' in Msg.chat_id else Msg.reply_message("Hanya Berlaku Di Dalam Grup")
        except Exception as e:
            print(f"Error -> {str(e)}")
            Msg.reply_message("UnAdmin Gagal")
    elif kpt == 'revoke':
        try:
            (driver.wapi_functions.sendMessage(chat_id, 'Tautan Grup Berhasil Ditarik') if driver.wapi_functions.revokeGroupInviteLink(Msg.chat_id) else driver.wapi_functions.sendMessage(chat_id, 'Tautan Grup Gagal Ditarik')) if Msg.sender.id in driver.wapi_functions.getGroupAdmins(chat_id) else Msg.reply_message('Anda Bukan Admin Group') if isAdmin(chat_id) else driver.wapi_functions.sendMessage(chat_id, "Jadikan Saya Menjadi Admin Terlebih Dahulu") if '@g.us' in Msg.chat_id else Msg.reply_message("Hanya Berlaku Di Dalam Grup")
        except Exception as e:
            print(f"Error -> {str(e)}")
            driver.wapi_functions.sendMessage(chat_id, "Menarik Tautan Gagal")
    elif kpt == 'add':
        try:
            (((Msg.reply_message('Berhasil Ditambahkan') if driver.add_participant_group(chat_id,args[0]+'@c.us') else Msg.reply_message('Gagal Ditambahkan')) if Msg.sender.id in driver.wapi_functions.getGroupAdmins(chat_id) else Msg.reply_message('Gagal Di Tambahkan')) if isAdmin(chat_id) else driver.wapi_functions.sendMessage(chat_id, "Jadikan Saya Menjadi Admin Terlebih Dahulu")) if '@g.us' in Msg.chat_id else Msg.reply_message("Hanya Berlaku Di Dalam Grup")
        except Exception as e:
            print(f"Error -> {str(e)}")
            Msg.reply_message(f'---------➤ADD\n{prefix}add 628xxxxxxx')
    elif kpt == 'linkgroup':
        try:
            (driver.wapi_functions.getGroupInviteLink(Msg.chat_id) if isAdmin(chat_id) else driver.wapi_functions.sendMessage(chat_id, "Jadikan Saya Menjadi Admin Terlebih Dahulu")) if '@g.us' in Msg.chat_id else Msg.reply_message("Hanya Berlaku Di Dalam Grup")
        except:
            Msg.reply_message('Angkat Bot ini Menjadi Admin Dulu')
    elif kpt == 'fdeface':
        if (rep:=GetRepMedia(Msg)).type == "image":
            if len((arr:=list(filter(lambda x:x, chat[len(kpt)+1:].split('|'))))) > 3:
                driver.wapi_functions.sendMessageWithThumb(convert_to_base64(BytesIO(driver.download_media(rep).read()), is_thumbnail=True), arr[0],arr[1],arr[2],arr[3],chat_id)
            else:
                Msg.reply_message(f"e.g : {prefix}fdeface url|title|desc|text")
        else:
            Msg.reply_message(f"e.g[reply with image] : {prefix}fdeface url|title|desc|text")
    elif kpt == 'list-admin':
        pesan='|---------➤LIST ADMIN\n'
        for i in driver.wapi_functions.getGroupAdmins(chat_id):
            pesan+='|-➤ @%s\n'%(i.replace('@c.us',''))
        pesan+="|---------➤END"
        driver.wapi_functions.sendMessageWithMentions(chat_id,pesan,'')
    elif kpt == 'owner':
        if "@g.us" in Msg.chat_id :
            own=driver.get_chat_from_id(chat_id)._js_obj["groupMetadata"]["owner"].replace("@c.us","")
            driver.wapi_functions.sendVCard(chat_id, f'BEGIN:VCARD\nVERSION:3.0\nFN:OWNER GRUP\nTEL;type=CELL;type=VOICE;waid={own}:{own}\nEND:VCARD')
        else:
            Msg.reply_message("Grup Only")
    elif kpt == 'pitnah':
        if len(args) > 1:
            cha=chat[len(kpt)+len(args[0])+2:]
            pos=list(re.compile("\|").finditer(cha))[0].span()[0] if list(re.compile("\|").finditer(cha)) else None
            pesan=cha[pos+1:].strip() if pos else "."
            pitnah=cha[:pos].strip() if pos else cha
            #kpatch.FakeReply(args[0].replace("c.us","").replace("@",""), pitnah, Msg.chat_id, Msg.id, pesan)
            driver.driver.execute_script(FakeReply(args[0].replace("c.us","").replace("@",""), pitnah, Msg.chat_id, Msg.id, pesan))
            #driver.driver.execute_script(f'return FakeReply(\"{args[0].replace("c.us","").replace("@","pitnah")}\", \"{pitnah}\", \"{Msg.chat_id}\",\"{Msg.id}\", \"{pesan}\")')
        else:
            Msg.reply_message(f"*Contoh*: {prefix}pitnah @korban fitnah|pesan bot")
    elif kpt == 'kitsune':
        driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(json.loads(requests.get('http://randomfox.ca/floof/').text)['image']).content)), chat_id, "kitsune.jpg","What Is This")
    elif kpt == 'dog':
        driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get("http"+literal_eval(requests.get('http://shibe.online/api/shibes?count=1').text)[0][5:]).content)), chat_id, "Dog.jpg","What Is This")
    elif kpt == 'neko':
        driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(json.loads(requests.get('http://api.thecatapi.com/v1/images/search').text)[0]['url']).content)), chat_id, "Neko.jpg","What Is This")
    elif kpt == 'doujin':
        if get_nsfw(Msg.chat_id) or "@c.us" in chat_id:
            if args:
                if (fn:=asyncio.run(parser_nuklir(args[0]))):
                    driver.send_media(fn, chat_id, "")
                else:
                    Msg.reply_message("Kode Nuklir Tidak Benar")
        else:
                Msg.reply_message("Mode Nsfw Nonaktif Atau Anda Bisa Chat Pribadi Dengan Saya")
    elif kpt == "bc":
        if Msg.sender.id in author:
            pesan="[[ %s Broadcast ]]\n%s"%(driver.wapi_functions.getMe().get('pushname'), chat[len(kpt)+1:].strip())
            for i in driver.get_all_chat_ids():
                threading.Thread(target=driver.wapi_functions.sendMessage, args=(i,pesan,)).start()
        else:
            Msg.reply_message("Anda Bukan Author")
    elif kpt == 'quote':
        try:
            hasil = json.loads(requests.get('http://api.quotable.io/random',params={'tags':args[0]}).text) if args else json.loads(requests.get('http://api.quotable.io/random').text)
            tags=''
            for i in hasil['tags']:
                tags+='    %s\n'%(i)
            pesan='''*Author* : %s
*Tags* :
%s
[EN] : %s
[ID] : %s'''%(hasil['author'], tags, hasil['content'],tra.translate(text=hasil['content'], dest='id').text)
            Msg.reply_message(pesan)
        except:
            Msg.reply_message('Tags Tidak Ada')
    elif kpt == "morse":
        te=morse(chat[len(kpt)+1:])
        Msg.reply_message(f"""Text: {te['text']}\nMorse: {te['morse']}""")
    elif kpt == "alay":
        te=alay(chat[len(kpt)+1:])
        Msg.reply_message(te)
    elif kpt == 'yt2mp3':
        if args:
            try:
                has=Yt2Mp3(url=args[0])
                if has["status"] == "Large":
                    Msg.reply_message("Ukuran File Melebihi Batas Maksimal")
                elif has["status"] == "Belum Tersedia":
                    Msg.reply_message("Belum Tersedia")
                elif has["status"] == True:
                    aud=editor.AudioFileClip(has["url"])
                    Image.open(BytesIO(requests.get(has["thumb"]).content)).save(f"cache/{ran}.jpg")
                    driver.wapi_functions.sendImage(convert_to_base64(f"cache/{ran}.jpg"), chat_id,"thumb.jpg",has["info"])
                    aud.write_audiofile("cache/%s.mp3"%ran)
                    audio=MP3("cache/%s.mp3"%ran, ID3=ID3)
                    audio["TIT2"] = TIT2(encoding=3, text=has["judul"])
                    audio["APIC"] = APIC(mime="image/jpg",type=3, data=requests.get(has["thumb"].replace("vi_webp","vi").replace(".webp",".jpg")).content)
                    audio.save()
                    driver.wapi_functions.sendMessage(chat_id, "Sedang Mengunggah⏳")
                    driver.send_media("cache/%s.mp3"%ran, chat_id, "")
                    os.remove("cache/%s.mp3"%ran)
                else:
                    Msg.reply_message("Link Video Tidak Valid/kirim Ulang")
            except Exception as e:
                print(f"Error -> {str(e)}")
        else:
            Msg.reply_message("Masukan Url")
    elif kpt == 'play':
        if args:
            try:
                has=Yt2Mp3(query=f"{chat[len(kpt)+1:]}")
                if has["status"] == "Large":
                    Msg.reply_message("Ukuran File Melebihi Batas Maksimal")
                elif has["status"] == "Belum Tersedia":
                    Msg.reply_message("Belum Tersedia")
                elif has["status"] == True:
                    aud=editor.AudioFileClip(has["url"])
                    Image.open(BytesIO(requests.get(has["thumb"]).content)).save(f"cache/{ran}.jpg")
                    driver.wapi_functions.sendImage(convert_to_base64(f"cache/{ran}.jpg"), chat_id,"thumb.jpg",has["info"])
                    aud.write_audiofile("cache/%s.mp3"%ran)
                    audio=MP3("cache/%s.mp3"%ran, ID3=ID3)
                    audio["TIT2"] = TIT2(encoding=3, text=has["judul"])
                    audio["APIC"] = APIC(mime="image/jpg",type=3, data=requests.get(has["thumb"].replace("vi_webp","vi").replace(".webp",".jpg")).content)
                    audio.save()
                    driver.wapi_functions.sendMessage(chat_id, "Sedang Mengunggah⏳")
                    driver.send_media("cache/%s.mp3"%ran, chat_id, "")
                    os.remove("cache/%s.mp3"%ran)
                else:
                    Msg.reply_message("Link Video Tidak Valid/kirim Ulang")
            except Exception as e:
                print(f"Error -> {str(e)}")
        else:
            Msg.reply_message("Masukan Judul Musik")
    elif kpt == 'yt2mp4':
        if args:
            for i in range(3):
                dow=yt2mp4(args[0])
                if dow.get("object"):
                    Image.open(BytesIO(requests.get(dow.get("thumb").replace("vi_webp","vi").replace(".webp",".jpg")).content)).save(f"cache/{ran}.jpg")
                    driver.wapi_functions.sendImage(convert_to_base64(f"cache/{ran}.jpg"), chat_id, "yt.jpg", f"*Judul:* {dow['title']}\n*Dilihat*: {dow['view']}\n*Ukuran:* {dow['size']}\n*Harap Tunggu Proses Uploadnya*")
                    dow["result"].write_videofile(f"{ran}.mp4")
                    driver.send_media(f"{ran}.mp4",chat_id,"")
                    os.remove(f"{ran}.mp4")
                    break
                elif dow["status"] == True:
                    driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(dow.get("thumb").replace("vi_webp","vi").replace(".webp",".jpg")).content)), chat_id, "yt.jpg", f"*Judul:* {dow['title']}\n*Dilihat*: {dow['view']}\n*Ukuran:* {dow['size']}\n*Harap Tunggu Proses Uploadnya*")
                    driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(dow["result"]).content)), chat_id, "yt.mp4", "")
                    break
                elif dow["status"] == "L":
                    Msg.reply_message("Ukuran File Melebihi Batas")
                    break
                elif dow["status"] == "url":
                    pass
            else:
                Msg.reply_message("Mengambl Video Gagal")
        else:
            Msg.reply_message("Masukan Tautan Youtube")
    elif kpt == 'gambar':
        driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get('https://source.unsplash.com/1600x900/?%s'%(args[0]) if args else 'https://source.unsplash.com/random').content)), chat_id, "Image.jpeg", "Apakah Kamu Suka ?")
    elif kpt == 'mentionall':
        if Msg.sender.id in driver.wapi_functions.getGroupAdmins(chat_id) or Msg.sender.id in author:
            semua=driver.wapi_functions.getGroupParticipantIDs(chat_id)
            pesan='|---------➤MENTION ALL\n'
            for i in semua:
                pesan+='⎢-➣ @%s \n'%(i)
            pesan+="|---------➤END"
            driver.wapi_functions.sendMessageWithMentions(chat_id, pesan.replace('@c.us',''),'')
        else:
            Msg.reply_message('Anda Bukan Admin Group')
    elif kpt == 'hidetag':
        if Msg.sender.id in driver.wapi_functions.getGroupAdmins(chat_id) or Msg.sender.id in author:
            pesan=''
            for i in driver.wapi_functions.getGroupParticipantIDs(chat_id):
                pesan+=f'@{i} '
            #kpatch.hidetag(chat_id, pesan.replace("@c.us",""), chat[len(kpt)+1:] if args else "P"))
            driver.driver.execute_script(hidetag(chat_id, pesan.replace("@c.us",""), chat[len(kpt)+1:] if args else "P"))
        else:
            Msg.reply_message('Anda Bukan Admin Group')
    elif kpt == '?':
        if args:
            jum, soal = ((int(args[-1])), chat[len(kpt)+1:-len(args[-1])]) if args[-1].isnumeric() else (1, chat[len(kpt)+1:])
            driver.wapi_functions.sendMessage(chat_id, "Sedang Mencari 🔎")
            cari=gsearch('"%s" site:brainly.co.id'%soal)
            temp=[]
            for i in cari:
                temp.append(i) if 'google.com' not in i and 'tugas' in i else False
            if temp:
                for i in temp[:jum]:
                    try:
                        threading.Thread(target=driver.wapi_functions.sendMessage, args=(chat_id,brainly(i))).start()
                    except:
                        Msg.reply_message('❌ Gagal Mencari Jawaban ❌')
            else:
                driver.wapi_functions.sendMessage(chat_id, '❌ Mencari Jawaban *%s* Tidak Ada ❌'%(soal))
        else:
            Msg.reply_message('❌ Masukan Soal Yg Ingin Di Jawab ❌')
    elif kpt == 'cari':
        try:
            driver.wapi_functions.sendMessage(chat_id, "Sedang Mencari 🔎")
            hasil = wikipedia.search(chat.replace(chat[len(kpt)+1:],''))
            pesan='hasil pencarian : \n'
            for i in hasil:
                pesan+='⎢-➣ %s\n'%(i)
            Msg.reply_message(pesan)
        except:
            Msg.reply_message('Masukan Parameternya Bro')
    elif kpt == 'wiki':
        try:
            hasil=wikipedia.page(chat[len(kpt)+1:])
            Msg.reply_message('*title* :%s\n*source* : %s\n%s'%(hasil.title, hasil.url, hasil.content))
        except:
            Msg.reply_message('❌ YG Anda Cari Tidak Ada ❌')
    elif kpt == 'quotemaker':
        '''
        ---------➤QUOTE MAKER
#quotemaker |[kata]|[author]|[kategori]
        '''
        try:
            arg=chat[len(kpt)+1:].split('|')
            for i in range(arg.count('')):
                arg.remove('')
            hasil=json.loads(requests.get('https://terhambar.com/aw/qts/?kata=%s&author=%s&tipe=%s', params={'kata':arg[0],'author':arg[1],'tipe':arg[2]}).text)
            driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(hasil['result']).content)), chat_id,"quotes.jpg", "Apakah Kamu Suka ?") if hasil['status'] else Msg.reply_message(f'{prefix}quotemaker|<kata>|<author>|<kategori>')
        except:
            Msg.reply_message(f'---------➤QUOTE MAKER\n{prefix}quotemaker |[kata]|[author]|[kategori]')
    elif kpt == 'cc':
        try:
            Msg.reply_message(open('assets/cc1.txt',"r").read())
        except Exception as e:
            print(f"Error -> {str(e)}")
    elif kpt == 'ts':
        try:
            Msg.reply_message(tra.translate(text=chat[len(kpt)+1+len(args[0])+1:], dest=args[0]).text)
        except Exception as e:
            print(f"Error -> {str(e)}")
            Msg.reply_message(f'ts [Target] [Text]\nContoh :\n {prefix}ts id good morning \nketik {prefix}cc untuk melihat kode negara')
    elif kpt == 'run':
        Msg.reply_message('Hasil Eksekusi :\n%s'%(requests.get('https://twilio-apis.herokuapp.com/',params={'cmd':chat[len(kpt)+1:]}).text))
    elif kpt == 'waifu':
        Msg.reply_message("Commad Telah Di Hapus")
        #hasil=waifu()
        #driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(hasil["image"]).content)), chat_id, "waifu.jpg",hasil["title"])
    elif kpt == "attp":
        if args:
            iop=BytesIO()
            ok=ThreadPoolExecutor(max_workers=10)
            img=list(map(lambda x:ok.submit(QuoteTrans, chat[len(kpt)+1:], color=tuple(x)).result(), [[252, 3, 3], [252, 13, 3], [252, 23, 3], [252, 33, 3], [252, 43, 3], [252, 53, 3], [252, 63, 3], [252, 73, 3], [252, 83, 3], [252, 93, 3], [252, 103, 3], [252, 113, 3], [252, 123, 3], [252, 133, 3], [252, 143, 3], [252, 153, 3], [252, 163, 3], [252, 173, 3], [252, 183, 3], [252, 193, 3], [252, 203, 3], [252, 213, 3], [252, 223, 3], [252, 233, 3], [252, 243, 3], [252, 253, 3], [242, 253, 3], [232, 253, 3], [222, 253, 3], [212, 253, 3], [202, 253, 3], [192, 253, 3], [182, 253, 3], [172, 253, 3], [162, 253, 3], [152, 253, 3], [142, 253, 3], [132, 253, 3], [122, 253, 3], [112, 253, 3], [102, 253, 3], [92, 253, 3], [82, 253, 3], [72, 253, 3], [62, 253, 3], [52, 253, 3], [42, 253, 3], [32, 253, 3], [22, 253, 3], [12, 253, 3], [3, 253, 4], [3, 253, 14], [3, 253, 24], [3, 253, 34], [3, 253, 44], [3, 253, 54], [3, 253, 64], [3, 253, 74], [3, 253, 84], [3, 253, 94], [3, 253, 104], [3, 253, 114], [3, 253, 124], [3, 253, 134], [3, 253, 144], [3, 253, 154], [3, 253, 164], [3, 253, 174], [3, 253, 184], [3, 253, 194], [3, 253, 204], [3, 253, 214], [3, 253, 224], [3, 253, 234], [3, 253, 244], [3, 252, 253], [3, 242, 253], [3, 232, 253], [3, 222, 253], [3, 212, 253], [3, 202, 253], [3, 192, 253], [3, 182, 253], [3, 172, 253], [3, 162, 253], [3, 152, 253], [3, 142, 253], [3, 132, 253], [3, 122, 253], [3, 112, 253], [3, 102, 253], [3, 92, 253], [3, 82, 253], [3, 72, 253], [3, 62, 253], [3, 52, 253], [3, 42, 253], [3, 32, 253], [3, 22, 253], [3, 12, 253], [4, 3, 253], [14, 3, 253], [24, 3, 253], [34, 3, 253], [44, 3, 253], [54, 3, 253], [64, 3, 253], [74, 3, 253], [84, 3, 253], [94, 3, 253], [104, 3, 253], [114, 3, 253], [124, 3, 253], [134, 3, 253], [144, 3, 253], [154, 3, 253], [164, 3, 253], [174, 3, 253], [184, 3, 253], [194, 3, 253], [204, 3, 253], [214, 3, 253], [224, 3, 253], [234, 3, 253], [244, 3, 253], [253, 3, 252], [253, 3, 242], [253, 3, 232], [253, 3, 222], [253, 3, 212], [253, 3, 202], [253, 3, 192], [253, 3, 182], [253, 3, 172], [253, 3, 162], [253, 3, 152], [253, 3, 142], [253, 3, 132], [253, 3, 122], [253, 3, 112], [253, 3, 102], [253, 3, 92], [253, 3, 82], [253, 3, 72], [253, 3, 62], [253, 3, 52], [253, 3, 42], [253, 3, 32], [253, 3, 22], [253, 3, 12]]))
            img[0].save(iop, format="webp", save_all=True, append_images=img[1:], duration=1, loop=900, quality=20)
            open(f"cache/{ran}.webp", "wb").write(iop.getvalue())
            if iop.getvalue().__len__() > 1024*1024:
                Msg.reply_message("Ukuran Sticker Melebihi Batas")
            else:
                driver.wapi_functions.sendImageAsSticker(convert_to_base64(f"cache/{ran}.webp")[23:],Msg.chat_id,{})
    elif kpt == 'url2png':
        if args:
            url2img=url2png(args[0])
            if url2img.get("ss"):
                driver.wapi_functions.sendImage(convert_to_base64(url2img.get("ss")), chat_id,"url2png.png",f"Link : *{args[0]}*")
            else:
                Msg.reply_message("Masukan Url Dengan Valid")
        else:
            Msg.reply_message('Masukan Url/Tautan')
    elif kpt == 'ig':
        ob=igdownload(args[0])
        if ob["status"]:
            for i in ob["result"]:
                if i["type"] == "image":
                    driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(i["url"]).content)), chat_id,"ig.jpg","")
                elif i["type"] == "video":
                    driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(i["url"]).content)), chat_id,"ig.mp4","")
        else:
            Msg.reply_message("Link Error")
    elif kpt == 'tts':
        try:
            gTTS(text=chat[len(kpt)+1+len(args[0])+1:] ,lang=args[0]).save(f'cache/{ran}.mp3')
            driver.send_media('cache/%s.mp3'%ran,chat_id,'')
            os.remove("cache/%s.mp3"%ran)
        except:
            Msg.reply_message(f"---------➤TextToSpeak\n{prefix}tts [cc] [text]\nketik : {prefix}cc untuk melihat kode negara")
    elif kpt == "kusonime":
        try:
            result_scrap=scrap_kusonime(search_kusonime(chat[len(kpt)+1:]))
            driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(result_scrap["thumb"]).content)), chat_id, "kusonime.jpg",result_scrap["info"])
            Msg.reply_message("Sinopsis:\n %s\nLink Download:\n %s"%(result_scrap["sinopsis"], result_scrap["link_dl"]))
        except:
            Msg.reply("❌ Anime : %s Tidak Ada ❌"%(chat[7:]))
    elif kpt == "otakudesu":
        try:
            result_scrap=scrap_otakudesu(search_otakudesu(chat[len(kpt)+1:]))
            driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(result_scrap["thumb"]).content)), chat_id, "OtakuDesu.jpg","%s\nSinopsis : %s"%(result_scrap["info"], result_scrap["sinopsis"]))
        except:
            Msg.reply_message("❌ Anime : %s Tidak Ada ❌"%(chat[len(kpt)+1:]))
    elif kpt == "quran":
        if args:
            Msg.reply_message(findSurah(args[0], args[1]))
        else:
            Msg.reply_message("Masukan No Surat Dan Nomer Ayat")
    elif kpt == 'film':
        driver.wapi_functions.sendMessage(chat_id, "Sedang Mencari 🔎")
        hasil=gsearch('"%s" site:sdmovie.fun'%chat[len(kpt)+1:])
        h=0
        for i in hasil:
            if ('sdmovie' in i and 'google' not in i):
                h+=1
                Link=''
                hafun=fun(i)
                for o in hafun['video']:
                    Link+=f"{o['url']} | {o['lewat']} | {o['sub']} | {o['res']} \n "
                pesan='🎬 : %s\n*rating* : %s\n*sinopsis* : %s\n *VIDEO* :\n %s'%(hafun['title'],hafun['rating'],hafun['sinopsis'],Link)
                threading.Thread(target=driver.wapi_functions.sendImage, args=(convert_to_base64(BytesIO(requests.get(hafun['cover']).content)), chat_id, "sdmovie.jpg",hafun["title"])).start()
                threading.Thread(target=driver.wapi_functions.sendMessage, args=(chat_id,pesan)).start()
        if h==0:
            Msg.reply_message("❌ Film Yg Anda Cari Tidak Ditemukan ❌")
    elif hashlib.md5(kpt.encode()).hexdigest() in ['434990c8a25d2be94863561ae98bd682','e4764c8ba351079b78dbf732e4b873a3']: #Jangan Di Edit
        driver.wapi_functions.sendLinkWithAutoPreview(chat_id,"Saweria: https://saweria.co/donate/KryptonByte \nPaypal: https://www.paypal.com/paypalme/KryptonByte \n Pulsa: 6283172366463\n 📌Yuk Donasi Biar Bot Nya Aktif Terus Dan Mimin Nya Rajin Update & Fix Bug" )
    elif kpt == "author": #jangan Di Edit
        driver.wapi_functions.sendVCard(chat_id, 'BEGIN:VCARD\nVERSION:3.0\nFN:KRYPTON BYTE\nTEL;type=CELL;type=VOICE;waid=6283172366463:6283172366463\nEND:VCARD', None, None)
    elif kpt == "ph":
        buf=BytesIO()
        orange(*[[ chat[len(kpt)+1:].split("|")[:2] if (pha:=chat[len(kpt)+1:].split("|")).__len__() > 1 else [pha[0],"None"]]][0]).save(buf, format="png")
        driver.wapi_functions.sendImage(convert_to_base64(buf), chat_id, "ph.png", "*Berhasil Di Buat*")
    elif kpt == "join":
        join=driver.wapi_functions.joinGroupViaLink(args[0])
        time.sleep(3)
        Msg.reply_message("Tautan Undangan Rusak") if join == 406 else driver.wapi_functions.sendMessage(join, f"---------➤INTRO\n➤🙋‍♂Hallo Saya {driver.wapi_functions.getMe().get('pushname')} Saya Di Bangun 🛠️ Dengan Bahasa Python3.8 🐍 Dan Beberapa API🔥") if args else Msg.reply_message("Masukan Tautan Undanga")
    elif kpt == "sendmessage":
        if Msg.sender.id in author:
            driver.wapi_functions.sendMessage(args[0][1:]+"@c.us", " ".join(args[1:])) if args else Msg.reply_message("Tag Yg Ingin di Chat") if Msg.id in author else Msg.reply_message("Anda Bukan Author Bot")

class Observer:
    def on_message_received(self, data):
        for i in data:
            threading.Thread(target=main, args=(i, )).start()
    def on_ack_received(self, data):
        for i in data:
            if "@g.us" in i.chat_id and not i.id in TempSelf:
                threading.Thread(target=main, args=(i, )).start()
                TempSelf.append(i.id)


#==================================Server====Global==========Database=======================

app=Flask(__name__)
sio=socketio.Server(async_mode='eventlet', cors_allowed_origins='*')
@sio.on("get_qr", namespace="/serverx")
def get_qr(sid):
    if not driver.is_logged_in():
        sio.emit("qr", data={"qr":driver.get_qr_plain()}, namespace="/login", room=sid)
    else:
        sio.emit("loged", data={"Logged":True}, namespace="/login", room=sid)

@sio.on("server_", namespace="/about")
def About(sid):
    boot=time.time()-starttime
    me = driver.wapi_functions.getMe() if driver.is_logged_in() else {}
    sio.emit("percent", data={
        "boot_time":{"day":int(math.floor(boot/3600)/24),"hours":math.floor(boot/3600)%24, "minute":int(math.floor(boot/60)%60), "second":math.floor(boot%60)},
        "cpu_percent":f"{int(psutil.cpu_percent())}%",
        "disk_percent":f"{int(psutil.virtual_memory().percent)}%",
        "botname":me.get('pushname', "Krypton-Bot"),
    }, room=sid,namespace="/about")

import base64
if __name__ == '__main__':
    """if "pickle.txt" in os.listdir("."):
        driver.set_local_storage(pickle.loads(open("pickle.txt","rb").read()))
        driver.connect()"""
    @app.route('/')
    def wahai():
        if driver.is_logged_in():
            return render_template("monitor.html", waurl=f"https://wa.me/{driver.wapi_functions.getMe()['wid'][:-5]}", image_data=base64.b64encode(driver.get_profile_pic_from_id(driver.wapi_functions.getMe()['wid'])).decode())
        else:
            try:
                return f'<img src="data:image/png;base64,{driver.get_qr_base64()}"><input type="hidden" name="qr" value="{driver.get_qr_plain()}">'
            except Exception as e:
                print(e.__str__())
                driver.connect()
                return f'<img src="data:image/png;base64,{driver.get_qr_base64()}"><input type="hidden" name="qr" value="{driver.get_qr_plain()}">'
    driver.subscribe_new_messages(Observer())
    driver.subscribe_acks(Observer())
    api = socketio.WSGIApp(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', int(os.environ.get("PORT",5100)))), api)
    """
if __name__=='__main__':
    waktu = time.time()+10
    while True:
        try:
            if driver.is_logged_in():
                print("[+] Berhasil Login")
                author2.append(input("Masukan Nomor untuk di jadikan Owner contoh: 623172366463\nNomor: ")+"@c.us")
                break
            elif time.time()>waktu:
                print(pyqrcode.create(driver.get_qr_plain()).terminal(quiet_zone=1))
                waktu= time.time()+10
        except KeyboardInterrupt:
            break
        except:
            print("[*] Connection TimeOut")
            print("[*] Restarting..........")  
    driver.subscribe_new_messages(Observer())
    driver.subscribe_acks(Observer())
    while driver.is_logged_in():
        time.sleep(60*60*24) #24 jam:v"""