import speech_recognition as sr
import webbrowser
import time
import os
from gtts import gTTS
from datetime import datetime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if(ask):
            print(ask)

        audio = r.listen(source)
        voice_data = ''

        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('Sorry did not understand that')
        except sr.RequestError:
            print('Sorry, system is down')

        return voice_data

def respond(voice_data):
    if 'what is your name' in voice_data:
        print('I am mini Jarvis')
    if 'what time is it' in voice_data:
        print(datetime.now().time())
    if 'search' in voice_data:
        search = record_audio('What would you like to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('Here is what I found for ' + search)
    if 'location' in voice_data:
        loc = record_audio('Find location')
        url = 'https://google.nl/maps/place' + loc + '/&amp;'
        webbrowser.get().open(url)
        print('Here is the location of ' + loc)
    if 'exit' in voice_data:
        exit()

time.sleep(1)
print('Mini-Jarvis here, how can I help?')
while 1:
    voice_data = record_audio()
    respond(voice_data)