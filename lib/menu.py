help_={
    'help':'''
-> #cara-penggunaan
-> #help
-> #help alat
-> #help grup
-> #help bot
-> #help hiburan
-> #support
    ''',
    'bot':'''
-> # <q>
    ''',
    'alat':'''
-> #sticker
-> #upimg
-> #ig
-> #fb
-> #cari
-> #qrmaker
-> #qrreader
-> #?
-> #wait
-> #tulis
-> #ocr
-> #url2png
-> #run
-> #doujin
-> #film
-> #kusonime
-> #otakudesu
-> #ts [cc] [text]
-> #tts [cc] [text]
-> #quotemaker
-> #yt2mp3
-> #yt
-> #wiki
''',
    'hiburan':'''
-> #dog
-> #neko
-> #quote
-> #kitsune
-> #gambar
-> # [chat]
-> #joke
-> #waifu
-> #bct [text]
    ''',
    'grup':'''
-> #list-admin
-> #admin
-> #mentionall
-> #unadmin
-> #kick
-> #add
-> #owner
-> #linkgroup
-> #revoke
'''
}

def menu(args):
    if help_.get(args):
        return help_[args]
    else:
        return help_["help"]