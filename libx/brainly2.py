import requests, re
from urllib.parse import quote
from bs4 import BeautifulSoup
def gsearch(query):
    '''
    query : String
    '''
    src = requests.get("https://www.google.com/search?q="+quote(query)).text
    return re.findall('<a href="/url\?q\=(.*?)\&amp;',src)
def brainly(url):
    try:
        get=requests.get(url, headers={'user-agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4183.102 Safari/537.36"})
        bs=BeautifulSoup(get.text,'html.parser')
        pertanyaan=bs.find_all('span',class_='sg-text sg-text--large sg-text--bold sg-text--break-words brn-qpage-next-question-box-content__primary')[0].text
        jawab=bs.find_all("div",attrs={"data-test":"answer-box-text"})
        jawaban=f"*Pertanyaan:*\n    {pertanyaan.strip()}\n"
        komen=[]
        for i in bs.find_all("ul",attrs={"class":"brn-qpage-next-comments__list"}):
            komen.append(">    "+"\n>    ".join([ (o.text.strip()) for o in i("div",attrs={"class":"sg-text sg-text--small sg-text--break-words"})]))
        for i in enumerate(jawab,1):
            t=BeautifulSoup(str(i[1]).replace("*"," * ").replace("<strong>"," *").replace(" </strong>","* ").replace("</strong>","* "),'html.parser').text.strip()
            jawaban+=f"*Jawaban {i[0]}:*\n    {t}\n"
            jawaban+=f"*Komentar*:\n{komen[i[0]-1] if (i[0]) <=len(komen) else ''}\n"
        return jawaban
    except Exception as e:
        print(f"Error -> {str(e)}")
        return "*Pertanyaan: Tidak Di Temukan*"

