import requests
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import pywhatkit
import psutil


MODEL_NAME = "llama3"
MEMORY_FILE = "memory.txt"

engine = pyttsx3.init()
engine.setProperty('rate', 165)

def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()
    
def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def save_memory(data):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        f.write(data)

conversation_memory = load_memory()

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)

        try:
            audio = r.listen(source, timeout=5)
        except:
            return ""

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""

    except sr.RequestError:
        print("Speech service error")
        return ""

    except:
        return ""

            

def ask_ai(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

speak("Initializing JARVIS. Systems online. Hello Nanda.")

while True:
    command = listen()

    if not command:
        continue

    if "exit" in command:
        speak("Shutting down. Goodbye Nanda.")
        break

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {time}")
        
    elif "date" in command:
        today = datetime.date.today()
        speak(f"Today's date is {today}")

    elif "open chrome" in command:
        speak("Opening Chrome")
        os.system("start chrome")
    
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    elif "open vs code" in command:
        speak("Opening Visual Studio Code")
        os.system("code")
        
    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")
        
    elif "open calculator" in command:
        speak("Opening Calculator")
        os.system("calc")
    
    elif "open" in command:
        app = command.replace("open", "").strip()
        speak(f"Opening {app}")
        os.system(app)

    elif "play" in command:
        song = command.replace("play", "")
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)
    
    elif "search for" in command:
        search = command.replace("search for", "")
        speak("Searching Google")
        webbrowser.open(f"https://www.google.com/search?q={search}")
        
    elif "clear memory" in command:
        conversation_memory = ""
        save_memory("")
        speak("Memory cleared successfully.")
        
    elif "battery" in command:
        battery = psutil.sensors_battery()
        percent = battery.percent
        speak(f"Battery is at {percent} percent")
    
    elif "shutdown computer" in command:
        speak("Shutting down computer")
        os.system("shutdown /s /t 5")
        
    elif "restart computer" in command:
        speak("Restarting computer")
        os.system("shutdown /r /t 5")
    
    else:
        reply = ask_ai(command)
        speak(reply)