import re, requests
def pinterest(url):
    m=requests.get(url)
    if re.search("https://v.pinimg.com/videos/mc/(.*?).mp4",m.text):
        if '"' in re.search("https://v.pinimg.com/videos/mc/(.*?).mp4",m.text)[0]:
            return re.search("https://i.pinimg.com/originals/(.*?)\" as\=\"image\"",m.text)[0][:-12]
        else:
            return re.search("https://v.pinimg.com/videos/mc/(.*?).mp4",m.text)[0]
    elif re.search("https://i.pinimg.com/originals/(.*?)\" as\=\"image\"",m.text):
        return re.search("https://i.pinimg.com/originals/(.*?)\" as\=\"image\"",m.text)[0][:-12]
    else:
        ''