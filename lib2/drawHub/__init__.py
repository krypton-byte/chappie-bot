from typing import Sized
from PIL import Image, ImageDraw, ImageFont
font=ImageFont.truetype("lib2/drawHub/expressway rg.ttf",100)
def Gabung(fun):
    def gabung(arg):
        im,text1=arg[0],arg[1]
        op=Image.new("RGB",(40,20),color=(0,0,0))
        draw=ImageDraw.Draw(op)
        size=font.getsize(text1)
        baru=Image.new("RGB",(im.width+size[0]+210+20+130,600), color=(0,0,0))
        draw=ImageDraw.Draw(baru)
        draw.text((150,250), text1,(255,255,255),font=font)
        baru.paste(im, (150+size[0]+20,230+10))
        return baru
    return gabung(fun)
def orange(text1, text2):
    panjangText=font.getsize(text2)
    oren=Image.new("RGBA",(panjangText[0]+20,140),color=(240, 152, 0))
    draw=ImageDraw.Draw(oren)
    draw.text((10,int((oren.height-panjangText[1])/2)-10),text2, (0,0,0),font=font)
    return Gabung([oren, text1])