import speech_recognition as sr
import pyaudio as pa

recognizer = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("Say something!")
            
            recognizer.adjust_for_ambient_noise(source, duration=0.2)
            audio = recognizer.listen(source)            
            text = recognizer.recognize_sphinx(audio)
            text = text.lower()

            print(f"You said: {text}")

    except sr.UnknownValueError:
        recognizer = sr.Recognizer()
        continue