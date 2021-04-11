# create: Krypton-byte
def stickerExif(stickerPackID="kryptonPack", packname="Krypton-Bot", author="Krypton-Byte", googlelink="https://kbyte--api.herokuapp.com", applelink="https://google.com"):
    code  = [0x00,0x00,0x16,0x00,0x00,0x00]
    exif = {"sticker-pack-id": stickerPackID,"sticker-pack-name": packname,"sticker-pack-publisher": author,"android-app-store-link": googlelink,"ios-app-store-link": applelink}
    if (length:=exif.__str__().__len__()) > 256:
        length -=256
        code.insert(0, 0x01)
    else:
        code.insert(0, 0x00)
    return bytes([0x49, 0x49, 0x2A, 0x00, 0x08, 0x00, 0x00, 0x00, 0x01, 0x00, 0x41, 0x57, 0x07, 0x00])+bytes([int("0x0"+hex(length)[2:].__str__() if length < 16 else hex(length)[2:].__str__(), 16)])+bytes(code)+exif.__str__().encode()