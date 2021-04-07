from requests import get
from moviepy import editor
from concurrent.futures import ThreadPoolExecutor
import re

author     = "Krypton_Byte"
repository = "https://github.com/krypton-byte/pinterest_video"
license    = "MIT License"

class PIN:
    def __init__(self, url: str):
        self.source       = get(url).text
        self.video        = re.findall("(https://v.pinimg.com/videos/mc/hls/.*?.m3u8)",self.source)
        self.dir          = "/".join(self.video[0].split("/")[:-1])
        self.quality      = re.findall("(.*?.m3u8)",get(self.video[0]).text)
        self.info         = get(f"{self.dir}/{self.quality[-1]}").text
        self.infoResAndTS = get(f"{self.dir}/{self.quality[-1]}").text
        self.duration     = sum([int(float(i)) for i in re.findall("#EXTINF:([0-9]{1,9}.[0-9]{0,9})",self.infoResAndTS)])
        self.videoList    = re.findall("(.*?.ts)",self.infoResAndTS)
    def download(self):
        try:
            listOfVideo=[]
            with ThreadPoolExecutor(max_workers=8) as kuli:
                for i in self.videoList:
                    listOfVideo.append(kuli.submit(editor.VideoFileClip,f"{self.dir}/{i}").result())
            return editor.concatenate_videoclips(listOfVideo)
        except Exception:
            return False
    def __repr__(self) -> str:
        return f"duration: {self.duration}"