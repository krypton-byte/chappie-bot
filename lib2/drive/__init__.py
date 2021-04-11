from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import time
import base64
gauth = GoogleAuth()
gauth.LoadCredentialsFile("assets/gdriveToken.txt")
drive = GoogleDrive(gauth)
parents="1BpUoZ4VS8_U_2FJPkLe-vGyH_n_cK2sR"
def upload(file_, ext="webp"):
    file=drive.CreateFile({"title":time.time().__str__()+"."+ext, "parents":[{"id":parents}]})
    file.SetContentFile(file_)
    file.Upload()
    return file
def downloadDrive(id_, fn):
    file=drive.CreateFile({"id":id_})
    file.GetContentFile(fn)
    