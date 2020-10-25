import json
class Change:
    def __init__(self,idGrup, nomer=None,switchInt=0, maxint=0,nsfw=0):
        self.grupID = idGrup
        self.nomer = nomer
        self.switchV = switchInt
        self.maxint = maxint
        self.data = json.loads(open("data/toxic.json","r").read())
        self.nsfw = nsfw
    def Tambah(self):
        for i in self.data:
            if i.get("idGrup") == self.grupID:
                for enum in i.get("alert"):
                    if enum.get("number") == self.nomer:
                        enum.update({"count":enum.get("count")+1})
                        break
                else:
                    i["alert"].append({
                    "number":self.nomer,
                    "count":0
                    })
        open("data/toxic.json","w").write(json.dumps(self.data,indent=4))
    def switchEdit(self):
        for i in self.data:
            if i.get("idGrup") == self.grupID:
                i.update({"Switch":self.switchV})
                if self.maxint:
                    i.update({"alert":[]})
                    i.update({"maxCount":self.maxint})
                break
        else:
            self.data.append({
            "idGrup":self.grupID,
            "Switch":self.switchV,
            "NSFW":self.nsfw,
            "maxCount":self.maxint,
            "alert":[]
        })
        open("data/toxic.json","w").write(json.dumps(self.data,indent=4))
    def nsfwEdit(self):
        for i in self.data:
            if i.get("idGrup") == self.grupID:
                i.update({"NSFW":self.nsfw})
                break
        open("data/toxic.json","w").write(json.dumps(self.data,indent=4))
    def nsfwX(self):
        for i in self.data:
            if i.get("idGrup") == self.grupID:
                return i.get("NSFW")
            break
        else:
            return 0
    def MaxEdit(self):
        for i in self.data:
            if i.get("idGrup") == self.idGrup:
                i.update({"maxCount":self.maxint})
                open("data/toxic.json").write(json.dumps(data, indent=4))
    def count(self):
        for i in self.data:
            if i.get("idGrup") == self.grupID:
                for enum in i.get("alert"):
                    if enum.get("number") == self.nomer:
                        return enum.get("count")
                else:
                    return 0
    def switch(self):
        for i in self.data:
            if i.get("idGrup") == self.grupID:
                return i.get("Switch")
        else:
            return 0
    def idGrup(self):
        for i in self.data:
            if i.get("idGrup") == self.grupID:
                return True
        else:
            return False
    def maxCount(self):
        for i in self.data:
            if i.get("idGrup") == self.grupID:
                return i.get("maxCount")
        else:
            return 0
