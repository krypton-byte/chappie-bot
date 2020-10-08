'''
@Module Chappie [BOT]
'''
from PIL import Image
def crop_image(fn):
    '''
    resize image resolution ratio 1:1
    fn : filename (*.jpg, *.png etc)
    '''
    image=Image.open(fn)
    width, height = image.size
    if width == height:
        return image
    offset  = int(abs(height-width)/2)
    if width>height:
        image = image.crop([offset,0,width-offset,height])
    else:
        image = image.crop([0,offset,width,height-offset])
    return image
def resizeTo(fn):
    '''
    fn : filename (*.jpg, *.png etc)
    resize image under resolution 512x512 pixel
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
def pasteLayer(fn):
    '''
    fn : filename (*.jpg, *.png etc..)
    paste image in layer
    '''
    img=resizeTo(fn)
    polosan=Image.new("RGBA", (512, 512), color=(0, 0, 0, 0))
    polosan.paste(img, (256-(int(img.width/2)), 256-(int(img.height/2))))
    polosan.save(fn)