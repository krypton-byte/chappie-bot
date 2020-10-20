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
    headers={'user-agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36"}
    get=requests.get(url, headers=headers)
    bs=BeautifulSoup(get.text,'html.parser')
    Tangg=bs.find_all('span',class_='sg-text sg-text--xsmall sg-text--gray-secondary')[0]('time')[0]['title']
    angkatan=bs.find_all('span',itemprop='name',class_='sg-text sg-text--xsmall sg-text--gray-secondary sg-text--link')[1].text
    mapel=bs.find_all('span',itemprop='name',class_='sg-text sg-text--xsmall sg-text--gray-secondary sg-text--link')[0].text
    answer=[]
    pertanyaan=bs.find_all('span',class_='sg-text sg-text--large sg-text--bold sg-text--break-words brn-qpage-next-question-box-content__primary')[0].text
    for jawaban in bs.find_all('div',class_='sg-text sg-text--break-words brn-rich-content js-answer-content'):
        answer.append(jawaban.text)
    return {
        'soal':pertanyaan,
        'angkatan':angkatan,
        'mapel':mapel,
        'tanggal':Tangg,
        'jawaban':answer
        }