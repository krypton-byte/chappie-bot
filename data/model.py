import json, os
model={"chat_id":"83278",
    "user":[{
        "user_id":"09",
        "alert":1
    }]}
if "toxic.json" not in os.listdir("assets"):
    open("assets/toxic.json","w").write("[]")
def resert_toxic(chat_id):
    if (hasil:=list(filter(lambda id_: id_ if id_[1].get("chat_id") == chat_id else None, enumerate((js:=json.loads(open("assets/toxic.json","r").read())))))):
        js[hasil[0][0]]["user"] = []
        open("assets/toxic.json","w").write(json.dumps(js, indent=4))
def update_toxic(chat_id, user_id, max_):
    if (hasil:=list(filter(lambda id_: id_ if id_[1].get("chat_id") == chat_id else None, enumerate((js:=json.loads(open("assets/toxic.json","r").read())))))):
        print("Mas")
        print(hasil)
        if (cari_user:=list(filter(lambda c_user: c_user if c_user.get("user_id")==user_id else None, (chat_db:=hasil[0][1].get("user",[]))))):
            print("user ada")
            js[hasil[0][0]]["user"].remove(chat_db[0])
            data_user=cari_user[0]
            data_user["alert"]+=1
            print(data_user)
            if data_user["alert"] > max_:
                open("assets/toxic.json","w").write(json.dumps(js, indent=4))
                return "kick"
            else:
                js[hasil[0][0]]["user"].append(data_user)
                open("assets/toxic.json","w").write(json.dumps(js, indent=4))
                return data_user["alert"]
        else:
            print(chat_db)
            print(cari_user)
            js[hasil[0][0]]["user"].append({"user_id":user_id, "alert":1})
            open("assets/toxic.json","w").write(json.dumps(js, indent=4))
            print("User Tidak Ada")
            return 1
    elif hasil:
        print("User Belum ada sama sekali")
        js[hasil[0][0]]["user"].append({"user_id":user_id, "alert":1})
        open("assets/toxic.json","w").write(json.dumps(js, indent=4))
        return 1
    else:
        print("GC BARU TERDAFTAR")
        js.append({"chat_id":chat_id, "user":[{"user_id":user_id, "alert":1}]})
        open("assets/toxic.json","w").write(json.dumps(js, indent=4))
        return 1