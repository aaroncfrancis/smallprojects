import speech_recognition as sr
import pyttsx3 as pyt

engine = pyt.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def run():
    r = sr.Recognizer()

    with sr.Microphone as inputSource:
        print("Say Something")
        audio = r.record(inputSource)
        print("Done")
    try: 
        text = r.recognize_google(audio)
        print("Google recognizes your input as: /n" + text)
    except Exception as e:
        print(e) 

    memory = open('output.txt','w')
    memory.write(text)
    memory.close()

run()
