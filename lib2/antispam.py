import time
ListOfBlock=[]
History=[]
class spam:
    def __init__(self, number):
        self.number    = number
        self.waktu     = time.time()
        self.masablock = 60.00 # Masa Blokir Sementara
        self.interval  = 1.00  # Jarak
        self.limit     = 2     # Dapat Dikatanan Bot Jika Spam Melebihi Batas Limit Secara Berturut Turut
    def check(self):
        for i in enumerate(ListOfBlock):
            if i[1][1] == self.number and self.masablock + i[1][0] > self.waktu and i[1][2]==self.limit:
                return {"s":self.masablock-(int(self.waktu - i[1][0]))}
            elif i[1][1] == self.number and self.masablock + i[1][0] < self.waktu and i[1][2]==self.limit:
                ListOfBlock[i[0]]=[self.waktu, self.number, 1]
                return {}
        for i in enumerate(History):
            if i[1][1] == self.number:
                selisih = self.waktu - i[1][0]
                IndexHist=i[0]
                History[IndexHist] = [self.waktu, self.number]
                break
        else:
            History.append([self.waktu, self.number])
            return {}
        if selisih == self.limit:
            History[IndexHist] = [self.waktu, self.number]
            return {}
        for i in enumerate(ListOfBlock):
            if i[1][1] == self.number and i[1][2] == self.limit and self.waktu - i[1][0] > self.interval:
                ListOfBlock[i[0]] = [self.waktu, self.number, 1]
                return True
            elif i[1][1] == self.number and selisih < self.interval:
                ListOfBlock[i[0]] = [self.waktu,self.number, i[1][2]+1]
                return {}
        else:
            ListOfBlock.append([self.waktu, self.number, 1])
            return {}
    def __repr__(self) -> str:
        return f"number: {self.number} timestamp: {self.waktu}"

