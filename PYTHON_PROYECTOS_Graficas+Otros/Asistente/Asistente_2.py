import time
import speech_recognition as sr
import pyttsx3
import os

os.system("cls")

listener = sr.Recognizer()
engine = pyttsx3.init ()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
engine.runAndWait()

mensaje = "Hola, ya puedes hablar"

engine.say(mensaje)
engine.runAndWait()
print(mensaje)


with sr.Microphone() as source:
    voice = listener.listen(source)
    try:
        rec = listener.recognize_google(voice, language ="es")
        rec = rec.lower()
        print (rec)
        engine.say(rec)
        engine.runAndWait()
    except:
        error = "No te pude entender"
        print (error)
        engine.say(error)
        engine.runAndWait()
      
    engine.say("Fin del  mensaje")
    engine.runAndWait()
#------------------------------------------------------------------------------------------------------------
