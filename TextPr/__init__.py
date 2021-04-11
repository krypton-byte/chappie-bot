from requests import Session
from bs4 import BeautifulSoup as bs
from json import loads
r = Session()
headers = {'user-agent': 'Googlebot'}
class tp:
    def __init__(self):
        self.BaseUrl = 'https://textpro.me{}'
        self.pack = loads(open('TextPr/theme.json').read())
    def img(self, pack, Text):
        return {
            "result":"https://i.ibb.co/52kR6M2/textprome-1606dd4c4bb2ac.jpg"
        }