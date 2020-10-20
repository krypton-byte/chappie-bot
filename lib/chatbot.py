import requests, json
def chatbot(question):
    headers = {
       'content-type': 'application/json', 
       'x-api-key': 'HGOheEzs7VL1.369BDXiVyr5jE~5VuAWPjdOLetG'
     }
    data = {
      'utext': question, 
      'lang': 'id',
      'country': ['ID'],
      'atext_bad_prob_max': '0.7'
      }
    req=requests.post("https://wsapi.simsimi.com/190410/talk/",data=json.dumps(data), headers=headers)
    return req.json().get("atext","Simi Lagi Sibuk :)")
