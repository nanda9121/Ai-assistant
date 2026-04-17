from speech import speak, listen
from llm import ask_ai
from memory import memory_as_text, clear_memory, add_fact
from retrieval import retrieve_context
from commands import handle_command

def main():
    speak("Initializing JARVIS. Systems online. Hello Nanda.")

    while True:
        command = listen()

        if not command:
            continue

        if "exit" in command:
            speak("Shutting down. Goodbye Nanda.")
            break

        if "clear memory" in command:
            clear_memory()
            speak("Memory cleared successfully.")
            continue

        if command.startswith("remember that "):
            fact = command.replace("remember that", "").strip()
            add_fact(fact)
            speak("Okay, I will remember that.")
            continue

        command_response = handle_command(command)
        if command_response:
            speak(command_response)
            continue

        memory_text = memory_as_text()
        retrieved_context = retrieve_context(command)

        reply = ask_ai(
            user_input=command,
            memory_text=memory_text,
            retrieved_context=retrieved_context
        )
        speak(reply)

if __name__ == "__main__":
    main()
