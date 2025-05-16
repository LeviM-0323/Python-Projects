import speech_recognition as sr
import pydirectinput
import time

# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print(f"{index}: {name}")

recognizer = sr.Recognizer()

single_command_map = {
    "forward":'w',
    "back":'s',
    "left":'a',
    "right":'d',
    "look left":'left',
    "look right":'right',
    "look up":'up',
    "look down":'down',
    "shoot":'ctrl',
    "center":'end',
    "run": 'shift',
    "open": 'e',
    "crouch": 'x',
    "jump": 'space',
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
    # "ten": '0',
}

combo_command_map = {
    "run forward": ['shift', 'w'],
    "run back": ['shift', 's'],
    "run left": ['shift', 'a'],
    "run right": ['shift', 'd'],
}

PRESS_DURATION = 0.3

while True:
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            recognizer.pause_threshold = 0.5
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio, language="en-US")
            command = command.lower()
            print(f"{command}")

            for phrase, keys in combo_command_map.items():
                if phrase in command:
                    for key in keys:
                        pydirectinput.keyDown(key)
                    time.sleep(PRESS_DURATION)
                    for key in keys:
                        pydirectinput.keyUp(key)  

            if "look left" in command:
                pydirectinput.keyDown('left')
                time.sleep(PRESS_DURATION)
                pydirectinput.keyUp('left')
            elif "look right" in command:
                pydirectinput.keyDown('right')
                time.sleep(PRESS_DURATION)
                pydirectinput.keyUp('right')
            elif "look up" in command:
                pydirectinput.keyDown('up')
                time.sleep(PRESS_DURATION)
                pydirectinput.keyUp('up')
            elif "look down" in command:
                pydirectinput.keyDown('down')
                time.sleep(PRESS_DURATION)
                pydirectinput.keyUp('down')
            else:
                for phrase, key in single_command_map.items():
                    if phrase in command:
                        pydirectinput.keyDown(key)
                        time.sleep(PRESS_DURATION)
                        pydirectinput.keyUp(key)
            
    except sr.UnknownValueError:
        recognizer = sr.Recognizer()
        continue