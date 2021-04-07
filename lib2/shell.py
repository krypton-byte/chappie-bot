import requests
language={
    "Bash":"bash",
    "Python 2":"python2",
    "Python 3":"python3",
    "C":"c",
    "C++":"cpp",
    "PHP":"php",
    "NodeJs":"nodejs",
    "Perl":"perl",
    "Kotlin":"kotlin",
    "VB.NET":"vbn",
    "Pascal":"pascal",
    "Dart":"dart",
    "BrainFuck":"brainfuck",
    "GoLang":"go",
    "C#":"csharp",
    "SQL":"sql",
    "Scala":"scala",
    "Groovy":"groovy",
    "Fortran":"fortran",
    "R":"r",
    "RhinoJs":"rhino",
    "Swift":"swift",
    "Scheme":"scheme",
    "Gcc Assembler":"gccasm",
    "Elixir":"elixir",
    "Clojure":"clojure",
    "Lua":"lua",
    "Haskell":"haskel",
    "Cobol":"cobol",
    "Falcon":"falcon",
    "CoffeeScript":"coffeescript",
    "NASM":"nasm",
    "Objective-C":"objc"
}
def langExecute(lang, sc):
    key=language.keys()
    if lang < len(list(key)) and lang >= 0:
        data={'args': None, 'libs': [], 'language': language[list(key)[lang]], 'script': sc, 'stdin': None, 'versionIndex': 3}
        print(data)
        return requests.post("https://www.jdoodle.com/engine/execute",json=data, headers={'kurukku-kuri': 'b6b214d5-f225-4583-bf89-43c8a156027e', 'origin': 'https://www.jdoodle.com', 'referer': 'https://www.jdoodle.com/python3-programming-online/', 'sec-fetch-dest': '', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36', 'x-requested-with': 'XMLHttpRequest'}).json()
    return ListLang()
def ListLang():
    lan="-----Bahasa Yg Tersedia--------\n"
    for i in enumerate(language):
        lan+=f"{i[0]} : {i[1]}\n"
    return lan.strip()
