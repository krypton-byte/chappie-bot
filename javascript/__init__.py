"""class krypton_patch:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.js     = driver.driver.execute_script
        driver.driver.execute_script("javascript/index.js") #patch 0.1
    def FakeReply(self, korban, pesan, chat_id, MsgId, teks):
        return self.js(f"return await FakeReply(\"{chat_id}\", \"{MsgId}\", \"{pesan}\", \"{korban}\", \"{teks}\")")
    def hidetag(self, chat_id, body, msg):
        return self.js(f"return await HideTagged(\"{chat_id}\", \"{body}\", \"{msg}\")")"""