import requests
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import pywhatkit


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
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You:", command)
        return command.lower()
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

    if "exit" in command:
        speak("Shutting down. Goodbye Nanda.")
        break

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {time}")

    elif "open chrome" in command:
        speak("Opening Chrome")
        os.system("start chrome")
    
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "open vs code" in command:
        speak("Opening Visual Studio Code")
        os.system("code")

    elif "play" in command:
        song = command.replace("play", "")
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)
    
    elif "search for" in command:
        search = command.replace("search for", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={search}")
        speak(f"Searching for {search}")
        
    elif "clear memory" in command:
        conversation_memory = ""
        save_memory("")
        speak("Memory cleared successfully.")

    else:
        reply = ask_ai(command)
        speak(reply)