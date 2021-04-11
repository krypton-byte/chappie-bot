import requests, json
"""def chatbot(question,token=''):
    headers = {
       'content-type': 'application/json', 
       'x-api-key': token
     }
    data = {
      'utext': question, 
      'lang': 'id',
      'country': ['ID'],
      'atext_bad_prob_max': '0.7'
      }
    req=requests.post("https://wsapi.simsimi.com/190410/talk/",data=json.dumps(data), headers=headers)
    return req.json().get("atext","Simi Lagi Sibuk :)")
"""
def chatbot(question):
  return requests.get("https://simsumi.herokuapp.com/api", params={"text":question, "lang":"id"}).json().get("success", "Simi Sedang Sibuk :)")