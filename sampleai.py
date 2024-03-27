import pyttsx3
import time
from datetime import date
import speech_recognition as sr
import os
import pyaudio
import webbrowser
from selenium import webdriver 
import pyautogui

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

nowtime = time.strftime('%I:%M %p')
hour = time.strftime("%H")
today = date.today()
day = today.strftime(" %d %B, %Y")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recgonizing...")
        text = r.recognize_google(audio, language = 'en-in')
        print("You said : ", text)

    except Exception as e:
        # pass
        print("Say that again please!")
        return "None"
    return text

def greeting():
    hours = int(hour)
    if hours >=0 and hours <12:
        speak("goodmorning sir...")
        speak(f"today is {day}")

    elif hours >= 12 and hours <=18:
        speak("Good Afternoon sir...")

    else:
        speak("Good Evening sir...")

if __name__ =="__main__":
    while True:
        comm= takeCommand()
        if comm == "Jarvis" or comm == "Wake up Jarvis":
            greeting()
            
            while True:
                text = takeCommand()
                if "open Chrome"  in  text:
                    chromepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"#this my chrome location
                    speak("I am opening Chrome sir")
                    os.startfile(chromepath)

                elif "open YouTube" in text   :
                    speak("I am opening Youtube sir")
                    webbrowser.open("https://youtube.com")
                
                elif "play a song for me" in text:
                    speak("I am opening spotify sir")
                    webbrowser.open("https://spotify.com")

                elif "open vs code" in text:
                    codepath ="C:\\Users\\SAINATH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"#this my vs code location
                    speak("I am opening v s code sir")
                    os.startfile(codepath)

                elif "open open office" in text:
                    openpath = "C:\\Program Files (x86)\\OpenOffice 4\\program\\soffice.exe"#this my openoffice location
                    speak("I am opening open office sir")
                    os.startfile(openpath)

                elif "open typing master" in text:
                    typepath  = "G:\\TypingMaster11\\TypingMaster.exe"#this my typingmaster location
                    speak("opening typing master sir")
                    os.startfile(typepath)
                
                elif "open CMD" in text:
                    os.system("start cmd ")  
                    speak("opening command prompt")
                

                elif "search" in text:
                    find = text.split()
                    find.pop(0)
                    search_find = '+'.join(find)
                    address = 'https://www.google.com/search?q='
                    url = address + search_find
                    print(url)
                    webbrowser.open_new(url)  
                
                elif "close application" in text:
                    speak("Closing  sir...")
                    pyautogui.hotkey("alt", "f4")

                elif "open thisPC" in text:
                    pyautogui.hotkey("fn","f11")
                
                elif "go to sleep" in text :
                    speak("I am sleeping sir")
                    break
                    
                elif "shutdown" in text:
                    speak("I am shutting down sir")
                    exit()
                elif "what is time" in text:
                    speak(nowtime)
                elif "what is date" in text:
                    speak(f"Today is {day}")
        elif "shutdown" in comm:
            speak("I am shutting down sir...")
            break