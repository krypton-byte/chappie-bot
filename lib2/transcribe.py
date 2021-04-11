from moviepy import editor
import os
import speech_recognition as sr
def SpeechToText(filename:str, lang="en"):
    editor.AudioFileClip(filename).write_audiofile(f"{filename}.wav")
    listen=sr.Recognizer()
    with sr.AudioFile(f"{filename}.wav") as source:
        audio = listen.record(source)
        result=listen.recognize_google(audio, language=lang, show_all=True)
        os.remove(f"{filename}.wav")
        os.remove(filename)
        pesan=""
        print(lang)
        if result:
            x="Transcript"
            for i in result["alternative"]:
                pesan+=f"{x}:  {i['transcript']} \n\n"
                x="Alternatif"
            return pesan.strip()
        else:
            return "Gagal Menerjemahkan Audio"


