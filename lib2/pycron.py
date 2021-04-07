import rx3
import time
data=[] #{"time":<timestamp>, "chat_id":<id>}
driver = None
def setDriver(dr): 
    global driver
    driver = dr
def setCountDown(arg):
    global data
    data.append(arg)
def isMin(dat):
    global data
    for i in dat:
        if i["time"]-time.time()>1:
            driver.wapi_functions.sendMessage(i["chat_id"], f"*{int(i['time']-time.time())} Detik lagi*")
        else:
            driver.wapi_functions.sendMessage(i["chat_id"], "*Waktu Habis*")
            data.remove(i)
rx3.interval(1).pipe().subscribe(lambda x:isMin(filter(lambda _: _["time"]-time.time()<4, data)))