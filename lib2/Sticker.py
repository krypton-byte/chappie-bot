import requests
from lib2 import upload
from setting import server
import time
def stickerSave(user, name, url):
    save=requests.get(f"{server}/uploadSticker", params={"pengguna":user[:-5], "nama":name, "konten":upload(url).get("id")}).json()
    print(save)
    if save.get("status") == False and save.get("tersimpan") == True:
        return "Nama Sticker Sudah Ada"
    elif save.get("tersimpan") == True and save.get("status") == True:
        return "Sticker Tersimpan Ke Database *Krypton Bot*"
    else:
        return "Error"


def getListSticker(user):
    pesan="╭────「 Sticker 」──────\n"
    save=requests.get(f"{server}/getListSticker", params={"pengguna":user[:-5]}).json()
    pesan+="│+"+"\n│+".join(save.get("sticker"))
    pesan+="\n╰────────────────────"
    return pesan

def getSticker(user, name):
    return requests.get(f"{server}/getSticker", params={"pengguna":user[:-5],"nama":name}).json()


def deleteSticker(user, name):
    save=requests.get(f"{server}/DeleteSticker", params={"pengguna":user[:-5], "nama":name}).json()
    if save.get("status") == True:
        return f"Sticker *{name}* Berhasil Di Hapus Dari Database *Krypton Bot*"
    else:
        return "Sticker Tidak Di Temukan"