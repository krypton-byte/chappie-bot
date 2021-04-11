from PIL import ImageDraw, ImageFont, Image
import os
output=[]
def tulis(text):
    '''
    text : string
    '''
    img, font, kata, tempkata=Image.open(os.path.abspath("assets/before.jpg")), ImageFont.truetype("assets/IndieFlower.ttf",24),'',''
    draw=ImageDraw.Draw(img)
    if type(text) is not list:
        global output
        output=[]
        for i in text:
            if draw.textsize(tempkata, font)[0] < 734:
                tempkata+=i
            else:
                kata, tempkata=kata+'%s\n'%tempkata, i
        if tempkata:
            kata+="%s"%tempkata
        spliter=kata.split("\n")
    else:
        spliter=text
    line=190
    for i in spliter[:25]:
        draw.text((170, int(line)), i, font=font, fill=(0, 0, 0)) #selisih = Line
        line+=37 + 2.2
    output.append(img)
    if len(spliter) > 25:
        tulis(spliter[25:])
    return output