import pyttsx3 # type: ignore
import speech_recognition as sr # type: ignore
import datetime
import wikipedia # type: ignore
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
       speak("Good Afternoon!") 

    else:
       speak("Good Evening!") 

    speak("I am meenu mam. Please tell me how may I help you")

def takecommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":

    wishMe()
    while True:
        query = takecommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")


        elif 'play music' in query:
            music_dir = r"C:\Windows\WinSxS\Temp\PendingRenames\c03c16642004db014d1f0000a815ec44.users_default_music_4066f7392302d756.cdf-ms"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, the time is {strTime}")


        elif 'open code' in query:
            codepath = "C:\Program Files\Microsoft Office\root\Office16\ADDINS\EduWorks Data Streamer Add-In\Microsoft.VisualStudio.Tools.Applications.Runtime.dll"
            os.startfile(codepath)