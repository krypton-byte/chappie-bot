 
from PIL import Image, ImageDraw, ImageFont
def desain(fn,katakata,author,col=(255,255,255)):
    img=Image.open(fn)
    widthImage=img.width
    heightImage=img.height
    kata='“%s”'%katakata
    kata2=''
    x=0
    fonMax=[]
    draw=ImageDraw.Draw(img)
    font=ImageFont.truetype('lib2/amertha.ttf',int(widthImage/28))
    maksWidthText=widthImage
    for i in kata:
        dra=draw.textsize(i, font)
        fonMax.append(dra[1])
        if x > maksWidthText:
            kata2+='\n%s'%(i)
            x=0
        else:
            kata2+=i
        x+=dra[0]
    print((x, maksWidthText))
    FM=max(fonMax)
    heightFm=0
    arr=kata2.split('\n')
    arr.append('')
    arr.append('')
    arr.append(author)
    for i in arr:
        length=draw.textsize(i, font)
        width=(widthImage/2)-(length[0]/2)
        height=(heightImage/3)-(length[1]/2)
        heightFm+=FM/3
        draw.text((width, height+heightFm), i, align='center', font=font, fill=col)
        print((width, height))
    img.save(fn)