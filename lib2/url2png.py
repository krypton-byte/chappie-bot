import imgkit
from io import BytesIO
import subprocess
def url2png(url: str) -> dict:
    try:
        return {"ss":BytesIO(imgkit.from_url(url,False))}
    except Exception as e:
        print(f"Error -> {str(e)}")
        return {}

def img2ascii(file):
    ascii_=subprocess.Popen(["jp2a", "--colors", "--fill", f"--width=200", "--html", file], stdout=subprocess.PIPE).stdout.read().decode()
    return BytesIO(imgkit.from_string(ascii_,False))
def eight_bit(file):
    ascii_=subprocess.Popen(["jp2a", "--colors", "--fill", f"--width=200", "--html","--chars='   '", file], stdout=subprocess.PIPE).stdout.read().decode()
    return BytesIO(imgkit.from_string(ascii_,False))