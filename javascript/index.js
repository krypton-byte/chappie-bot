window.FakeReply = async function (chatId, msgid, pesan, korban, MessagE){
    if (typeof quotedMsg !== "object") quotedMsg = Store.Msg.get(msgid)
    var chat = Store.Chat.get(chatId);
    quotedMsg.__x_body = pesan;
    quotedMsg.__x_author["user"] = korban;
    var body=MessagE;
    if (!chat) return false;
    let extras = {
        quotedParticipant: quotedMsg.author || quotedMsg.from,
        quotedStanzaID: quotedMsg.id.id
    };
    var tempMsg = Object.create(Store.Msg.models.filter(msg => msg.__x_isSentByMe && !msg.quotedMsg)[0]);
    var newId = window.WAPI.getNewMessageId(chatId);
    var extend = {
        ack: 0,
        id: newId,
        local: !0,
        self: "out",
        t: parseInt(new Date().getTime() / 1000),
        to: new Store.WidFactory.createWid(chatId),
        isNewMsg: !0,
        type: "chat",
        quotedMsg,
        body,
        ...extras
    };
    Object.assign(tempMsg, extend);
    const res = await Promise.all(await Store.addAndSendMsgToChat(chat, tempMsg));
    if (res[1] != 'success') return false;
    return res[0].id._serialized

    };
window.HideTagged = async function (ch, body,messagE) {
    var chat = ch.id ? ch : Store.Chat.get(ch);
    var chatId = chat.id._serialized;
    var msgIveSent = chat.msgs.filter(msg => msg.__x_isSentByMe)[0];
    if (!msgIveSent) return chat.sendMessage(body);
    var tempMsg = Object.create(msgIveSent);
    var newId = window.WAPI.getNewMessageId(chatId);
    var mentionedJidList = body.match(/@(\d*)/g).filter(x => x.length > 5).map(x => new Store.WidFactory.createUserWid(x.replace("@", ""))) || undefined;
    var extend = {
      ack: 0,
      id: newId,
      local: !0,
      self: "out",
      t: parseInt(new Date().getTime() / 1000),
      to: new Store.WidFactory.createWid(chatId),
      isNewMsg: !0,
      type: "chat",
      body:messagE,
      quotedMsg: null,
      mentionedJidList
    };
    Object.assign(tempMsg, extend);
    await Store.addAndSendMsgToChat(chat, tempMsg)
    return newId._serialized;
  }