import requests, json
def chatbot(question):
    headers = {
       'content-type': 'application/json', 
       'x-api-key': '6iwuT7tMxqd1IdWTLHUnQ6Mhrgr6Ry5R3YBSDWDo'
     }
    data = {
      'utext': question, 
      'lang': 'id',
      'country': ['ID'],
      'atext_bad_prob_max': '0.7'
      }
    req=requests.post("https://wsapi.simsimi.com/190410/talk/",data=json.dumps(data), headers=headers)
    return req.json().get("atext","Simi Lagi Sibuk :)")
