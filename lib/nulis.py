from PIL import Image, ImageDraw, ImageFont
def tulis(text):
    '''
    text : string
    '''
    img, font, kata, tempkata=Image.open("lib/before.jpg"), ImageFont.truetype("lib/IndieFlower.ttf",24),'',''
    draw=ImageDraw.Draw(img)
    for i in text:
        if draw.textsize(tempkata, font)[0] < 734:
            tempkata+=i
        else:
            kata, tempkata=kata+'%s\n'%tempkata, i
    if tempkata:
        kata+="%s"%tempkata
    spliter=kata.split("\n")
    line=190
    for i in spliter:
        draw.text((170, int(line)), i, font=font, fill=(0, 0, 0)) #selisih = Line
        line+=37 + 0.9
    return img