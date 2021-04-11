import requests
def findSurah(surah: str, ayat: str):
    try:
        hasil=''
        z=requests.get(f"https://api.banghasan.com/quran/format/json/surat/{surah}/ayat/{ayat}").json()
        if z["status"] =="ok":
            hasil+=f"""
    Nomer Surat: {z['surat']['nomor']}
    Asma : {z['surat']['asma']}
    Nama Surat :{z['surat']['nama']}
    Arti Surat : {z['surat']['arti']}
    Jumlah Ayat : {z['surat']['ayat']}
    Diturunkan: Di {z['surat']['type']}
    """
            if z["ayat"].get("data"):
                for i in range(len(z["ayat"]["proses"])):
                    hasil+=f"""
    Ayat: {z['ayat']['data']['ar'][i]['ayat']}
    Arab: {z['ayat']['data']['ar'][i]['teks']}
    Arti: {z['ayat']['data']['id'][i]['teks']}
                    """
                return hasil.strip()
            else:
                hasil+="Ayat Tidak Di Temukan\n"
                return hasil
        else:
            print(z)
            return z["pesan"]
    except:
        return "Masukan Nomer Surat Dan Nomer Ayat"