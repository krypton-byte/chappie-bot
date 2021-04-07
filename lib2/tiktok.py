from requests import Session
from bs4 import BeautifulSoup
import re

class tiktok:
    def __init__(self) -> None:
        self.request = Session()
        self.url     = "https://ssstik.io"
        self.html    = self.request.get(self.url).text
        self.key     = BeautifulSoup(self.html, "html.parser").find_all("form",attrs={"data-hx-target":"#target"})[0].get("include-vals")
        self.post    = BeautifulSoup(self.html, "html.parser").find_all("form",attrs={"data-hx-target":"#target"})[0].get("data-hx-post")
        self.tt      = re.search("tt\:\'(.*?)\'",self.key)[1]
        self.ts      = re.search("ts\:([0-9]{5,15})",self.key)[1]
        self.header  = {"content-type": "application/x-www-form-urlencoded; charset=UTF-8","hx-active-element": "submit","hx-current-url": "https://ssstik.io/","hx-request": "true","hx-target": "target","origin": "https://ssstik.io","sec-fetch-dest": "","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
    def download(self, url) -> dict:
        data   = {"id": url,"locale": "en","tt": self.tt,"ts": int(self.ts)}
        post   = self.request.post(f"{self.url}{self.post}", headers=self.header, data=data)
        respon = BeautifulSoup(post.text, "html.parser")
        hasil  = {"video":[f'{self.url}{respon.find_all("a",class_="pure-button pure-button-primary is-center u-bl dl-button download_link without_watermark")[0].get("href")}',f'{self.url}{respon.find_all("a",class_="pure-button pure-button-primary is-center u-bl dl-button download_link without_watermark_direct")[0].get("href")}'],"music":f'{respon.find_all("a",class_="pure-button pure-button-primary is-center u-bl dl-button download_link music")[0].get("href")}'}
        return hasil
class tiktok2:
    def __init__(self, url) -> None:
        self.request = Session()
        self.url =url
        self.header  = {"accept": "*/*","accept-language": "en-US,en;q=0.9,id;q=0.8","origin": "https://snaptik.app","referer": "https://snaptik.app/ID","sec-fetch-dest": None,"sec-fetch-mode": "cors","sec-fetch-site": "same-origin","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",}
    def download(self):
        self.request.post("https://snaptik.app/check_token.php", headers=self.header)
        self.bs = BeautifulSoup(self.request.post("https://snaptik.app/action-2021.php", headers=self.header, data={"url":self.url}).text, "html.parser")
        return [self.request,{"title":self.bs('a', attrs={"title":""})[0].text,"date":self.bs("b", attrs={"class":"blur"})[0].text,"url":list(filter(lambda x:x, map(lambda x:x["href"] if "token" in x["href"] else None, self.bs("a", attrs={"class":"abutton is-success is-fullwidth"}))))}, self.header]