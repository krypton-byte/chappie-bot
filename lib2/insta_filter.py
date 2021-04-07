import pilgram
from PIL import Image
from io import BytesIO
def instagram_filter(im, filter_):
    buffer = BytesIO()
    im=Image.open(im)
    filter_=filter_.lower()
    if filter_ == "_1977":
        pilgram._1977(im).save(buffer, format="png")
    elif filter_ == "aden":
        pilgram.aden(im).save(buffer, format="png")
    elif filter_ == "brannan":
        pilgram.brannan(im).save(buffer, format="png")
    elif filter_ == "brooklyn":
        pilgram.brooklyn(im).save(buffer, format="png")
    elif filter_ == "clarendon":
        pilgram.clarendon(im).save(buffer, format="png")
    elif filter_ == "gingham":
        pilgram.gingham(im).save(buffer, format="png")
    elif filter_ == "hudson":
        pilgram.hudson(im).save(buffer, format="png")
    elif filter_ == "inkwell":
        pilgram.inkwell(im).save(buffer, format="png")
    elif filter_ == "earlybird":
        pilgram.earlybird(im).save(buffer, format="png")
    elif filter_ == "kelvin":
        pilgram.kelvin(im).save(buffer, format="png")
    elif filter_== "lark":
        pilgram.lark(im).save(buffer, format="png")
    elif filter_ == "lofi":
        pilgram.lofi(im).save(buffer, format="png")
    elif filter_ == "maven":
        pilgram.maven(im).save(buffer, format="png")
    elif filter_ == "mayfair":
        pilgram.mayfair(im).save(buffer, format="png")
    elif filter_ == "moon":
        pilgram.moon(im).save(buffer, format="png")
    elif filter_ == "nashville":
        pilgram.nashville(im).save(buffer, format="png")
    elif filter_ == "perpetua":
        pilgram.perpetua(im).save(buffer, format="png")
    elif filter_ == "reyes":
        pilgram.reyes(im).save(buffer, format="png")
    elif filter_ == "rise":
        pilgram.rise(im).save(buffer, format="png")
    elif filter_ == "slumber":
        pilgram.slumber(im).save(buffer, format="png")
    elif filter_ == "stinson":
        pilgram.stinson(im).save(buffer, format="png")
    elif filter_ == "toaster":
        pilgram.toaster(im).save(buffer, format="png")
    elif filter_ == "valencia":
        pilgram.valencia(im).save(buffer, format="png")
    elif filter_ == "walden":
        pilgram.walden(im).save(buffer, format="png")
    elif filter_ == "willow":
        pilgram.willow(im).save(buffer, format="png")
    elif filter_ == "xpro2":
        pilgram.xpro2(im).save(buffer, format="png")
    else:
        return "Nama Filter Belum Tersedia"
    return buffer
