"""
@author : Krypton Byte
"""
import requests
def igdownload(url):
    req=requests.get(url, params={"__a":1})
    if ('graphql' in req.text):
        media=req.json()["graphql"]["shortcode_media"]
        if media.get("is_video"):
            return {"status": True,"result":[{"type":"video", "url":media["video_url"]}]}
        elif media.get("edge_sidecar_to_children"): #multiple media
            med={"status":True, "result":[]}
            for i in media["edge_sidecar_to_children"]["edges"]:
                med["result"].append( {"type":"video","url":i["node"]["video_url"]} if i["node"]["is_video"] else {"type":"image","url":i["node"]["display_resources"][-1]["src"]})
            return med
        else: #1 media
            return {"status":True,"result":[{"type":"image","url":media["display_resources"][-1]["src"]}]}
    else:
        return {"status":False}
def igstalker(user):
    stalk=requests.get(f"https://www.instagram.com/{user}/",params={"__a":1}).json()
    if stalk:
        userProperty=stalk["graphql"]["user"]
        return {
            "pic":userProperty["profile_pic_url_hd"],
            "username":userProperty["username"],
            "follower":userProperty["edge_followed_by"]["count"],
            "following":userProperty["edge_follow"]["count"],
            "bio":userProperty["biography"],
            "post":userProperty["edge_owner_to_timeline_media"]["count"]

        }
    else:
        return {}
