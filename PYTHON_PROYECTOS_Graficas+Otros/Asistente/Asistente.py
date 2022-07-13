import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()

engine = pyttsx3.init ()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)

#engine.say("Buenos dias")
engine.runAndWait()

def talk (text):
    engine.say(text)
    engine.runAndWait()
    print (text)

try:
    with sr.Microphone() as source:
        print("Escuchando....")
        voice = listener.listen(source)
        rec = listener.recognize_google(voice)
        rec = rec.lower()
        if 'protocolo uno dos tres' in rec:
            engine.say("Buenos dias, activando el protocola 123")
            engine.runAndWait()
        else:
            talk(rec)
            engine.say("Eso fue lo que entendí")
            engine.runAndWait()
   #     talk(rec)

except:
    pass
