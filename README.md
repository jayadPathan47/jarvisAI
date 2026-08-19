<div align="center">
🤖 JARVIS AI
Your Personal AI Voice Assistant for Windows
<p>
  <img src="https://img.shields.io/badge/Python-3.14+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows">
  <img src="https://img.shields.io/badge/AI-Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white" alt="Gemini">
  <img src="https://img.shields.io/badge/Voice-Whisper-412991?style=for-the-badge" alt="Whisper">
</p>
<p>
  <strong>A modular, voice-controlled AI assistant designed to control your PC, understand natural language, search the web, remember conversations, and see what's on your screen.</strong>
</p>
<p>
  <a href="#-features">Features</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-roadmap">Roadmap</a>
</p>
</div>
---
✨ What is JARVIS?
JARVIS AI is a personal desktop voice assistant built with Python.
The project combines:
🎤 Speech recognition with Faster-Whisper
🧠 AI conversations with Google Gemini
🔊 Natural speech using Edge TTS
⚙️ Windows automation and application control
🌐 Web search
👁️ Screen capture and AI vision
🧠 Persistent local memory
🔥 Wake-word activation with "Hey Jarvis"
The goal is simple:
> **Talk to your computer naturally — JARVIS handles the rest.**
---
🖥️ System Overview
```text
                         ┌──────────────────────┐
                         │      🎤 USER         │
                         │   "Hey Jarvis..."    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   🎙️ VOICE SYSTEM   │
                         │   Microphone + STT   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    🔥 WAKE WORD      │
                         │    "Hey Jarvis"      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                  ┌─────────────────────────────────┐
                  │          🧠 AI BRAIN            │
                  │       Gemini + Memory           │
                  └──────────────┬──────────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              ▼                  ▼                  ▼
      ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
      │ ⚙️ COMMANDS  │   │ 🌐 WEB SEARCH │   │ 👁️ VISION   │
      │ PC Automation│   │ Live Search   │   │ Screen AI    │
      └──────┬───────┘   └──────────────┘   └──────────────┘
             │
             ▼
      ┌────────────────────┐
      │ 💻 WINDOWS SYSTEM  │
      │ Apps • Volume • PC │
      └─────────┬──────────┘
                │
                ▼
      ┌────────────────────┐
      │ 🔊 JARVIS RESPONSE │
      │       Edge TTS     │
      └────────────────────┘
```
---
🚀 Features
Feature	Status
🎤 Voice input	✅
🔥 Wake word detection	✅
🧠 Gemini AI brain	✅
🧠 Persistent memory	✅
🔊 Text-to-speech	✅
🌐 Web search	✅
👁️ Screen vision	✅
📸 Screenshot system	✅
🌐 Open websites	✅
🖥️ Open Windows apps	✅
🔊 Volume control	✅
🔒 Lock computer	✅
🔄 Restart computer	✅
⏻ Shutdown / cancel shutdown	✅
💻 CMD / PowerShell	✅
📝 Notepad / Calculator / Explorer	✅
🛑 Stop command	✅
🧩 Modular architecture	✅
🤖 Advanced automation	🚧
🎨 GUI dashboard	🚧
🏠 Smart-home integration	🔮
📱 Mobile companion app	🔮
---
🧩 Core Modules
```text
jarvis-ai/
│
├── app.py              # 🚀 Main JARVIS loop
├── listener.py         # 🎤 Speech recognition
├── speaker.py          # 🔊 Text-to-speech
├── wakeword.py         # 🔥 Wake-word detection
├── brain.py            # 🧠 AI/Gemini brain
├── memory.py           # 🧠 Persistent memory
├── commands.py         # ⚙️ PC command execution
├── web_search.py       # 🌐 Web search
├── screenshot.py       # 📸 Screenshot capture
├── vision.py           # 👁️ Screen analysis
├── memory.json         # 💾 Local memory
├── .env                # 🔐 API configuration
│
├── test_brain.py       # 🧪 AI tests
└── test_memory.py      # 🧪 Memory tests
```
---
🛠️ Tech Stack
<div align="center">
Technology	Purpose
🐍 Python	Core application
🎙️ Faster-Whisper	Speech-to-text
🧠 Google Gemini	AI reasoning
🔊 Edge TTS	Voice generation
🎧 SoundDevice	Microphone input
🖱️ PyAutoGUI	Desktop automation
🌐 Web Search	Internet search
🖼️ Pillow	Screenshots/images
💾 JSON	Local memory
🪟 Windows APIs	System control
</div>
---
⚡ Installation
1️⃣ Clone the repository
```bash
git clone https://github.com/jayadPathan47/jarvisAI.git
cd jarvisAI
```
2️⃣ Create a virtual environment
```bash
python -m venv .venv
```
Activate it on Windows:
```powershell
.venv\Scripts\Activate.ps1
```
Or CMD:
```cmd
.venv\Scripts\activate
```
3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
If you don't have a requirements file yet:
```bash
pip install sounddevice numpy scipy faster-whisper edge-tts pyautogui python-dotenv google-genai
```
---
🔐 Environment Variables
Create a `.env` file in the project root.
```env
GOOGLE_API_KEY=your_google_gemini_api_key
```
⚠️ Never upload `.env` to GitHub.
Add this to `.gitignore`:
```gitignore
.env
__pycache__/
*.pyc
input.wav
output.mp3
command.wav
```
---
▶️ Run JARVIS
Start the assistant with:
```bash
python app.py
```
You should see:
```text
Starting JARVIS...

🎤 Listening...
🧠 Processing...
You: Hey Jarvis.
✅ Wake word detected

🎤 Listening...
🧠 Processing...
You: Open Chrome.

⚙️ Command: open chrome
🌐 Opening Chrome...
✅ Chrome opened
```
---
🎙️ Example Commands
💻 Applications
```text
Hey Jarvis, open Chrome
Hey Jarvis, open Notepad
Hey Jarvis, open Calculator
Hey Jarvis, open File Explorer
Hey Jarvis, open Settings
```
🌐 Websites
```text
Open Google
Open YouTube
Open GitHub
Search Python tutorials
Search latest technology news
```
🖥️ System
```text
Volume up
Volume down
Mute
Lock computer
Restart computer
Shutdown computer
Cancel shutdown
```
👁️ Vision
```text
What is on my screen?
Describe my screen
Read my screen
What do you see?
Analyze my screen
```
🛑 Control
```text
Stop Jarvis
```
---
🧠 How the AI Pipeline Works
```text
🎤 Voice
   │
   ▼
🔥 Wake Word
   │
   ▼
📝 Speech → Text
   │
   ▼
🧠 Intent / AI Brain
   │
   ├───────────────┐
   ▼               ▼
⚙️ Command       💬 AI Answer
   │               │
   ▼               ▼
💻 Windows       🔊 TTS
   │               │
   └───────┬───────┘
           ▼
       👤 USER
```
---
🧠 Memory System
JARVIS stores useful conversation information locally.
```text
User
 │
 ▼
Conversation
 │
 ▼
Memory System
 │
 ▼
memory.json
 │
 ▼
Future conversations
```
This allows the assistant to maintain context between sessions.
> **Privacy note:** Review the memory implementation before storing sensitive information.
---
👁️ Vision System
JARVIS can capture the current screen and send the screenshot to the vision model for analysis.
Example:
```text
You:
"Jarvis, what is on my screen?"

        ↓

📸 Screenshot

        ↓

👁️ Vision Model

        ↓

🧠 Analysis

        ↓

🔊 Spoken Response
```
This can be useful for understanding:
Applications
Error messages
Buttons
Visible text
Important UI information
---
⚙️ Command Architecture
Commands are handled independently from the AI brain.
```python
execute_command("open chrome")
```
The command system then maps the request to a Windows action.
This separation makes JARVIS easier to extend without modifying the entire application.
---
🧪 Testing
Test the AI brain:
```bash
python test_brain.py
```
Test memory:
```bash
python test_memory.py
```
Test a command directly:
```bash
python -c "from commands import execute_command; execute_command('open chrome')"
```
---
🐛 Troubleshooting
Microphone not detected
Check available audio devices:
```bash
python -c "import sounddevice as sd; print(sd.query_devices())"
```
Then verify that Windows has microphone permission enabled.
Whisper is slow
The project currently uses a CPU configuration:
```python
WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)
```
For better performance, use a smaller Whisper model if your hardware is limited.
Chrome does not open
Check whether Chrome exists at one of these locations:
```text
C:\Program Files\Google\Chrome\Application\chrome.exe
C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
```
Gemini API error
Check:
```text
GOOGLE_API_KEY
```
and make sure the model configured in `brain.py` / `vision.py` is currently available for your API account.
---
🗺️ Roadmap
Phase 1 — Foundation
[x] Python core
[x] Voice input
[x] Text-to-speech
[x] Wake word
[x] Basic commands
Phase 2 — Intelligence
[x] Gemini AI
[x] Memory
[x] Web search
[x] Screen vision
Phase 3 — Automation
[ ] Application launcher
[ ] Keyboard automation
[ ] Mouse automation
[ ] File management
[ ] Process manager
[ ] Smart command routing
[ ] Multi-step task execution
Phase 4 — JARVIS UI
[ ] Futuristic desktop dashboard
[ ] Animated waveform
[ ] Live system stats
[ ] AI activity panel
[ ] Command history
[ ] Memory viewer
[ ] Settings panel
Phase 5 — Advanced JARVIS
[ ] Offline AI mode
[ ] Long-term memory
[ ] Multi-agent architecture
[ ] Smart home integration
[ ] Mobile companion
[ ] Personalized automation
[ ] Plugin system
---
🎨 Future UI Concept
```text
╔══════════════════════════════════════════════════════╗
║                    J A R V I S                       ║
║                                                      ║
║              ◉  SYSTEM ONLINE  ◉                     ║
║                                                      ║
║                 ╭───────────╮                        ║
║              ╭──│  ◉ ◉ ◉   │──╮                     ║
║              │  │   JARVIS  │  │                     ║
║              ╰──│  ◉ ◉ ◉   │──╯                     ║
║                 ╰───────────╯                        ║
║                                                      ║
║   🎤 Listening...                                    ║
║                                                      ║
║   USER     →  Open Chrome                            ║
║   JARVIS   →  Opening Chrome...                     ║
║                                                      ║
║   CPU ███████░░░  72%      RAM █████░░░░░  51%       ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
```
---
🔒 Security
JARVIS can execute powerful operating-system commands.
Do not blindly execute AI-generated commands.
Recommended protections:
Confirm destructive commands
Keep API keys outside source control
Validate file paths
Restrict dangerous system commands
Log executed actions
Add authentication before remote control
Never expose the assistant directly to the public internet
---
🤝 Contributing
Contributions are welcome.
```bash
git checkout -b feature/my-feature
git add .
git commit -m "Add my feature"
git push origin feature/my-feature
```
Then open a Pull Request.
---
⭐ Support the Project
If you like this project:
⭐ Star the repository
🍴 Fork it
🐛 Report bugs
💡 Suggest features
🤝 Contribute
---
📜 License
This project is intended for educational and personal use.
Add an appropriate open-source license to the repository before publishing it as a reusable open-source project.
---
<div align="center">
🤖 JARVIS AI
"Your voice. Your computer. Your AI."
Built with ❤️ and Python.
<br>
⭐ If JARVIS helped you, give the repository a star! ⭐
</div>
