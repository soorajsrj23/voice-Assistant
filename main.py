import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import time
import pyjokes

start_time = time.time()
listner = sr.Recognizer()
engine = pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            talk("Ask me anything")
            print("listening....")
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                talk(command)
            print(command)
    except:
        pass
    return command
start_time = time.time()

while (time.time() - start_time) < 4:
    take_command()
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk("playing "+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("Current time is "+time)
        print(time)
    elif 'who are you' in command:
        talk("I am jarvis version 1.0 developed by srj")
    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person,7)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("Sorry i could not hear you")

while True:
    run_alexa()