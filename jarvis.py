import pyttsx3
import os
import webbrowser as wb
import datetime

hour = int(datetime.datetime.now().hour)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if hour < 12:
    speak("Good Morning!!")
    print("Good Morning!!")

elif hour < 18:
    speak("Good Afternoon!!")
    print("Good Afternoon!!")

else:
    speak("Good Evening!!")
    print("Good Evening!!")

speak("I am jarvis sir please tell how may I help you")
print("Give a command which you want!!")


query = input()

if 'open youtube' in query:
    wb.register('chrome', None)
    wb.open('https://www.youtube.com')
    print("Opened youtube")
    speak("Opened youtube")

elif 'open notepad' in query:
    notepadPath = "C:\\Windows\\Notepad.exe"
    os.startfile(notepadPath)
    speak("Opened notepad")
    print("Opened notepad")

elif 'open google chrome' in query:
    chromePath =  "C:\Program Files\Google\Chrome\Application\chrome.exe"
    os.startfile(chromePath)
    speak("Opened google")
    print("Opened google")

elif 'open code' in query:
    codePath = "C:\\Users\\lokpr\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)

else:
    print("Command not found. If you want to run the command contact Sujal Lokhande mobile no. 7588519775")
    speak("Command not found. If you want to run the command contact Sujal Lokhande mobile no. 7588519775")

jarvisPath = "C:\\Users\\lokpr\\Downloads\\python\\jarvis2.py"

os.startfile(jarvisPath)

