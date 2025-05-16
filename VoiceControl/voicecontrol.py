import speech_recognition as sr
from pynput.keyboard import Controller, Key

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"{index}: {name}")

recognizer = sr.Recognizer()
keyboard = Controller()

single_command_map = {
    "foward":'w',
    "back":'s',
    "left":'a',
    "right":'d',
    "run": Key.shift,
    "shoot": Key.ctrl_l,
    "open": Key.space,
    "switch": '2',
    "look left": Key.left,
    "look right": Key.right,
    "look up": Key.up,
    "look down": Key.down,
}

combo_command_map = {
    "run forward": [Key.shift, 'w'],
    "run back": [Key.shift, 's'],
    "run left": [Key.shift, 'a'],
    "run right": [Key.shift, 'd'],
}

def recognize_and_trigger():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        print("Audio Captured.")
        try:
            command = recognizer.recognize_vosk(audio)
            print(f"Recognized command: {command}")

            for phrase, keys in combo_command_map.items():
                if phrase in command:
                    for key in keys:
                        keyboard.press(key)
                    for key in reversed(keys):
                        keyboard.release(key)
                    return
            
            for phrase, key in single_command_map.items():
                if phrase in command:
                    keyboard.press(key)
                    keyboard.release(key)
                    return
        
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Request error: {e}")

if __name__ == "__main__":
    while True:
        recognize_and_trigger()