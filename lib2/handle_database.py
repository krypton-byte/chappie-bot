
from datetime import datetime
from io import BytesIO
import random
import socketio
import requests
from setting import server
from openwa.helper import convert_to_base64
from threading import Thread
import base64
import time
start=time.time()
grup_json=requests.get(f"{server}/AllInfoGrup/").json()["result"]
user_json=requests.get(f"{server}/allUser/").json()["result"]
Client = socketio.Client()
Client.connect(server, namespaces=["/grup","/GrupBot","/bot","/user","/bc"])
def driver_(drive):
    global driver
    driver=drive
    return True
@Client.on("cmd", namespace="/bot")
def comm(data):
    from_bot=data.get("from_bot")
    from_id = data.get("from_id")
    cmd = data.get("cmd","None")
    if not from_bot == driver.wapi_functions.getMe()["wid"] and data.get("type") == "request":
        print(data)
        d=driver.wapi_functions.getMe()
        if cmd == "activate_bot":
            date=time.time()-start
            pesan=f"""
╭────「 *BOT INFO* 」──────
│ *Name*   : {d['pushname']}
│ *WA*     : https://wa.me/{d['wid'][:-5]}
│ *Runtime* : {int(date//3600)}:{int(date%3600//60)}:{int(date%60)}
│ *Status* : ONLINE
╰────────────────────
""".strip()
            data_={"pesan":pesan, "type":"response", "from_bot":from_bot, "from_id":from_id}
            if (profile:=driver.get_profile_pic_from_id(d["wid"])):
                data_.update({"media":base64.b64encode(profile).decode()})
                print(data_)
            Client.emit("broadcast", data=data_ , namespace="/bc")
    if cmd.split()[0] == "gbroadcast":
        for i in driver.get_all_chat_ids():
            Thread(target=driver.wapi_functions.sendMessage, args=(i,cmd[len(cmd.split()[0])+1:],)).start()
    if from_bot == driver.wapi_functions.getMe()["wid"] and data.get("type") == "response":
        if data.get("media"):
            driver.wapi_functions.sendImage(convert_to_base64(BytesIO(base64.b64decode(data["media"].encode()))), from_id, "bs.jpg",data["pesan"])
        else:
            driver.wapi_functions.sendMessage(from_id, data["pesan"])
def broadcast_serv(chat_id, cmd):
    Client.emit("broadcast", data={"cmd":cmd, "from_bot":driver.wapi_functions.getMe()["wid"], "from_id":chat_id, "type":"request"} ,namespace="/bc")
@Client.on("UserBot", namespace="/bot")
def updateDbUser(data):
    global user_json
    if data.get("from_bot") == driver.wapi_functions.getMe()["wid"]:
        driver.wapi_functions.sendMessage(data.get("from_id"), "Successfully added to database")
    data.pop("from_bot")
    data.pop("from_id")
    if (res:=list(filter(lambda x:x[1]["chat_id"]==data.get("chat_id"), enumerate(user_json)))):
        user_json[res[0][0]] = data
    else:
        user_json.append(data) 
@Client.on("GrupBot", namespace="/bot")
def updateDB(data):
    global grup_json
    if data.get("from_bot") == driver.wapi_functions.getMe()["wid"] if driver else "Wuih":
        driver.wapi_functions.sendMessage(data.get("chat_id"),"group updated successfully")
    data.pop("from_bot")
    if (res:=list(filter(lambda x:x[0] if x[1]["chat_id"]==data.get("chat_id") else None, enumerate(grup_json)))):
        grup_json[res[0][0]] = data
    else:
        grup_json.append(data)
def set_user(**kwargs):
    Client.emit("user", data=kwargs, namespace="/user")
def CariData(chat_id):
    if (res:=list(filter(lambda x:x[0] if x[1]["chat_id"]==chat_id else None, enumerate(grup_json)))):
        return grup_json[res[0][0]]
    else:
        return {"nama_grup":None, "chat_id":chat_id, "prefix":"!", "nsfw":0, "AntiToxic":0}
def SocketGrupUpdate(**kwargs):
    if kwargs.get("chat_id"):
        if (result:=CariData(kwargs.get("chat_id"))):
            result.update(kwargs)
            Client.emit("update", data=result, namespace="/grup")
        else:
            True
    else:
        print("Invalid Update")

def get_prefix(chat_id):
    return CariData(chat_id=chat_id).get("prefix")

def get_nsfw(chat_id):
    return int(CariData(chat_id=chat_id).get("nsfw",0))

def get_AntiToxic(chat_id):
    return int(CariData(chat_id=chat_id).get("AntiToxic",0))

def set_prefix(chat_id, prefix, nama_grup, from_bot):          
    SocketGrupUpdate(chat_id=chat_id, prefix=prefix, nama_grup=nama_grup, from_bot=from_bot)
    return True

def set_nsfw(chat_id, nsfw, nama_grup, from_bot):
    SocketGrupUpdate(chat_id=chat_id, nsfw=nsfw, nama_grup=nama_grup, from_bot=from_bot)
    return True

def set_AntiToxic(chat_id, AntiToxic, nama_grup, from_bot):
    SocketGrupUpdate(chat_id=chat_id, AntiToxic=AntiToxic, nama_grup=nama_grup, from_bot=from_bot)
    return True
def get_female():
    return random.choice(list(filter(lambda x:x if x["gender"]=="female" else None, user_json)))
def get_male():
    return random.choice(list(filter(lambda x:x if x["gender"]=="male" else None, user_json)))
def isUsers(chat_id):
    return list(filter(lambda x:x if x["chat_id"]==chat_id else None, user_json))