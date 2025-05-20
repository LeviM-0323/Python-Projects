# VoiceControl

VoiceControl is a Python application that lets you control your computer or games (this program was made with GZDoom in mind) using spoken commands. It uses speech recognition to listen for specific phrases and simulates keyboard input, making it possible to play games or control applications hands-free. A simple Tkinter GUI displays the most recent recognized commands.

---

## Features

- **Voice Command Recognition:**  
  Uses your microphone and Google Speech Recognition to detect spoken commands.
- **Keyboard Simulation:**  
  Maps voice commands to keyboard keys using `pydirectinput` for compatibility with most games and apps.
- **Combo Commands:**  
  Supports multi-key combos (e.g., "run forward" triggers Shift+W).
- **Customizable:**  
  Easily add or modify commands in the code.
- **Live GUI Feedback:**  
  Displays the last few recognized commands in a floating, always-on-top window.

---

## Project Structure

```
PythonProjects/VoiceControl/
│
├── voicecontrol.py   # Main application script
├── mictester.py      # Mic tester script
├── requirements.txt  # Project requirements
└── README.md         # Project documentation
```

---

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/LeviM-0323/Python-Projects.git
   cd PythonProjects/VoiceControl
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
---

## Usage

1. **Run the application:**
   ```sh
   python voicecontrol.py
   ```
2. **Speak a command:**  
   - Example commands: "forward", "back", "run forward", "look left", "shoot", "jump", etc.
   - The recognized command will be shown in the floating GUI window.
   - The corresponding keyboard key(s) will be pressed for a short duration.

3. **Customize commands:**  
   - Edit the `single_command_map` and `combo_command_map` dictionaries in `voicecontrol.py` to add or change commands.

---

## Notes

- **Microphone Selection:**  
  If you have multiple microphones, you may need to specify the correct one in the code.
- **Game Compatibility:**  
  `pydirectinput` is designed to work with most games, but some may require running as administrator.
- **Safety:**  
  Use with caution, as the script will send real keyboard inputs to your system.

---

## License

This project is open source and available under the MIT License.