import asyncio
from bs4 import BeautifulSoup 
import requests, re
from io import BytesIO
from PIL import Image
async def download_image(link):
    return Image.open(BytesIO(requests.get(link).content)).convert("RGB")
async def parser_nuklir(nuklir):
    try:
        source=requests.get(f"https://nhentai.net/g/{nuklir}").text
        parsing=BeautifulSoup(source, 'html.parser')
        komik=[]
        for i in parsing.find_all('a',class_='gallerythumb'):
            if i('img'):
                komik.append(download_image('https://i'+i('img')[0]['data-src'][9:-5]+'.jpg'))
        z=await asyncio.gather(*komik)
        z[0].save(f"{parsing.title.text}.pdf", save_all=True, append_images=z[1:])
        return parsing.title.text+".pdf"
    except Exception as e:
        print(e)
        return False
def nsearch(query: str):
    doujin=[]
    req=requests.get("https://nhentai.net/search", params={"q":query}).text
    title=re.findall("\<\/noscript\>\<div class\=\"caption\"\>(.*?)\</div\>",req)
    nuklir=re.findall("href\=\"/g/([0-9]{5,6})/\"",req)
    thumb=re.findall("data\-src\=\"(https://t.nhentai.net/galleries/[0-9]{6,8}/thumb.jpg)\"",req)
    for i in enumerate(thumb):
        doujin.append({"title":title[i[0]],"thumbnail":i[1],"nuklir":nuklir[i[0]]})
    return doujin