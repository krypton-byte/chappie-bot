import requests, re
from bs4 import BeautifulSoup as bs
def twettdownload(url):
    head={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36', 'origin': 'https://twdown.net', 'referer': 'https://twdown.net/', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1'}
    tst=requests.post("https://twdown.net/download.php", headers=head, data={"URL":url})
    if tst.status_code == 200:
        hasil=re.findall("\<a download href\=\"(.*?)\" target\=\"_blank\"",tst.text)
        bsa=bs(tst.text, 'html.parser')
        return {"thumbnail":re.findall('\<img class\="img-thumbnail\" src\=\"(.*?)\"',tst.text)[0] if re.findall('\<img class\="img-thumbnail\" src\=\"(.*?)\"',tst.text) else None, "url":list(map(lambda x:{"res":re.findall("/vid/(.*?)x(.*?)/", x)[0],"url":x}, hasil)),"author":bsa.find('div', attrs={'style':'overflow-wrap: break-word;'}).h4.text, "caption":bsa.find('div', attrs={'style':'overflow-wrap: break-word;'}).p.text}
    else:
        return {}