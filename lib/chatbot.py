import random
class chatBot:
    '''input chat e.g chatbot("Hi")'''
    def __init__(self, req):
        self.req = req.lower().split()
        self.list_ask = ["aku","sayang","kamu"]
        self.balas_ask = ["same",":)","kamu bilang apa"]
        self.list_odading = ["hiu","tomat"]
        self.list_intro = ["hi","hai","hello","hai","p","bro","halo","hallo","helo"]
        self.balas_intro = ["iya","ada apa gan","ya hallo","ada apaan gan","Ya"]
        self.list_rumah = ["dimana","rumah","kamu","tempat","tinggal","daerah","di","mana"];
        self.balas_rumah = ["Jawa Barat","jawa Tengah","Jawa Timur"]
        self.list_nama = ["siapa","nama","kamu","namanya"]
        self.balas_nama = ["nama saya chappie","nama saya chappie atau bisa di sebut Bot whatsapp"]
        self.list_author = ["siapa","author","pembuat","pencipta","menciptakan","kamu"]
        self.balas_author = ["Ntah","saya Tidak Tahu"]
        self.list_salam = ["assalamu'alaikum","asalamualaikum"]
        self.balas_salam = ["wa'alaikumsalam","Wa'alaikumsalam"]
        self.list_fav_makanan = ["makanan","favorit","kesukaan"]
        self.balas_fav_makanan = ["Nasi Goreng","Telur Ceplok","Mie Goreng"]
    def max_(self):
        self.rumah = len(set(self.list_rumah) & set(self.req))
        self.nama = len(set(self.list_nama) & set(self.req))
        self.author = len(set(self.list_author) & set(self.req))
        self.salam = len(set(self.list_salam) & set(self.req))
        self.intro = len(set(self.list_intro) & set(self.req))
        self.fav_makanan = len(set(self.list_fav_makanan) & set(self.req))
        self.ask = len(set(self.list_ask) & set(self.req))
        self.odading = len(set(self.list_odading) & set(self.req))
        self.list=[self.rumah, self.nama, self.author, self.salam, self.fav_makanan, self.intro, self.ask, self.odading]
    def balas(self):
        maks=max(self.list)
        if 'bot' in self.req and set(['goblok','tolol'])&set(self.req):
            return random.choice(["yg main bot gk ada akhlak","nama nya juga bot","aku ini bukan bot sepeti ML (machine learning) yg bisa di ajarin"])
        elif maks == 0:
            return False
        elif self.rumah == maks:
            return random.choice(self.balas_rumah)
        elif self.nama == maks:
            return random.choice(self.balas_nama)
        elif self.author == maks:
            return random.choice(self.balas_author)
        elif self.salam == maks:
            return random.choice(self.balas_salam)
        elif self.fav_makanan == maks:
            return random.choice(self.balas_fav_makanan)
        elif self.intro == maks:
            return random.choice(self.balas_intro)
        elif self.ask == maks:
            return random.choice(self.balas_ask)
        elif self.odading == maks:
            return "Goblok !!!"

        