import requests, re, random
from urllib.parse import quote
from bs4 import BeautifulSoup
def gsearch(query):
    '''
    query : String
    '''
    src = requests.get("https://www.google.com/search?q="+quote(query)).text
    return re.findall('<a href="/url\?q\=(.*?)\&amp;',src)
def brainly(url):
    '''
    url : string
    e.g brainly("https://brainly.co.id/tugas/2754169")
    '''
    headers={'user-agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4183.102 Safari/537.36"}
    get=requests.get(url, headers=headers)
    bs=BeautifulSoup(get.text,'html.parser')
    answer=""
    pertanyaan=bs.find_all('span',class_='sg-text sg-text--large sg-text--bold sg-text--break-words brn-qpage-next-question-box-content__primary')[0].text
    for jw in bs.find_all("div", class_="sg-text sg-text--break-words brn-rich-content js-answer-content"):
        for jawaban in jw.find_all("p"):
            answer+="\n%s"%jawaban.text
    return {
        'soal':pertanyaan,
        'jawaban':answer.strip()
        }
