from requests import get
import requests
token="1411572463:AAEIw18OU2DkEZh6VYt_E979tlhFIR0n2ng"
def download(file_id):
    return get(f"https://api.telegram.org/file/bot{token}/"+get(f"https://api.telegram.org/bot{token}/getFile", params={"file_id":file_id}).json()["result"]["file_path"])
def t_sticker(name):
    try:
        return map( lambda x:{"content":download(x["file_id"]), "anim":x["is_animated"]}, get(f"https://api.telegram.org/bot{token}/getStickerSet", params={"name":name}).json()["result"]["stickers"])
    except:
        return "error"