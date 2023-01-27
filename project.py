from ast import main
from msilib import MSIMODIFY_VALIDATE_NEW
from multiprocessing.spawn import _main
from tkinter.tix import MAIN
from tkinter import tix as tk
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os , subprocess
import time
import folium
import winshell
import urllib.request
import urllib.parse
import re
import win32 as shell
from pynput.keyboard import Key, Controller
from pynput import keyboard
import keyboard
import sys
import random
import subprocess as sp
from requests import get
import cv2
import pywhatkit as kit
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
from PyPDF2 import PdfFileReader
import turtle #print(voices[1].id)
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak ("Good evening")
    speak("Hello i am  your taskboat, what can i do for you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said :{query}\n")
    except Exception as e:
        print("Say that again please...")
        return"None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('smartabhigupta09@gmail.com','#Gurukul2integral')
    server.sendmail('smartabhigupta09@gmail.com',to,content)
    server.close()

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'who are you ' in query:
            speak(' i am your taskbot')   

        elif 'open google' in query:
            speak("Sir ,what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"https://{cm}")


        elif 'open  youtube' in query:
            webbrowser.open("youtube.com")


        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")


         #   os.startfile(codePath)
        elif 'play music' in query:
            music_dir = 'G:\Audio songs\mix'
            songs = os.listdir(music_dir)
            rd = random.choice(songs) 
            os.startfile(os.path.join(music_dir, rd))


        #     speak("my name is abhishek gupta");
        elif 'current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")


        elif 'where am i' in query:
                speak('wait ! i am fatching')
                time.sleep(3)
                india = folium.Map(location = ['26.90173', '80.97416']).save("india1.html")
                webbrowser.open("india1.html")   


        elif  'bin' in query:
                try:

                    speak("i am trying to clear recycle bin")
                    time.sleep(3)
                    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
                    speak("Sucessfully clear recycle bin")
                except :
                    speak("Sorry! nothing in recycle bin")


        elif "open youtube and play" in query:
                try:

                    x=query[21:]
                    def remove(string): 
                        return string.replace(" ", "") 
            
                    string = x
                    v=(remove(string))
                    speak("Well i am fetching "+v)
                    print(v)
                    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + v)
                    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                    print("https://www.youtube.com/watch?v=" + video_ids[0])
                    webbrowser.open("https://www.youtube.com/watch?v=" + video_ids[0])
                except :
                    speak("i think You colse the window ! before of the execuation") 


        elif 'open task manager' in query:
            commands = 'taskmgr'
            shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)
            speak("sucessfully open task manager")
            time.sleep(5)


        elif re.search('open notepad', query):
                speak("opening notepad")
                programName = "notepad.exe"
                fileName = "abhiproject.txt"
                sp.Popen([programName, fileName])


        elif re.search('close notepad', query):
                speak("closing notepad")
                subprocess.call(["taskkill","/F","/IM","notepad.exe"])
    

        elif 'delete temporary files' in query:
                speak("wait i am fatching data")
                time.sleep(3)
                del_dir2 = r'C:\\Windows\\Temp'
                del_dir3 = r'C:\\Windows\\SoftwareDistribution\\Download'
                #obj = subprocess.Popen('rmdir /S /Q %s' % del_dir, shell=True, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
                obj2 = subprocess.Popen('rmdir /S /Q %s' % del_dir2, shell=True, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
                obj3 = subprocess.Popen('rmdir /S /Q %s' % del_dir3, shell=True, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
                #trp = obj.communicate()
                trp2= obj2.communicate()
                trp3= obj3.communicate()
                #rCod = obj.returncode
                rCod2 = obj2.returncode
                rCod3 = obj3.returncode
                if rCod2 == 0:
                    print('Success: Cleaned Windows Temp Folder')
                    speak("Sucessfully Cleaned Windows Temporary files")
                else:
                    print('Fail: Unable to Clean Windows Temp Folder')
                    speak("Fail Unable to  Cleaned Windows Temporary files")


        elif 'tree' in query:
            t=turtle.Turtle()
            t.screen.bgcolor('white')
            t.pensize(2)
            t.left(90)
            t.backward(100)
            t.speed(200)
            t.shape('turtle')
            def tree(i):
                if i<10:
                    return
                else:
                    t.forward(i)
                    t.color('red')
                    t.circle(2)
                    t.color('brown')
                    t.left(30)
                    tree(3*i/4)
                    t.right(60)
                    tree(3*i/4)
                    t.left(30)
                    t.backward(i)
            tree(100)
            turtle.done()


        elif "send message" in query:
            kit.sendwhatmsg("+917651941012","this is testing protocol",2,25)


        elif "open command prompt" in query:
            os.system("start cmd")
        

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllwindows()
        


        elif " ip address" in query:
            ip = get ('https://www.api.ipify.org').text
            speak(f" your ip address is {ip}")
            


        elif "send mail to abhi" in query:
            try:
                speak("email should i say?")
                content = takeCommand().lower()
                to = "abhgupta09@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to abhi")
            except Exception as e:
                print(e)
                speak("sorry sir , i am not able to send this e mail")



        elif 'exit' in query or 'close maya' in query:
                speak("Good bye see you soon")
                exit()


        elif 'shutdown' in query or 'shutdown this pc' in query:
            speak("do you want to shut down your laptop")
            sd= takeCommand().lower()
            try:

                if 'yes' in sd:
                    time.sleep(2)
                    speak("shutingdown your laptop see you soon")
                    os.system('shutdown /s /t 1')
                else:
                    speak("ok well !")  
            except:
                    speak("something went wrong")
                    
        

        elif 'restart' in query or 'shutdown this pc' in query:
            speak("do you want to restart your laptop")
            sd= takeCommand().lower()
            try:

                if 'yes' in sd:
                    time.sleep(2)
                    speak("restarting  your laptop see you soon")
                    os.system('shutdown /r /t 1')
                else:
                    speak("ok well !")  
            except:
                    speak("something went wrong")


        elif 'sleep' in query or 'shutdown this pc' in query:
            speak("do you want to sleep your laptop")
            sd= takeCommand().lower()
            try:

                if 'yes' in sd:
                    time.sleep(2)
                    speak(" your laptop is going to sleep")
                    os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
                else:
                    speak("ok well !")  
            except:
                    speak("something went wrong")