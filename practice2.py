import pyttsx3
import os
voice = pyttsx3.init()
while 1: 
    voice.say(input("What should he say?\n"))
    voice.runAndWait()
    os.system("clear")
