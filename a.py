import speech_recognition as aa 
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import random
import webbrowser
import requests
import smtplib
from ecapture import ecapture as ec
import pyjokes
import subprocess
import os


listener = aa.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction(ask = False):
    global instruction
    try:
        with aa.Microphone() as origin:
            listener.adjust_for_ambient_noise(origin,duration=1)
            talk("listening")
            print("listening")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "jarvis" in instruction:
                instruction = instruction.replace('jarvis'," ")
                print(instruction)
    except:
        pass
    return instruction
 
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('20cs096@ssit.edu.in', 'Varun')
    server.sendmail('20cs096@ssit.edu.in', to, content)
    server.close()


def play_Jarvis():
    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
        song = instruction.replace('play', " ")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk('current time'+ time)

    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        talk("VARUN Today's date is" + date) 

    elif 'how are you' in instruction:
        talk('I am fine VARUN, how about you?')

    elif 'what is your name' in instruction:
        talk('I am Jarvis,what can i do for you? Varun')

    elif 'pick me a number' in instruction:
        val = random.randint(0,1000)
        print(val)
        talk(val)

    elif 'send a mail' in instruction:
        try:
            talk("What should I say?")
            content = input_instruction()
            print(content)
            talk("whome should i send")
            to = input()   
            sendEmail(to, content)
            talk("Email has been sent !")
        except Exception as e:
                print(e)
                talk("I am not able to send this email")


    elif "write a note" in instruction :
        talk("What should i write, sir")
        note = input_instruction()
        file = open('jarvis.txt', 'w')
        talk("Sir, Should i include date and time")
        snfm = input_instruction()
        if 'yes' in snfm or 'sure' in snfm:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            file.write(strTime)
            file.write(" :- ")
            file.write(note)
        else:
            file.write(note)

    elif "show me the notes" in instruction:
            talk("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            talk(file.read(6))

    
    elif 'who is' in instruction:
        human = instruction.replace('who is', " ")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)

    elif 'good morning' in instruction:
        talk('hey good morning varun hope you had a good sleep...I wish you a great day')

    elif 'who created you' in instruction:
        talk('I was created by ,,,mister VIGNESH AND mister VARUN ')

    elif 'tell me a joke' in instruction:
        joke=pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif 'tell me about yourself' in instruction:
        talk('hey I am JARVIS...I am a voice assistant for VARUN..........I was created by VARUN and VIGNESH as a MINI project....under the guidance of lecturer Dr Guruprakash...')

    elif 'search' in instruction:
        talk('what do u want to search')
        search = input_instruction("what do u want to search VARUN")
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        talk('VARUN,,,,,here is what i found for' +search)
    
    elif 'calculate' in instruction:
        talk('input the expression')
        n = input("type here:")
        x=print("your answer is",eval(n))
    
    elif "take a photo" in instruction or "camera" in instruction:
        ec.capture(0,"Jarvis camera","img.jpg")

    elif 'jarvis who am i' in instruction:
        talk('if u are talking then definitely... human ')

    elif "restart" in instruction:
            subprocess.call(["shutdown", "/r"])
    
    else:
        talk('SORRY! VARUN ,,Can you Please repeat what you asked')

play_Jarvis()