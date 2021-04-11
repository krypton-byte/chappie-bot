from luxand import luxand
import requests
def detect(url=""):
    client = luxand("d20a6a91b6954e27a033d2361243b492")
    detect = client.detect(url)
    celeb  = client.celebrity(photo=url)["result"]
    emot   = client.emotions(photo=url)
    Fmin=min([len(detect), len(emot)])
    data=""
    for i in range(Fmin):
        expr=""
        for xx in emot[i]["emotions"].keys():
            expr+="\n\t%s : %s"%(xx, emot[i]["emotions"][xx])
        data+=f"""
Nama : { celeb[i].get("name") if len(celeb) > i else getName(url) } 
Selebriti : { "Ya" if len(celeb) else "Tidak"}
Gender: {detect[i].get("gender",{"gender":{"value":"Tidak Di Ketahui"}} if len(detect) >i else {"value":"Tidak Di Ketahui"}).get("value")}
Umur : {int(detect[i].get("age")) if len(detect) >= 1 else "Tidak Di Ketahui"}
Kelompok Usia : {detect[i].get("age_group","Tidak Di Ketahui") if len(detect) >i else "Tidak Di Ketahui"}
Emosi : {expr}
        """
    return data.strip()

def getName(urlImage):
    url = "https://api.luxand.cloud/photo/search"
    headers = { 'token': "" }
    response = requests.post(url, data={"photo":urlImage}, headers=headers)
    return ",".join([i.get("name") for i in response.json()])
