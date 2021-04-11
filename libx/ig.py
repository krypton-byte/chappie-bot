import requests, datetime, re
def Unix():
    dt = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
    timestamp = dt.replace(tzinfo=datetime.timezone.utc).timestamp()
    # print(timestamp)
    return timestamp

def InstaLogin(user, password):
    rHeaders= {"Accept": "*/*" , "Accept-Language": "ar,en-US;q=0.7,en;q=0.3" , "Content-Type": "application/x-www-form-urlencoded", "Cookie": "Y1z1n" , "Host": "www.instagram.com" , "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0" , "X-CSRFToken": "Y1z1n", "X-IG-App-ID": "936619743392459" , "X-Instagram-AJAX": "Y1z1n", "X-Requested-With": "XMLHttpRequest"}
    rData = {"username": user, "enc_password": "#PWD_INSTAGRAM_BROWSER:0:" + str(Unix())[:-4]+ ":"+password, "queryParams": "{}" , "optIntoOneTap": "false"}
    r = requests.post("https://www.instagram.com/accounts/login/ajax/" ,  headers=rHeaders , data=rData, verify=False)
    res = r.json()
    print(res)
    if "userId" in res:
        #print("Done login :)")
        csrf = str(r.headers)
        full_cookies = "".join(re.findall(r'csrftoken=.*?;', csrf)) +   "".join(re.findall(r'ds_user_id=.*?;', csrf)) + "".join(re.findall(r'ig_did=.*?;', csrf))  + "".join(re.findall(r'mid=.*?;', csrf)) + "".join(re.findall(r'rur=.*?;', csrf)) + "".join(re.findall(r'sessionid=.*?;', csrf)) + "".join(re.findall(r'shbid=.*?;', csrf)) + "".join(re.findall(r'shbts=.*?;', csrf))
        print(full_cookies)
        return full_cookies
    else:
        print("Wrong username or password, or a banned account")
        return ""

def igdownload(url):
    global token
    req=requests.get(url, params={"__a":1},headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36","Cookie":kuki})
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
    global token
    stalk=requests.get(f"https://www.instagram.com/{user}/",params={"__a":1},headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36","Cookie":kuki}).json()
    userProperty=stalk["graphql"]["user"]
    return {
        "pic":userProperty["profile_pic_url_hd"],
        "username":userProperty["username"],
        "follower":userProperty["edge_followed_by"]["count"],
        "following":userProperty["edge_follow"]["count"],
        "bio":userProperty["biography"],
        "post":userProperty["edge_owner_to_timeline_media"]["count"]

    }

#kuki=InstaLogin("frisall_","frisal3108")
kuki='csrftoken=2nRbk1oUAQTMJdFmPGlwlGdo0fbTKWw2;ds_user_id=8547754873;ig_did=D0C03879-9BB8-42CC-B141-BCC94C2A0F96;mid=YCfLZQALAAGHt2mPJF-NIAIUeG-7;rur=ATN;sessionid=8547754873%3AL5VaJHO0uUbzVp%3A0;'