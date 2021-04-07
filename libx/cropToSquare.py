'''
@Module Chappie [BOT]
'''
from lib2 import stickerExif
from PIL import Image
def crop_image(image):
    '''
    resize image resolution ratio 1:1
    fn : filename (*.jpg, *.png etc)
    '''
    width, height = image.size
    if width == height:
        return image
    offset  = int(abs(height-width)/2)
    if width>height:
        image = image.crop([offset,0,width-offset,height])
    else:
        image = image.crop([0,offset,width,height-offset])
    return image
def patternRes(x,y):
    if x==y:
        return [512, 512]
    elif x>y:
        return [512,int(y/(x/512))]
    elif x<y:
        return  [int(x/(y/512)),512]
def patternResCustom(x, y, res=1280):
    if x==y:
        return [res, res]
    elif x>y:
        return [res,int(y/(x/res))]
    elif x<y:
        return  [int(x/(y/res)),res]
def resizeTo(fn):
    '''
    fn : filename (*.jpg, *.png etc)
    resize: 512x512
    '''
    img=Image.open(fn)
    if img.width == img.height:
        width, height = 512, 512
    elif img.width > img.height:
        width = 512
        height = img.height/(img.width/width)
    elif img.width < img.height:
        height = 512
        width = img.width/(img.height/height)
    return img.resize((int(width), int(height)))
def pasteLayer(fn, packname="Krypton-Bot"):
    '''
    fn : filename (*.jpg, *.png etc..)
    '''
    img=resizeTo(fn)
    polosan=Image.new("RGBA", (512, 512), color=(0, 0, 0, 0))
    polosan.paste(img, (256-(int(img.width/2)), 256-(int(img.height/2))))
    polosan.save(fn+".webp", exif=stickerExif(packname=packname))