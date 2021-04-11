'''
@Author  : MhankBarBar
@Github  : https://github.com/MhankBarBar
'''
from requests import get
from bs4 import BeautifulSoup as bs
import json
import random

ua = ['Mozilla/5.0 (X11; CrOS x86_64 13310.76.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.108 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 11895.118.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.159 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 12239.92.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.136 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 13099.110.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.136 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 13099.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.127 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 13020.87.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.119 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 12499.66.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.106 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 13310.59.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.84 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 12739.111.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 12607.82.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.123 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 13099.85.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.110 Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 12607.58.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.86 Safari/537.36']
usr_agent = {
	'User-Agent': random.choice(ua)
	}
def search_kusonime(query):
    url = bs(get('https://kusonime.com/?s=%s' % query, headers=usr_agent).text, 'html.parser').find('div', class_='detpost').a['href']
    return url

def search_dewabatch(query):
    url = bs(get('https://dewabatch.com/?s=%s' % query, headers=usr_agent).text, 'html.parser').find('div', class_='dtl').a['href']
    return url

def search_otakudesu(query):
    url = otakudesu = bs(get('https://otakudesu.tv/?s=%s&post_type=anime' % query, headers=usr_agent).text, 'html.parser').find('ul', class_='chivsrc').a['href']
    return url

def scrap_kusonime(url):
    try:
        kuso = bs(get(url).text, 'html.parser')
        title = kuso.find('h1', class_='jdlz').text
        view = kuso.find('span', class_='viewoy').text.strip()
        info = '\n'.join(str(i.text) for i in kuso.find('div', class_='info').findAll('p'))
        sinopsis = '\n'.join(str(kya.text.split('Credit')[0].split('Download')[0].strip()) for kya in kuso.findAll('p')[10:][:5]).rstrip('\n')
        smokedl = kuso.find('div', class_='smokeddl')
        ttl = len(kuso.findAll('div', class_='smokeurl'))
        tmpt_dl = list(u.text for u in smokedl.findAll('a'))
        reso = list(e.text for e in smokedl.findAll('strong'))
        link_dl = list(ntapz['href'] for ntapz in smokedl.findAll('a'))
        result_dl = ''.join(f'{tmpt_dl[o]} {reso[o]} => {link_dl[o]}\n' for o in range(len(reso)))
        thumb = json.loads(kuso.findAll('script')[5].string)['image']['url']
        if 'BD' in title:title = title.split('BD')[0]
        if 'Batch' in title:title = title.split('Batch')[0]
        return {
            'thumb': thumb,
            'info': info,
            'sinopsis': sinopsis,
            'title': title,
            'link_dl': result_dl
        }
    except Exception as e: return {
        'error': e,
        'msg': 'Failed get metadata!'
    }
def scrap_otakudesu(url):
    try:
        otakudesu = bs(get(url).text, 'html.parser')
        title = otakudesu.find('div', class_='jdlrx').text.split('Subtitle')[0]
        sinopsis = otakudesu.find('div', class_='sinopc').text
        info = '\n'.join(str(o.text) for o in otakudesu.find('div', class_='infozingle').findAll('p'))
        thumb = otakudesu.find('img', class_='attachment-post-thumbnail size-post-thumbnail wp-post-image')['src']
        return {
            'thumb': thumb,
            'info': info,
            'sinopsis': sinopsis,
            'title': title
        }
    except Exception as e: return {
        'error': e,
        'msg': 'Failed get metadata'
    }
