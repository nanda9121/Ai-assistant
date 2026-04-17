import requests

MODEL_NAME = "llama3"
OLLAMA_URL = "http://localhost:11434/api/generate"

def build_prompt(user_input, memory_text="", retrieved_context=""):
    return f"""
You are JARVIS, a helpful AI voice assistant.

Known user memory:
{memory_text}

Retrieved context:
{retrieved_context}

User input:
{user_input}

Instructions:
- Reply clearly and naturally.
- Use retrieved context if relevant.
- Keep answers concise.
- If unsure, say you are not fully sure.
"""

def ask_ai(user_input, memory_text="", retrieved_context=""):
    prompt = build_prompt(user_input, memory_text, retrieved_context)

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )
        response.raise_for_status()
        data = response.json()
        return data.get("response", "I could not generate a response.")
    except requests.exceptions.ConnectionError:
        return "I could not connect to Ollama. Please make sure Ollama is running."
    except requests.exceptions.Timeout:
        return "The AI model took too long to respond."
    except Exception as e:
        return f"Something went wrong: {str(e)}"
