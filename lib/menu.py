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
-> #qa Q|A
    ''',
    'alat':'''
-> #sticker
-> #upimg
-> #cari
-> #qrmaker
-> #qrreader
-> #?
-> #wait
-> #ocr
-> #url2png
-> #run
-> #doujin
-> #film
-> #nime
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