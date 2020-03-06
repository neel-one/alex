import speech_recognition as sr
import os
from gtts import gTTS
from playsound import playsound
import time

r = sr.Recognizer()
def MyCommand():
    with sr.Microphone() as source:
        print('Say something...')
        #r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('Command: ' + command)
    except sr.UnknownValueError:
        print("...")
        command = MyCommand()
    return command

def response(audio, filename = 'audio/latest_command.mp3'):
    text = ' ' + audio
    speak = gTTS(text = text, lang = 'en', slow = False )
    speak.save(filename)
    playsound(filename)
    #os.system("latest_command.mp3")

def WakeUp():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio).lower()
        except sr.UnknownValueError:
            return False
        print('Command: ' + command)
    if 'hey alex' or 'wake up' or 'listen' in command:
        playsound("audio/wake_up.mp3")
        return True
    return False


woken = False
while not woken:
    woken = WakeUp()


response(MyCommand())





