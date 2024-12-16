import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import smtplib
import vlc
import time
from bs4 import BeautifulSoup
import requests
import sys
import webbrowser as wb
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon!")  
  
    else:
        speak("Good Evening !") 
  
    assname =("Edith")
    speak("Hi, I am your Assistant")
    speak(assname)
    
def username():
    speak("What should I call you?")
    uname = takeCommand()
    speak("Welcome ")
    speak(uname)
     
    print("#####################")
    print("Welcome ", uname)
    print("#####################")
     
    speak("How can I help you?")
 
def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        audio = r.listen(source)
  
        try:
            text = r.recognize_google(audio)
            print("You said: {}".format(text))
  
        except:
            print("Unable to Recognize your voice.") 
     
        return text 
    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in mail
    server.login('245621737044.glwec@gmail.com', 'uhkegfxpbnyxgmqy')
    server.sendmail('245621737044.glwec@gmail.com', to, content)
    server.close()

def play_song(song):
    song = str(song)
    p = vlc.MediaPlayer(song + ".mp3")
    p.play()
    time.sleep(10)
    p.stop()
    
def weather(city):
	city = city.replace(" ", "+")
	res = requests.get(
		f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
	print("Searching...\n")
	soup = BeautifulSoup(res.text, 'html.parser')
	location = soup.select('#wob_loc')[0].getText().strip()
	time = soup.select('#wob_dts')[0].getText().strip()
	info = soup.select('#wob_dc')[0].getText().strip()
	weather = soup.select('#wob_tm')[0].getText().strip()
	print(location)
	print(time)
	print(info)
	print(weather+"°C")
    
def tellTime():
    time = str(datetime.datetime.now())
    #the time will be displayed like this "2020-06-05 17:50:14.582630"
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is " + hour + "hours" + "and" + min + "Minutes")
    
def tellDay():
   day = datetime.datetime.today().weekday() + 1
   Day_dict = {1: 'Monday', 2: 'Tuesday', 
               3: 'Wednesday', 4: 'Thursday', 
               5: 'Friday', 6: 'Saturday',
               7: 'Sunday'}
     
   if day in Day_dict.keys():
       day_of_the_week = Day_dict[day]
       print(day_of_the_week)
       speak("The day is " + day_of_the_week)
       
def past_papers(sub):
    sub = str(sub)
    wb.open_new(sub+".pdf")
    speak("Opening the paper for "+sub)
    


if __name__ == '__main__':
    clear = lambda: os.system('cls')
     
    clear()
    wishMe()
    username()
     
    while True:
         
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak("Directing you to Youtube\n")
            webbrowser.open("youtube.com")
 
        elif 'open google' in query:
            speak("Directing you to Google\n")
            webbrowser.open("google.com")
        
        elif "day" in query:
            tellDay()
            continue
        
        elif "time" in query:
            tellTime()
            continue
                
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you?")
            
        elif "change your name to" in query:
            query = query.replace("change your name to", "")
            assname = query
        
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            sys.exit()
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        elif 'mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whom should i send")
                to = input()   
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
                
        elif "music" in query:
            speak("What song should I play?")
            print("As It Was - Harry Styles")
            print("Heat Waves - Glass Animals")
            print("Stay - The Kid Laroi & Justin Bieber")
            speak("Tell me your music choice from the following list")
            speak("Say only the song title!")
            song = takeCommand()
            play_song(song)
            
        elif "weather" in query:
            speak("What city would you like to see?")
            city = takeCommand()
            city = city+" weather"
            weather(city)
            speak("I have listed the data for ")
            speak(city)
        
        elif "previous" in query:
            speak("Which subject's previous paper would you like me to open?")
            print("Math")
            print("English")
            print("Chemistry")
            print("Physics")
            speak("Please choose from the following list")
            sub = takeCommand()
            past_papers(sub)
            
            
                
                









    
    
    
    
    