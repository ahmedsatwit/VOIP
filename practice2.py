import pyttsx3
voice = pyttsx3.init()
while 1: 
    voice.say(input("What should he say?\n"))
    voice.runAndWait()