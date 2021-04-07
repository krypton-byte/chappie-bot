import requests
from bs4 import BeautifulSoup
def fun(url):
    '''
    url : String
    '''
    try:
        video=[]
        req=BeautifulSoup(requests.get(url).text,'html.parser')
        for i in req.find_all('ul',class_='enlaces')[1].find_all('li'):
            video.append({
                'url':i.find_all('a')[0]['href'],
                'lewat':i.find_all('span',class_='b')[0].text.replace(' ',''),
                'sub':i.find_all('span',class_='c')[0].text,
                'res':i.find_all('span',class_='d')[0].text

            })
        image=[]
        for i in req.find_all('img',itemprop='image'):
            image.append(i['src'])
        hasil={
            'sinopsis':req.find_all('p')[5].text,
            'video':video,
            'status':True,
            'cover':image[0],
            'gambar':image,
            'rating':req.find_all('span',itemprop='ratingValue')[0].text,
            'title':req.title.text[:-14]
        }
        return hasil
    except:
        return{
            'status':False
        }