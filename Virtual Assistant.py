import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('here comes your wolframalpha id like'='VK6JV4-274JXEJK6')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-2].id)

volume = engine.getProperty('volume') #getting to know current volume level (min=0 and max=1)
#print (volume) #printing current volume level
engine.setProperty('volume',1.0)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Sir, I am your digital assistant jarvis!')
speak('How may i help you')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query

def sendEmail(to , content):
    server = smtplib.SMTP('smtplib.gmail.com' , 587)
    server.ehlo
    server.starttls()
    server.login('yourmail@gmail.com' , 'password')
    server.sendmail('receivermail@gmail.com', to , content)
    server.close()
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
            

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir')
            
        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
                                    
        elif 'play music' in query:
            music_dir = "F:\\music"
            songs = os.listdir(music_dir)
            print (songs)
            os.startfile(os.path.join(music_dir , songs[0]))
            speak('Okay, here is your music! Enjoy!')

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(F"sir , the time is {strTime}")
            
        elif 'open notepad' in query:
            notepad_path="C:\\Users\\Wolverine\\AppData\\Roaming\\Microsoft\Windows\\Start Menu\Programs\\Accessories\\notepad"
            os.startfile(notepad_path)

        elif 'email to akshay' in query:
            try:
                speak("what should i say")
                content = myCommand()
                to = "akshay@gmail.com"
                sendEmail(to , content)
                speak("email has been sent")

            except Exception as e:
                print(e)
                speak("sorry i am not able to send this email")
            

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!')
        
