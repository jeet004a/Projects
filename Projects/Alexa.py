import pyaudio
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import requests
import sys
import bs4




engine=pyttsx3.init('sapi5')

voices= engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")

    speak("I am Alexa   sir . Please tell me how may i help you")



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        print("Recongnizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
        print("say that again please....")
        return "None"
    return query


def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('wastijeet110@gmail.com','Chintu012')
    server.sendmail('wastiarco01@gmail.com',to,content)
    server.close()





if  __name__ == "__main__":
    wishMe()
    #if 1:
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('serching Wikipedia....')
            query= query.replace("wikipedia", "")
            results=wikipedia.summary(query,sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            speak("so   what   sir  next  i  am here for  you!")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak(" so  what     next   i    am here for    you!")
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("so what next i am here for you!")
        
        
        elif 'play music' in query:
            music_dir='E:\\Song'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
            speak(" so what next i am here for you!")
        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            speak("so what next i am here for you!")

        elif 'open code' in query:
            codePath='E:\\Song\\Woofer - Dr Zeus.mp3' 
            os.startfile(codePath)
            speak(" so what next i am here for you!")
        elif 'email' in query:
            try:
                speak("what should i say?")
                content=takeCommand()
                to="wastiarco01@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Not  send ")
            speak("so what next i am here for you!")

        elif 'google' in query:
            speak("what would you search!")
            content=takeCommand()        
            if content=="nothing":
                exit
            else:
                webbrowser.open('https://google.com/search?q='+content)
            speak("so what next i am here for you!")
        elif 'youtube' in query:
            speak("what would you search!")
            content=takeCommand()        
            if content=="nothing":
                exit
            else:
                webbrowser.open('https://youtube.com/search?q='+content)
            speak("so what next i am here for you!")


            
        elif 'stop' in query:
            speak("Thank you for using me ")
            break
        
            


