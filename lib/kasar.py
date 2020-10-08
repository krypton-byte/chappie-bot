import sqlite3
class Kasar:
    def __init__(self, chat_id):
        self.chat_id = chat_id
    def add_check_kick(self, chat):
        b=sqlite3.connect('kesalahan.db')
        db=b.cursor()
        data_=db.execute('SELECT * FROM KESALAHAN WHERE number="%s"'%(self.chat_id)).fetchall()
        print('add check kik')
        if data_: #telah terdaftar
            if int(data_[0][1]) > 1:
                print('True')
                chat.remove_participant_group(self.chat_id.split('-')[0]+'@c.us')
                db.execute('DELETE FROM KESALAHAN WHERE number="%s"'%(self.chat_id))
                b.commit()
                driver.send_image_as_sticker('sticker/%s'%(random.choice(os.listdir('sticker'))), self.chat_id)
                print('terhapus')
            else:
                print('False')
                db.execute(f'UPDATE KESALAHAN SET jumlah="{int(data_[0][1])+1}" WHERE number="{self.chat_id}"')
                b.commit()
                print(int(data_[0][1])+1)
                print('Telah Tertambah 1')
        else: #belum terdaftar
            print('False')
            db.execute('INSERT INTO KESALAHAN VALUES ("%s","1")'%(self.chat_id)).fetchall()
            b.commit()
            print('Terbuat 1')
    def check(self):
        b=sqlite3.connect('kesalahan.db')
        db=b.cursor()
        data_=db.execute('SELECT * FROM KESALAHAN WHERE number="%s"'%(self.chat_id)).fetchall()
        if data_:
            return str(data_[0][1])
        else:
            return '0'