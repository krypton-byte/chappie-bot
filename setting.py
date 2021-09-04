import os
proxy = {}
author = [os.environ.get("AUTHOR", "6283172366463").strip("@c.us")+"@c.us"]
BotName = os.environ.get("botname","Krypton-Bot") #profile_name
prefix = os.environ.get("prefix","!")
server = os.environ.get("server","http://sticker-database.herokuapp.com")
#server = "http://127.0.0.1:8000"
MenuList=lambda prefix, BotNamex, author, name:f"""
─────「 {BotNamex} 」─────

Hai, {name}! 👋️

╭────「 INFO BOT 」──────
│
│+ Name    : {BotNamex}
│+ Creator : Krypton Byte
│+ Ver Bot : v1.1
│+ Owner   : {author[:-5]}
│
│+ {prefix}ping
│+ {prefix}status
│+ {prefix}runtime
│
╰────────────────────
╭────「 CREATOR 」──────
│
│+ {prefix}toimg
│+ {prefix}blackpink
│+ {prefix}ph
│+ {prefix}quotemaker
│+ {prefix}tulis teks
│+ {prefix}qrmaker
│+ {prefix}img2ascii
│+ {prefix}8bit
│+ {prefix}fdeface
│
╰────────────────────
╭────「 ISLAM 」 ───────
│
│+ {prefix}quran
│
╰────────────────────
╭──「 INSTA FILTER」 ───
│
│+ {prefix}ifilter _1977
│+ {prefix}ifilter aden
│+ {prefix}ifilter brannan
│+ {prefix}ifilter brooklyn
│+ {prefix}ifilter clarendon
│+ {prefix}ifilter earlybird
│+ {prefix}ifilter gingham
│+ {prefix}ifilter hudson
│+ {prefix}ifilter inkwell
│+ {prefix}ifilter kelvin
│+ {prefix}ifilter lark
│+ {prefix}ifilter lofi
│+ {prefix}ifilter maven
│+ {prefix}ifilter mayfair
│+ {prefix}ifilter moon
│+ {prefix}ifilter nashville
│+ {prefix}ifilter perpetua
│+ {prefix}ifilter reyes
│+ {prefix}ifilter rise
│+ {prefix}ifilter slumber
│+ {prefix}ifilter stinson
│+ {prefix}ifilter toaster
│+ {prefix}ifilter valencia
│+ {prefix}ifilter walden
│+ {prefix}ifilter willow
│+ {prefix}ifilter xpro2
│
╰────────────────────
╭────「 STICKER 」 ─────
│
│+ {prefix}cimage
│+ {prefix}tstiker
│+ {prefix}sticker
│+ {prefix}tele_sticker
│+ {prefix}gif
│+ {prefix}save_sticker
│+ {prefix}get_sticker
│+ {prefix}delete_sticker
│+ {prefix}list_sticker
│
╰────────────────────
╭─────「 USERS 」 ──────
│+ {prefix}gf
│ (for looking for a gf)
│+ {prefix}bf
│ (for looking for a bf)
│+ {prefix}reg
│ (Register)
╰────────────────────
╭────「 DOWNLOADER 」 ──
│
│+ {prefix}yt2mp3 link
│+ {prefix}yt2mp4 link
│+ {prefix}play title
│+ {prefix}ig link
│+ {prefix}fb link
│+ {prefix}pintdown
│+ {prefix}tiktok
│+ {prefix}tiktok2
│+ {prefix}twitter_download
│+ {prefix}doujin
│+ {prefix}xnx2mp4
│
╰────────────────────
╭───「 N Downloader」 ──
│+ {prefix}doujin nuclear
│+ {prefix}nsearch query
│+ {prefix}nserachs query
╰────────────────────
╭────「 FUN 」─────────
│
│+ {prefix}tts
│+ {prefix}afk
│+ {prefix}other_bots
│+ {prefix}ts
│+ {prefix}dadu
│+ {prefix}transcript
│+ {prefix}pitnah
│+ {prefix}hidetag
│+ {prefix}ocr
│+ {prefix}pitch
│+ {prefix}qrreader
│+ {prefix}whatimage
│+ {prefix}whoisthis
│+ {prefix}simi
│+ {prefix}joke
│+ {prefix}bct
│+ {prefix}pitch
│+ {prefix}alay
│+ {prefix}morse
│
╰────────────────────
╭────「 IMAGES 」──────
│
│+ {prefix}images
│+ {prefix}neko
│+ {prefix}dog
│+ {prefix}kitsune
│+ {prefix}cari_gambar
│+ {prefix}gambar
│+ {prefix}pinterest
│
╰────────────────────
╭────「 ANIME 」───────
│
│+ {prefix}wait
│+ {prefix}kusonime
│+ {prefix}otakudesu
│
╰────────────────────
╭────「 OTHER 」───────
│
│+ {prefix}film
│+ {prefix}cari
│+ {prefix}wiki
│+ {prefix}quote
│+ {prefix}kquote
│+ {prefix}chord title
│+ {prefix}igstalk
│+ {prefix}url2png
│+ {prefix}report
│+ {prefix}check
│+ {prefix}? [question] [amount]
│  (Brainly)
│+ {prefix}upimg
│+ {prefix}support
│
╰────────────────────
╭────「 ADMIN 」───────
│
│+ {prefix}delete
│+ {prefix}join
│+ {prefix}grup
│+ {prefix}add
│+ {prefix}mentionall
│+ {prefix}linkgroup
│+ {prefix}revoke
│+ {prefix}notoxic [0/1] [amount]
│+ {prefix}nsfw  [0/1] [amount]
│+ {prefix}kick @tag
│+ {prefix}unadmin @tag
│+ {prefix}admin @tag
│
╰────────────────────
╭────「 AUTHOR 」───────
│+ {prefix}bc
│+ {prefix}pembersihan
│
╰────────────────────

Hope you have a great day!✨""".strip()
