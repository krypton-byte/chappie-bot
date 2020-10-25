#!/usr/bin/python
"""
 @AUTHOR : KRYPTON-BYTE
 @DATE   : TUE OCT 13, 2020

" Wahai Orang-orang Yg Beriman Mengapakah Kamu Mengatakan Sesuatu Yg Tidak Kamu Kerjakan? Amat Besar Kebencian Di Sisi Allah Bahwa Kamu Mengatakan Apa-apa Yang Tidak Kmau Kerjakan." (QS asg-shaff: 2-3)
"""

kasar=[]
from requests.api import request
from os import remove
from openwa.helper import convert_to_base64
from openwa import WhatsAPIDriver
from urllib.parse import quote, unquote
from bs4 import BeautifulSoup as bs
from moviepy import editor
from lib import pytube
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TIT2
from googletrans import Translator
import time, base64, os,pickle, hashlib, random, subprocess, sqlite3, wikipedia, re,secrets , pyqrcode, hashlib, json, requests
from gtts import gTTS
try:
     tesserocr
except:
    pass
from PIL import Image
from pyzbar.pyzbar import decode
from ast import Bytes, literal_eval
from gtts import gTTS
from io import BytesIO
from concurrent.futures.thread import ThreadPoolExecutor
#------------Module--------------#
from lib.sdmovie import fun
from lib.chatbot import chatbot
from lib.cropToSquare import crop_image, resizeTo, pasteLayer
from lib.api import *
from lib.kasar import *
from lib.brainly2 import *
from lib.nulis import tulis
from lib.fb import fbvid
from lib.anime import *
from lib.ig import igdownload, igstalker
#-----------setting----------------------#
tempChatBot={}
author=["6283172366463@c.us"]
wikipedia.set_lang('id')
tra=Translator()
global driver
driver=WhatsAPIDriver(client='Chrome')
FullCommand=["#help","#igstalk","#sticker","#stiker","#fb","#kusonime","#otakudesu","#delete","#upimg","#ig","#cari","#support","#cara-penggunaan","#tulis","#waifu","#qrmaker","#gambar","#intro","#kitsune","#qrreader","#?","#wait","#url2png","#run","#ocr","#doujin","#film","#nime","#ts","#cc","#tts","#quotemaker","#yt2mp3","#yt","#wiki","#list-admin","#admin","#unadmin","#kick","#add","#owner","#linkgroup","#revoke","#dog","#mentionall","#neko","#quote","gambar","#","#bc","#joke","#bct"]
_Kasar=open("lib/badword.txt","r").read() 
# kasar=open("lib/badword.txt","r").read() #hapus hastag untuk mengaktifkan Anti Toxic Dalam grup
import sqlite3
class GetRepMedia:
    def __init__(self, js):
        self.obj = js._js_obj["quotedMsg"]
        self.client_url = self.obj.get("clientUrl")
        self.media_key = self.obj.get("mediaKey")
        self.type = self.obj.get("type")
        self.crypt_keys= {'document': '576861747341707020446f63756d656e74204b657973','image': '576861747341707020496d616765204b657973','video': '576861747341707020566964656f204b657973','ptt': '576861747341707020417564696f204b657973','audio': '576861747341707020417564696f204b657973','sticker': '576861747341707020496d616765204b657973'}
def main():
    with ThreadPoolExecutor(max_workers=8) as executor:
        while True:
            task=[]
            chatTextObject=driver.get_unread()
            for chatObject in chatTextObject:
                for TextObject in chatObject.messages:
                    if TextObject.type == 'chat':
                        if set(TextObject.content.lower().split(' '))&set(kasar): #anda Bisa mengaktifkan Anti Toxic
                            if '@g.us' in TextObject.chat_id:
                                try:
                                    ksr=Kasar(TextObject.chat_id)
                                    ksr.add_check_kick(chatObject.chat, TextObject)
                                except Exception as e:
                                    False
                        elif TextObject.content.split()[0] in FullCommand or TextObject.content.split('|')[0] in FullCommand:
                            executor.submit(replyCommand, (TextObject),(chatObject.chat))
                        elif TextObject.content.split()[0] != '#' and '@g.us' != TextObject.chat_id:
                            if '@c.us' in TextObject.chat_id:
                                TextObject.reply_message(chatbot(TextObject.content))
                    elif TextObject.type == 'image':
                        executor.submit(recImageReplyCommand, (TextObject),(chatObject.chat))
                    elif TextObject.type == 'vcard':
                        masuk='SELAMAT DATANG :\n'
                        for i in TextObject.contacts:
                            for u in re.findall('waid\=(.*?):',i.decode()):
                                try:
                                    chatObject.chat.add_participant_group('%s@c.us'%(u))
                                    masuk+='-@%s'%(u)
                                except Exception:
                                    TextObject.reply_message('Menambahkan %s Sukses'%(u))
                        try:
                            driver.wapi_functions.sendMessageWithMentions(chatObject.chat.id,masuk,'')
                        except Exception:
                            False    
def recImageReplyCommand(Msg, Chat):
    caption = Msg.caption
    args=caption.split()[1:]
    ran=secrets.token_hex(7)
    if Msg.caption:
        kpt = Msg.caption.lower().split()[0]
        if kpt == "#wait":
            fn=Msg.save_media('./cache',Msg.media_key)
            res=WhatAnimeIsThis(fn)
            driver.wapi_functions.sendImage(convert_to_base64(BytesIO(res["video"].content)), Msg.chat_id, "wait.mp4", res["hasil"]) if res["status"] else Msg.reply_message("Gagal di cari")
            os.remove(fn)
        elif kpt in ['#stiker','#sticker']:
            try:
                fn=Msg.save_media('./cache',Msg.media_key)
                os.rename(fn,"cache/%s.png"%ran)
                pasteLayer("cache/%s.png"%ran)
                driver.send_image_as_sticker("cache/%s.png"%ran,Msg.chat_id)
                os.remove("cache/%s.png"%ran)
            except Exception as e:
                False
        elif kpt == "#upimg":
            fn=Msg.save_media("./cache", Msg.media_key)
            Msg.reply_message(imgUploader(base64.b64encode(open(fn,"rb").read()).decode()))
        elif kpt == '#qrreader':
            img=decode(Image.open(Msg.save_media('./cache',Msg.media_key)))
            Msg.reply_message('Text : %s\nType : %s'%(img[0][0].decode(), img[0][1])) if img else Msg.reply_message('Gambar Tidak Valid')
        elif kpt == "#ocr":
            fn=Msg.save_media("./cache", Msg.media_key)
            Msg.reply_message(tesserocr.file_to_text(fn, lang="eng+ind+jap+chi").strip())
            os.remove(fn)
def replyCommand(Msg, Chat):
    chat     = Msg.content
    args     = chat.split(' ')[1:]
    kpt      = chat.lower().split(' ')[0].lower()
    chat_id  = Msg.chat_id
    kpt      = chat.lower().split(' ')[0].lower()
    jsObject = Msg.get_js_obj()
    ran=secrets.token_hex(7)
    if kpt == '#qrmaker':
        if len(kpt) == 1:
            Msg.reply_message('*salah*')
        else:
            pyqrcode.create(chat.replace(kpt+' ','')).png('cache/bar.png', scale=6)
            driver.send_media('cache/bar.png',chat_id,'text : %s'%(chat.replace(kpt,'')))
    elif kpt == "#igstalk":
        if args:
            Chat.send_message("Sedang Mencari 🔍")
            userProperty=igstalker(args[0].replace("@",""))
            if userProperty:
                driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(userProperty["pic"]).content)), chat_id, "stalk.jpg", f'''
Nama Pengguna : {userProperty["username"]}
Mengikuti     : {userProperty["following"]}
Di Ikuti      : {userProperty["follower"]}
Jumlah Post   : {userProperty["post"]}
============BIO===========
{userProperty["bio"]}
''')
            else:
                Msg.reply_message("Nama Pengguna Tidak Ada ❌")
        else:
            Msg.reply_message("Masukan Nama Pengguna Yg Ingin Di Stalk")
    elif kpt == '#qrreader':
        rep=GetRepMedia(Msg)
        if rep.type == "image":
            wri = driver.download_media(rep)
            img=decode(Image.open(wri))
            Msg.reply_message('Text : %s\nType : %s'%(img[0][0].decode(), img[0][1])) if img else Msg.reply_message('Gambar Tidak Valid')
    elif kpt == "#wait":
        rep=GetRepMedia(Msg)
        if rep.type == "image":
            wri = driver.download_media(rep)
            open("cache/%s.jpg"%ran,"wb").write(wri.read())
            res=WhatAnimeIsThis("cache/%s.jpg"%ran)
            driver.wapi_functions.sendImage(convert_to_base64(BytesIO(res["video"].content)), chat_id, "wait.mp4", res["hasil"]) if res["status"] else Msg.reply_message("Gagal di cari")
            os.remove("cache/%s.jpg"%ran)
    elif kpt == "#tulis":
        tulisan=tulis(chat[7:])
        for i in tulisan:
            ran=secrets.token_hex(7)
            print("ran")
            i.save("cache/%s.jpg"%ran)
            driver.send_media("cache/%s.jpg"%ran, chat_id,"Berhasil Ditulis 📝")
            os.remove("cache/%s.jpg"%ran)
            print("Berhasil Di Tulis")
    elif kpt == "#upimg":
        rep=GetRepMedia(Msg)
        if rep.type == "image":
            wri = driver.download_media(rep)
            Msg.reply_message(imgUploader(base64.b64encode(wri.read()).decode()))
    elif kpt == "#ocr":
        rep=GetRepMedia(Msg)
        if rep.type == "image":
            wri = driver.download_media(rep)
            open("%s.jpg"%ran, "wb").write(wri.read())
            Msg.reply_message(tesserocr.file_to_text("%s.jpg"%ran, lang="eng+ind+jap+chi").strip())
            os.remove("%s.jpg"%ran)
    elif kpt in ["#sticker","#stiker"]:
        rep = GetRepMedia(Msg)
        if rep.type == "image":
            wri = driver.download_media(rep)
            open("cache/%s.png"%ran,"wb").write(wri.read())
            pasteLayer("cache/%s.png"%ran)
            driver.send_image_as_sticker("cache/%s.png"%ran,chat_id)
            os.remove("cache/%s.png"%ran)
    elif kpt == '#fb':
        link=fbvid(args[0])
        driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(link["url"]).content)), chat_id, "fb.mp4","") if link["status"] else Msg.reply_message("Kemungkinan Link video salah/ video di privasikan") 
    elif kpt == '#???':
        ksr = Kasar(chat_id)
        Msg.reply_message('You have said the harsh word %s times'%(ksr.check()))
    elif kpt == '#intro':
        Msg.reply_message('🙋‍♂Hallo Saya Chappie-Bot Saya Di Bangun 🛠️ Dengan Bahasa Python3.8 🐍 Dan Beberapa API🔥')
    elif kpt in ['#menu','#help']:
        Chat.send_message('''.    🛠️ TOOLS 🛠️
-> #
-> #sticker
-> #upimg
-> #ig
-> #igstalk [User]
-> #fb [Tautan Video]
-> #cari [Kata Kunci]
-> #qrmaker [Teks]
-> #qrreader
-> #? [Soal]
-> #wait
-> #tulis [Teks]
-> #ocr
-> #url2png [Tautan]
-> #run [Syntak]
-> #doujin [Kode Nuklir]
-> #film [Judul Film]
-> #kusonime [Judul Anime]
-> #otakudesu [Judul Anime]
-> #ts [cc] [text]
-> #tts [cc] [text]
-> #quotemaker|[quote]|[author]|[theme]
-> #yt2mp3 [Tautan Youtube]
-> #yt [Tautan Youtube]
-> #wiki [Kata Kunci]

     🕹️HIBURAN 🕹️

-> #dog
-> #neko
-> #quote
-> #kitsune
-> #gambar
-> # [chat]
-> #joke
-> #waifu
-> #bct [text]
    

     👁️‍🗨️   GRUP   👁️‍🗨️

-> #list-admin
-> #admin
-> #mentionall
-> #unadmin @tag
-> #delete @tag
-> #kick @tag
-> #add 62xxxx
-> #owner
-> #linkgroup
-> #revoke

     🗣️  BANTUAN 🗣️
-> #cara-penggunaan

     ☕ DUKUNGAN ☕
-> #support
-> #intro

      & Author &
-> #bc [Teks]
''')
    elif kpt == '#joke':
        _help, dat='''#joke <category> <flags>\ncategory:1:Programming\n         2:miscellaneous\n         3:dark\n         4:pun\nflags :1:nsfw\n       2:religious\n       3:political\n       4:racist\n       5:sexist''', {'flags':{'1':'nsfw','2':'religious','3':'political','4':'racist','5':'sexist'},'category':{'1':'Programming','2':'Miscellaneous','3':'Dark','4':'Pun'}}
        if(len(args) == 2 and args[0].isnumeric()) and (args[1].isnumeric()):
            try:
                global ffff
                ffff=json.loads(requests.get('https://sv443.net/jokeapi/v2/joke/%s?blacklistFlags=%s'%(dat['category'][args[0]],dat['flags'][args[0]])).text)
            except:
                Msg.reply_message(_help)
            if ffff['error']:
                Msg.reply_message(_help)
            else:
                try:
                    Msg.reply_message(tra.translate(text=ffff['joke'], dest='id').text)
                except KeyError:
                    Msg.reply_message(tra.translate(text='%s\n%s'%(ffff['setup'], ffff['delivery']), dest='id').text)
        else:
            Msg.reply_message(_help)
    elif kpt == '#bct':
        try:
            Msg.reply_message(bacot(chat[5:]))
        except:
            Msg.reply_message('masukan Text')
    elif kpt == '#kick': #for Admin
        for i in args:
            try:
                (Chat.remove_participant_group(i.replace('@','')+'@c.us') if len(args) == 1 else Msg.reply_message('#kick @tag')) if Msg.sender.id in [(x.id) for x in Chat.get_admins()] else Msg.reply_message('Anda Bukan Admin') if '@g.us' in Msg.chat_id else Msg.reply_message("Hanya Berlaku Di Dalam Grup")
            except Exception as e:
                Msg.reply_message('Terdapat Error\ndetail : %s'%(e))
    elif kpt == "#delete":
        if "@g.us" in Msg.chat_id:
            if Msg._js_obj["quotedMsgObj"]:
                id_ = Msg._js_obj["quotedMsgObj"]["id"]
                chat_id = Msg.chat_id
                if Msg.sender.id in [(x.id) for x in Chat.get_admins()]+author:
                    if not driver.wapi_functions.deleteMessage(chat_id,id_,True):
                        Msg.reply_message("Hanya Pesan Bot Yg Bisa Di Hapus")
                else:
                    Msg.reply_message("Anda Bukan Admin Grup")
            else:
                Msg.reply_message("Tag Pesan Bot Yg Ingin Di Hapus")
        else:
            Msg.reply_message("Hanya Berlaku Di Dalam Grup")


    elif kpt == '#admin':
        try:
            (Chat.promove_participant_admin_group(args[0].replace('@','')+'@c.us') if len(args) == 1 else Msg.reply_message('#admin @tag')) if Msg.sender.id in [(x.id) for x in Chat.get_admins()] else Msg.reply_message('Anda Bukan Admin Group')  if '@g.us' in Msg.chat_id else Msg.reply_message("Hanya Berlaku Di Dalam Grup")
        except Exception as e:
            Msg.reply_message('Terdapat Error\ndetail : %s'%(e))
    elif kpt == '#unadmin':
        try:
            (Chat.demote_participant_admin_group(args[0].replace('@','')+'@c.us') if len(args) == 1 else Msg.reply_message('#unadmin 62xxxxx')) if Msg.sender.id in [(x.id) for x in Chat.get_admins()] else Msg.reply_message('Anda Bukan Admin Group') if '@g.us' in Msg.chat_id else Msg.reply_message("Hanya Berlaku Di Dalam Grup")
        except Exception as e:
            Msg.reply_message('Terjadi Kesalahan\ndetail : %s'%(e))
    elif kpt == '#revoke':
        try:
            (Chat.send_message('Tautan Grup Berhasil Ditarik') if driver.wapi_functions.revokeGroupInviteLink(Msg.chat_id) else Chat.send_message('Tautan Grup Gagal Ditarik')) if Msg.sender.id in [(x.id) for x in Chat.get_admins()] else Msg.reply_message('Anda Bukan Admin Group') if '@g.us' in Msg.chat_id else Msg.reply_message("Hanya Berlaku Di Dalam Grup")
        except Exception as e:
            Chat.send_message('Terjadi kesalahan\ndetail : %s'%(e))
    elif kpt == '#add':
        try:
            ((Msg.reply_message('Berhasil Ditambahkan') if Chat.add_participant_group(args[0]+'@c.us') else Msg.reply_message('Gagal Ditambahkan')) if Msg.sender.id in [(x.id) for x in Chat.get_admins()] else Msg.reply_message('Gagal Di Tambahkan')) if '@g.us' in Msg.chat_id else Msg.reply_message("Hanya Berlaku Di Dalam Grup")
        except Exception as e:
            Msg.reply_message('Terjadi kesalahan\ndetail : %s'%(e))
    if kpt == '#linkgroup':
        try:
            Msg.reply_message(driver.wapi_functions.getGroupInviteLink(Msg.chat_id)) if '@g.us' in Msg.chat_id else Msg.reply_message("Hanya Berlaku Di Dalam Grup")
        except:
            Msg.reply_message('Angkat Bot ini Menjadi Admin Dulu')
    elif kpt == '#list-admin':
        pesan=''
        for i in Chat.get_admins():
            pesan+='nama : @%s\n'%(i.id.replace('@c.us',''))
        driver.wapi_functions.sendMessageWithMentions(Chat.id,pesan,'')
    elif kpt == '#owner':
        Msg.reply_message(Msg.get_js_obj()['chat']['groupMetadata']['owner'].replace('@c.us','')) if '@g.us' in Msg.chat_id else Msg.reply_message("Hanya Berlaku Di Dalam Grup")
    elif kpt == '#kitsune':
        driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(json.loads(requests.get('http://randomfox.ca/floof/').text)['image']).content)), chat_id, "kitsune.jpg","What Is This")
    elif kpt == '#tts':
        try:
            gTTS(text=chat[8:] ,lang=chat[5:7]).save('cache/%s.mp3'%ran)
            driver.send_media('cache/%s.mp3'%ran,chat_id,'')
            os.remove("cache/%s.mp3"%ran)
        except:
            Msg.reply_message("Masukan Perintah Dengan benar \n#tts [cc] [text]\nketik : #cc untuk melihat kode negara")
    elif kpt == '#dog':
        driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get("http"+literal_eval(requests.get('http://shibe.online/api/shibes?count=1').text)[0][5:]).content)), chat_id, "Dog.jpg","What Is This")
    elif kpt == '#neko':
        driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(json.loads(requests.get('http://api.thecatapi.com/v1/images/search').text)[0]['url']).content)), chat_id, "Neko.jpg","What Is This")
    elif kpt == '#doujin':
        doujin(args[0], driver, chat_id, Msg) if args else Msg.reply_message('Masukan Kode Nuklir')
    elif kpt == "#bc":
        if Msg.sender.id == author[0]:
            pesan="[[ Chappi-Bot Broadcast ]]\n%s"%(chat[4:].strip())
            for i in driver.get_all_chat_ids():
                driver.wapi_functions.sendMessage(i,pesan)
        else:
            Msg.reply_message("Anda Bukan Author")
    elif kpt == '#quote':
        try:
            hasil = json.loads(requests.get('http://api.quotable.io/random',params={'tags':args[0]}).text) if args else json.loads(requests.get('http://api.quotable.io/random').text)
            tags=''
            for i in hasil['tags']:
                tags+=' ↦%s\n'%(i)
                pesan='''author : %s
Tags :
%s[EN] : %s
[ID] : %s'''%(hasil['author'], tags, hasil['content'],tra.translate(text=hasil['content'], dest='id').text)
            Msg.reply_message(pesan)
        except:
            Msg.reply_message('Tags Tidak Ada')
    elif kpt == '#yt2mp3':
        if args:
            while True:
                has=yt2mp3(args[0])
                if not has["status"] == "ulang":
                    break
            if has["status"] == "Large":
                Msg.reply_message("Ukuran File Melebihi Batas Maksimal")
            elif has["status"] == True:
                aud=editor.AudioFileClip(has["url"])
                Chat.send_message("🛠️Sedang Mengkonversi Ke Audio 🛠️")
                aud.write_audiofile("cache/%s.mp3"%ran)
                Chat.send_message("🔖Menambahkan Metadata🔖")
                audio=MP3("cache/%s.mp3"%ran, ID3=ID3)
                audio["TIT2"] = TIT2(encoding=3, text=has["judul"])
                audio["APIC"] = APIC(mime="image/jpg",type=3, data=requests.get(has["thumb"]).content)
                audio.save()
                Chat.send_message("Sedang Mengunggah⏳")
                driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(has["thumb"]).content)), chat_id,"thumb.jpg",has["info"])
                driver.send_media("cache/%s.mp3"%ran, chat_id, "")
                os.remove("cache/%s.mp3"%ran)
            else:
                Msg.reply_message("Link Video Tidak Valid")
        else:
            Msg.reply_message("Masukan Url")
    elif kpt == '#yt':
        if len(args) == 2:
            print("Pilih")
            if args[1].isnumeric():
                while True:
                    print("True")
                    dow=Merger(args[0], int(args[1])).down()
                    print(dow)
                    if dow["status"] == True:
                        Chat.send_message("Merging 🛠️")
                        dow["result"].write_videofile("cache/%s.mp4"%ran)
                        Chat.send_message("Sedang Mengunggah⏳")
                        driver.send_media("cache/%s.mp4"%ran, chat_id, "")
                        os.remove("cache/%s.mp4"%ran)
                        break
                    elif dow["status"] == "L":
                        Msg.reply_message("Ukuran File Melebihi Batas")
                        break
                    elif dow["status"] == "url":
                        Msg.reply_message("Tautan Tidak Valid")
                        break
                    elif dow["status"] == "ulang":
                        print(dow)
                    print(dow)
        
            else:
                Msg.reply_message("Perintah Salah")
        else:
            if args:
                while True:
                    print("Loop")
                    paser=Merger(args[0]).parser()
                    if not paser["status"] == "ulang":
                        Msg.reply_message(paser["result"])
                        break
                if paser["status"] == "url":
                    Msg.reply_message("Tautan Tidak Valid")
            else:
                Msg.reply_message("Masukan Tautan Video")
    elif kpt == '#gambar':
        driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get('https://source.unsplash.com/1600x900/?%s'%(args[0]) if args else 'https://source.unsplash.com/random').content)), chat_id, "Image.jpeg", "Apakah Kamu Suka ?")
    elif kpt == '#mentionall':
        if Msg.sender.id in [(x.id) for x in Chat.get_admins()] or Msg.sender.id == '6283172366463@c.us':
            semua=Chat.get_participants()
            pesan=''
            for i in semua:
                pesan+='@%s '%(i.id)
            driver.wapi_functions.sendMessageWithMentions(Chat.id, pesan.replace('@c.us',''),'')
        else:
            Msg.reply_message('Anda Bukan Admin Group')
    elif kpt == '#?':
        if args:
            answers=''
            isi='''Soal    : %s\nMapel   : %s\nSekolah : %s\nTanggal : %s\n'''
            jum, soal = ((int(args[-1])), chat[3:-len(args[-1])]) if args[-1].isnumeric() else (1, chat[3:])
            Chat.send_message("Sedang Mencari 🔎")
            cari=gsearch('"%s" site:brainly.co.id'%soal)
            temp=[]
            for i in cari:
                temp.append(i) if 'google.com' not in i and 'tugas' in i else False
            if temp:
                for i in temp[:jum]:
                    try:
                        br=brainly(i)
                        Chat.send_message("%s\n%s"%(br.get("soal"), br.get("jawaban")))
                    except:
                        Msg.reply_message('❌ Gagal Mencari Jawaban ❌')
            else:
                Chat.send_message('❌ Mencari Jawaban *%s* Tidak Ada ❌'%(soal))
        else:
            Msg.reply_message('❌ Masukan Soal Yg Ingin Di Jawab ❌')
    elif kpt == '#cari':
        try:
            Chat.send_message("Sedang Mencari 🔎")
            hasil = wikipedia.search(chat.replace('#cari',''))
            pesan='hasil pencarian : \n'
            for i in hasil:
                pesan+='↦ %s\n'%(i)
            Msg.reply_message(pesan)
        except:
            Msg.reply_message('Masukan Parameternya Bro')
    elif kpt == '#wiki':
        try:
            hasil=wikipedia.page(chat[6:])
            Msg.reply_message('title :%s\nsource: %s\n%s'%(hasil.title, hasil.url, hasil.content))
        except:
            Msg.reply_message('❌ YG Anda Cari Tidak Ada ❌')
    elif chat.split('|')[0] == '#quotemaker':
        '''
        #quotemaker|<kata>|<author>|<kategori>
        '''
        try:
            arg=chat.split('|')[1:]
            hasil=json.loads(requests.get('https://terhambar.com/aw/qts/?kata=%s&author=%s&tipe=%s', params={'kata':arg[0],'author':arg[1],'tipe':arg[2]}).text)
            driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(hasil['result']).content)), chat_id,"quotes.jpg", "Apakah Kamu Suka ?") if hasil['status'] else Msg.reply_message('#quotemaker|<kata>|<author>|<kategori>')
        except:
            Msg.reply_message('#quotemaker|<kata>|<author>|<kategori>')
    elif kpt == '#cc':
        cc=json.loads(open('lib/ISO-639-1-language.json').read())
        pesan=''
        for i in cc:
            pesan+='%s : %s\n'%(i['code'], i['name'])
        Msg.reply_message(pesan)
    elif kpt == '#ts':
        try:
            Msg.reply_message(tra.translate(text=chat[7:], dest=chat[4:6]).text)
        except:
            Msg.reply_message('#ts [Target] [Text]\nContoh :\n #ts id good morning \nketik #cc untuk melihat kode negara')
    elif kpt == '#run':
        Msg.reply_message('Hasil Eksekusi :\n%s'%(requests.get('https://twilio-apis.herokuapp.com/',params={'cmd':chat[4:]}).text))
    elif kpt == '#waifu':
        hasil=waifu()
        driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(hasil["image"]).content)), chat_id, "waifu.jpg",hasil["title"])
    elif kpt == '#url2png':
        if args:
            try:
                driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(url2png(args[0])).content)), chat_id,"url2png.png","Link : %s"%args[0])
            except:
                False
        else:
            Msg.reply_message('masukan Url \n#url2png https://google.com')
    elif kpt == '#ig':
        print("ig")
        ob=igdownload(args[0])
        print("Yup")
        if ob["status"]:
            print("True")
            for i in ob["result"]:
                print("Loop")
                if i["type"] == "image":
                    print("image")
                    driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(i["url"]).content)), chat_id,"ig.jpg","")
                elif i["type"] == "video":
                    print("vid")
                    driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(i["url"]).content)), chat_id,"ig.mp4","")
        else:
            Msg.reply_message("Link Error")
    elif kpt == '#tts':
        try:
            gTTS(text=chat[8:] ,lang=chat[5:7]).save('cache/tts.mp3')
            driver.send_media('cache/%s.mp3'%ran,chat_id,'')
            os.remove("cache/%s.mp3"%ran)
        except:
            Msg.reply_message("Masukan Perintah Dengan benar \n#tts [cc] [text]\nketik : #cc untuk melihat kode negara")
    elif kpt == "#kusonime":
        try:
            result_scrap=scrap_kusonime(search_kusonime(chat[10:]))
            driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(result_scrap["thumb"]).content)), chat_id, "kusonime.jpg",result_scrap["info"])
            Msg.reply_message("Sinopsis:\n %s\nLink Download:\n %s"%(result_scrap["sinopsis"], result_scrap["link_dl"]))
        except:
            Msg.reply("❌ Anime : %s Tidak Ada ❌"%(chat[7:]))
    elif kpt == "#otakudesu":
        try:
            result_scrap=scrap_otakudesu(search_otakudesu(chat[11:]))
            driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(result_scrap["thumb"]).content)), chat_id, "OtakuDesu.jpg","%s\nSinopsis : %s"%(result_scrap["info"], result_scrap["sinopsis"]))
        except:
            Msg.reply_message("❌ Anime : %s Tidak Ada ❌"%(chat[11:]))
    elif kpt == '#film':
        Chat.send_message("Sedang Mencari 🔎")
        hasil=gsearch('"%s" site:sdmovie.fun'%chat[5:])
        h=0
        for i in hasil:
            if ('sdmovie' in i and 'google' not in i):
                h+=1
                Link=''
                hafun=fun(i)
                for o in hafun['video']:
                    Link+=f"{o['url']} | {o['lewat']} | {o['sub']} | {o['res']} \n "
                pesan='🎬 : %s\nrating: %s\nsinopsis : %s\n VIDEO :\n %s'%(hafun['title'],hafun['rating'],hafun['sinopsis'],Link)
                driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(hafun['cover']).content)), chat_id, "sdmovie.jpg",hafun["title"])
                Chat.send_message(pesan)
        if h==0:
            Msg.reply_message("❌ Film Yg Anda Cari Tidak Ditemukan ❌")
    elif hashlib.md5(kpt.encode()).hexdigest() == 'fe1538c21f7479f15103962373b2b841':
        driver.send_message_with_auto_preview(chat_id,"https://saweria.com/donate/KryptonByte" ,"📌Yuk Donasi Biar Bot Nya Aktif Terus Dan Mimin Nya Rajin Update & Fix Bug" )
    elif kpt == "#cara-penggunaan":
        Msg.reply_message('''*#help alat* -> menampilkan perintah alat
*#sticker* -> pembuat sticker
*#upimg* -> Upload Gambar Ke Img.bb
*#cari* -> cari query wikipedia
con : #cari hantu
*#qrmaker* -> pembuat qrcode
con : #qrmaker Sebuah qrcode
*#qrreader* -> pembaca qrcode
*#?* -> pencari jawaban langsung dari brainly.co.id
con : #? contoh soal matematika
con : #? contoh soal matematika 2
*#ocr* -> untuk mengambil teks di sebuah Gambar
*#url2png* -> mengubah url ke bentuk Gambar
con : #url2png https://www.google.com
*#run* -> python compiler Api
con : #run 
print("Hallo world")
*#doujin* -> Doujin Download
con : #doujin kode-nuklir
*#film* -> pencari film + link Download
con : #film chappie
*#ts* -> Translate
con : #ts en Hai
*#tts* -> text to speak
con : #tts id Hallo Saya Bot
*#cc* -> menampilkan Kode Negara
*#otakudesu* -> pencari anime
*#kusonime* -> pencari anime
*#wait* -> pencari judul Anime Menggunakan potongan scene
*#quotemaker* -> pembuat quotes
con : #quotemaker|Teks Kuotes|Penulis|happy
*#tulis* -> Menulis Text
con : #tulis Nama : Krypton-Byte
*#yt2mp3* -> pencari link download lagu dengan link youtube
con : #yt2mp3 #https://www.youtube.com/watch?v=FQQbRBs3nFY
*#yt2mp3* -> pencari download video dari youtube tidak termasuk audio
con : #yt https://www.youtube.com/watch?v=FQQbRBs3nFY
*#wiki* -> wikipedia
con : #wiki hantu
*#help grup* -> menampilkan perintah yg berlaku di dalam grup
*#list-admin* -> menampilkan admin grup
*#admin* -> mengadminkan seseorang
con : #admin @orang
con : #admin 6281234567890
*#unadmin* -> Mencopot sebagai admin
con : #unadmin @orang
con : #unadmin 6281234567890
*#kick* -> mengkick anggota grup
con : #kick @orang
con : #kick 6281234567890
*#add* -> menambah kan anggota grup
con : #add 6281234567890
atau anda bisa mengirim kartu kontak
*#owner* -> menampilkan owner grup
*#linkgroup* -> menampilkan tautan invite grup
*#revoke* -> menarik tautan invite grup
*#mentionall* -> menTag seluruh member grup
*#help bot* -> menampilkan perintah bot
*#* -> chat bot
#con : # Hai
*#help hiburan* -> menampilkan perintah yg bisa menghibur
*#dog* -> mengirimkan gambar anjing secara acak
*#neko* -> mengirimkan gambar kucing secara acak
*#kitsune* -> mengirimkan gambar rubah secra acak
*#gambar* -> mencari gambar
con : gambar cat
*#joke* -> menampilkan joke
con : #joke 1 1
con : #joke 1 3
*#waifu* -> Random Waifu 
*#bct* -> mengubah huruf semua huruf vokal ke huruf "i"
con : #bct Aku Saya kamu
*#help* -> menampilkan semua opsi help''')
    elif kpt == '#':
        if args:
            Msg.reply_message(chatbot(chat))
        else:
            Msg.reply_message('Mau Nanya apa ?')
    


if __name__ == '__main__':

    if 'pickle.txt' in os.listdir('.'):
        driver.set_local_storage(pickle.loads(open("pickle.txt","rb").read()))
        driver.connect()
        while True:
            if driver.is_logged_in():
                with ThreadPoolExecutor(max_workers=2) as executor:
                    try:
                        executor.submit(main)
                    except selenium.common.exceptions.InvalidSessionIdException:
                        pass
    else:
        while True:
            if driver.is_logged_in():
                open("pickle.txt","wb").write(pickle.dumps(driver.get_local_storage()))
                with ThreadPoolExecutor(max_workers=2) as executor:
                    try:
                        executor.submit(main)
                    except selenium.common.exceptions.InvalidSessionIdException:
                        pass
