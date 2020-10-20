'''
@Author  : MhankBarBar
@Github  : https://github.com/MhankBarBar
'''
from requests import *
from googlesearch import *
from urllib.parse import *
from bs4 import BeautifulSoup as bs
def cari(url):
	try:
		req=get(url).text
		bes=bs(req, 'html.parser')
		a=bes.find('div', class_='spe').text
		b=bes.find('div', class_='entry-content entry-content-single').select('p')
		desc = b[0].text.replace('& quot;','&').replace('& Quot;','&').replace('& mdash;','&')
		descc = b[1].text.replace('& quot;','&').replace('& Quot;','')
		c=bes.find('div', class_='boxdl')
		d=c.select('a')
		e = []
		g = ''.join(e)
		for i in d:
			x = i.attrs['href']
			e.append(x)

		hasil=f'Sinopsis : {desc}{descc}{c.text}'
		hasil+=f'[360p]\n{e[0]}\n{e[1]}\n{e[2]}\n{e[3]}\n\n\n[480p]\n{e[4]}\n{e[5]}\n{e[6]}\n{e[7]}\n\n\n[720p]\n{e[8]}\n{e[9]}\n{e[10]}\n{e[11]}\n\n\n[1080p]\n{e[12]}\n{e[13]}\n{e[14]}\n{e[15]}\n'+g if '240p -' in c.text else f'[240p]\n{e[0]}\n{e[1]}\n{e[2]}\n{e[3]}\n\n\n[360p]\n{e[4]}\n{e[5]}\n{e[6]}\n{e[7]}\n\n\n[480p]\n{e[8]}\n{e[9]}\n{e[10]}\n{e[11]}\n\n\n[720p]\n{e[12]}\n{e[13]}\n{e[14]}\n{e[15]}'
		return {
			'cover':bes.find_all('div',itemprop='image')[0].find_all('img',itemprop='image')[0]['src'],
			'result':hasil,
			'a':a
		}
	except Exception as e:return(f'Error : {e}\n\nanime tidak di temukan')