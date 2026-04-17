🤖 AI Voice Assistant (LLM + Memory + RAG)

An intelligent voice-based AI assistant built using Python and Ollama (LLM) that supports real-time interaction, command execution, persistent memory, and basic Retrieval-Augmented Generation (RAG).

🚀 Features

- 🎤 Voice input using Speech Recognition  
- 🔊 Text-to-speech output using pyttsx3  
- 🤖 LLM-powered responses (Ollama - LLaMA3)  
- 🧠 Persistent memory system (JSON-based)  
- 📂 Context-aware responses using basic RAG  
- 🌐 Web automation (open websites, search Google)  
- ⚙️ System commands (battery status, shutdown, restart)  
- 📝 Knowledge retrieval from local files  


🧠 How It Works

1. User speaks a command  
2. Speech is converted to text  
3. System checks for predefined commands  
4. Retrieves relevant context (RAG)  
5. Adds memory + context into prompt  
6. Sends prompt to LLM (Ollama)  
7. Generates response  
8. Speaks output  

---

🛠 Tech Stack

- Python
- Ollama (LLaMA3)
- SpeechRecognition
- pyttsx3
- Requests
- psutil
- pywhatkit
