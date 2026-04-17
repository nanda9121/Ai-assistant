import datetime
import webbrowser
import os
import pywhatkit
import psutil

def handle_command(command):
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        return f"The current time is {current_time}"

    if "date" in command:
        today = datetime.date.today()
        return f"Today's date is {today}"

    if "open chrome" in command:
        os.system("start chrome")
        return "Opening Chrome"

    if "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google"

    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    if "open instagram" in command:
        webbrowser.open("https://www.instagram.com")
        return "Opening Instagram"

    if "open vs code" in command:
        os.system("code")
        return "Opening Visual Studio Code"

    if "open notepad" in command:
        os.system("notepad")
        return "Opening Notepad"

    if "open calculator" in command:
        os.system("calc")
        return "Opening Calculator"

    if command.startswith("open "):
        app = command.replace("open", "").strip()
        os.system(app)
        return f"Opening {app}"

    if command.startswith("play "):
        song = command.replace("play", "").strip()
        pywhatkit.playonyt(song)
        return f"Playing {song}"

    if command.startswith("search for "):
        search = command.replace("search for", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={search}")
        return f"Searching Google for {search}"

    if "battery" in command:
        battery = psutil.sensors_battery()
        if battery:
            return f"Battery is at {battery.percent} percent"
        return "Battery information is not available"

    if "shutdown computer" in command:
        os.system("shutdown /s /t 5")
        return "Shutting down computer"

    if "restart computer" in command:
        os.system("shutdown /r /t 5")
        return "Restarting computer"

    return None
