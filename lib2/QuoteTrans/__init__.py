from PIL import Image, ImageDraw, ImageFont

def QuoteTrans(quote: str, color=(255, 255, 255), border=(0, 0, 0)):
    img=Image.new("RGBA", (512, 512), color=(0,0,0,0))
    font=ImageFont.truetype("lib2/QuoteTrans/impact.ttf", int(img.width/7))
    draw=ImageDraw.Draw(img)
    kata=temp=""
    for xy in quote.split("\n"):
        for i in xy:
            if font.getsize(temp)[0] > img.size[0]-img.width/11:
                kata+=temp+"\n"
                temp=i
            else:
                temp+=i
        kata+=temp+"\n"
        temp=""
    TinggiText=[(font.getsize(i)[1])for i in temp.split("\n")[:4]]
    jum=sum(TinggiText)+len(kata.split("\n"))*80
    awal=(img.height/2)-(jum/2)
    outlineRange = int(font.size/15)
    for i in kata.split("\n"):
        for x in range(-outlineRange, outlineRange+1):
            for y in range(-outlineRange, outlineRange+1):
                draw.text(
                (int(img.width/2)-(font.getsize(i)[0]/2)+x, awal+y),
                i,  fill=border, font=font)
        draw.text(
            (int(img.width/2)-(font.getsize(i)[0]/2), awal),
             i, fill=color, font=font)
        awal+=100
    return img
        


