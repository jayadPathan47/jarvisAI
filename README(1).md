<div align="center">

# JARVIS AI

**A modular, voice-first AI desktop assistant for Windows.**

Control your computer, interact with an AI brain, search the web, manage persistent memory, and analyze your screen — through natural voice commands.

<br>

[![Python](https://img.shields.io/badge/Python-3.14%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Windows](https://img.shields.io/badge/Platform-Windows-0078D6?style=flat-square&logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![Gemini](https://img.shields.io/badge/AI-Gemini-8E75B2?style=flat-square&logo=google&logoColor=white)](https://ai.google.dev/)
[![Whisper](https://img.shields.io/badge/STT-Faster--Whisper-412991?style=flat-square)](https://github.com/SYSTRAN/faster-whisper)
[![Status](https://img.shields.io/badge/Status-Active%20Development-orange?style=flat-square)](#roadmap)

</div>

---

## Overview

JARVIS AI is a Python-based personal desktop assistant designed around a simple principle:

> **Speak naturally. Let JARVIS translate intent into action.**

The project is intentionally split into independent modules so that voice recognition, AI reasoning, memory, automation, web search, vision, and speech output can evolve without turning the application into a single monolithic script.

### Current capabilities

- Wake-word driven voice interaction
- English speech-to-text using Faster-Whisper
- AI responses through Google Gemini
- Local persistent memory
- Text-to-speech responses
- Windows application and system control
- Web search and browser actions
- Screenshot capture
- AI-powered screen analysis
- Modular command routing

---

## Architecture

```text
┌──────────────────────────────────────────────────────────┐
│                        JARVIS AI                         │
└───────────────────────────┬──────────────────────────────┘
                            │
                    ┌───────▼────────┐
                    │  Voice Input   │
                    │ SoundDevice +  │
                    │ Faster-Whisper │
                    └───────┬────────┘
                            │
                    ┌───────▼────────┐
                    │   Wake Word    │
                    │  "Hey Jarvis"  │
                    └───────┬────────┘
                            │
              ┌─────────────▼─────────────┐
              │       Command Router      │
              └─────────────┬─────────────┘
                            │
       ┌────────────────────┼────────────────────┐
       │                    │                    │
┌──────▼──────┐      ┌──────▼──────┐      ┌──────▼──────┐
│   Commands  │      │  AI Brain   │      │    Vision   │
│   Windows   │      │   Gemini    │      │  Screenshot │
│ Automation  │      │  Reasoning  │      │   Analysis  │
└──────┬──────┘      └──────┬──────┘      └──────┬──────┘
       │                    │                    │
       └────────────────────┼────────────────────┘
                            │
                    ┌───────▼────────┐
                    │     Memory     │
                    │   memory.json  │
                    └───────┬────────┘
                            │
                    ┌───────▼────────┐
                    │  Voice Output  │
                    │    Edge TTS    │
                    └────────────────┘
```

---

## Project Structure

```text
jarvis-ai/
│
├── app.py                 # Application entry point
│
├── listener.py            # Microphone capture + speech recognition
├── speaker.py             # Text-to-speech output
├── wakeword.py            # Wake-word detection
│
├── brain.py               # AI reasoning / Gemini integration
├── memory.py              # Persistent memory management
├── memory.json             # Local memory store
│
├── commands.py             # Windows command and automation router
├── web_search.py           # Web search integration
├── screenshot.py           # Screenshot capture
├── vision.py               # Screen/image analysis
│
├── test_brain.py           # AI integration tests
├── test_memory.py          # Memory tests
│
├── .env                    # Local secrets — never commit
├── README.md               # Project documentation
└── .gitignore              # Git exclusions
```

---

## Request Lifecycle

A typical interaction follows this pipeline:

```text
Microphone
    │
    ▼
Audio Capture
    │
    ▼
Faster-Whisper
    │
    ▼
"Hey Jarvis"
    │
    ▼
Wake Word Detection
    │
    ▼
User Command
    │
    ├──► Local Command ──► Windows / Browser / Automation
    │
    ├──► Web Request ────► Search / Browser
    │
    ├──► Vision Request ─► Screenshot ─► AI Analysis
    │
    └──► General Query ──► Gemini ──► Response
                                      │
                                      ▼
                                  Memory
                                      │
                                      ▼
                                   Edge TTS
```

This separation keeps deterministic computer actions independent from open-ended AI responses.

---

## Features

| Area | Capability | Status |
|---|---|:---:|
| Voice | Microphone input | ✅ |
| Voice | English speech recognition | ✅ |
| Voice | Text-to-speech | ✅ |
| Voice | Wake-word activation | ✅ |
| AI | Gemini integration | ✅ |
| Memory | Persistent local memory | ✅ |
| Automation | Windows application control | ✅ |
| Automation | Volume / lock / restart / shutdown | ✅ |
| Browser | Open websites | ✅ |
| Search | Web search | ✅ |
| Vision | Screenshot capture | ✅ |
| Vision | Screen analysis | ✅ |
| Developer | Modular architecture | ✅ |
| UI | Desktop dashboard | 🚧 |
| Automation | Advanced multi-step workflows | 🚧 |
| AI | Offline AI fallback | 🚧 |
| Extensibility | Plugin system | 🔮 |
| Mobile | Companion application | 🔮 |

---

## Technology Stack

| Component | Technology |
|---|---|
| Language | Python |
| Speech-to-text | Faster-Whisper |
| AI | Google Gemini |
| Text-to-speech | Edge TTS |
| Audio | SoundDevice / NumPy / SciPy |
| Desktop automation | PyAutoGUI |
| Browser control | WebBrowser / subprocess |
| Image handling | Pillow |
| Memory | JSON |
| Platform | Windows |

---

## Installation

### Prerequisites

- Windows 10/11
- Python 3.14+
- Working microphone
- Internet connection for Gemini/web features
- Google Gemini API key

### 1. Clone the repository

```bash
git clone https://github.com/jayadPathan47/jarvisAI.git
cd jarvisAI
```

### 2. Create a virtual environment

PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Command Prompt:

```cmd
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

If `requirements.txt` exists:

```bash
pip install -r requirements.txt
```

Otherwise, install the core dependencies:

```bash
pip install sounddevice numpy scipy faster-whisper edge-tts pyautogui python-dotenv google-genai
```

### 4. Configure environment variables

Create `.env` in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Do not commit this file.

---

## Running JARVIS

```bash
python app.py
```

Expected startup:

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

## Example Commands

### Applications

```text
Hey Jarvis, open Chrome
Open Notepad
Open Calculator
Open File Explorer
Open Settings
Open Command Prompt
Open PowerShell
```

### Web

```text
Open Google
Open YouTube
Open GitHub
Search Python tutorials
Search latest technology news
```

### System

```text
Volume up
Volume down
Mute
Lock computer
Restart computer
Shutdown computer
Cancel shutdown
```

### Vision

```text
What is on my screen?
Describe my screen
Read my screen
What do you see?
Analyze my screen
```

### Session control

```text
Stop Jarvis
```

---

## Memory

JARVIS uses a local JSON-based memory layer.

```text
Conversation
     │
     ▼
Memory Manager
     │
     ▼
memory.json
     │
     ▼
Future context
```

Keeping memory local makes the storage layer simple and transparent.

**Important:** Do not store passwords, API keys, authentication tokens, or other sensitive secrets in `memory.json`.

---

## Vision

The vision subsystem can capture the current desktop and send the image to the configured vision-capable AI model.

Example flow:

```text
"Jarvis, analyze my screen."
             │
             ▼
      Capture Screenshot
             │
             ▼
       Vision Model
             │
             ▼
      Structured Analysis
             │
             ▼
        Voice Response
```

Typical use cases include identifying visible applications, reading errors, locating UI elements, and summarizing important on-screen information.

---

## Command System

Local commands are handled deterministically wherever possible.

Example:

```python
execute_command("open chrome")
```

The command router checks the normalized request and maps it to a specific action.

This is preferable to allowing an AI model to directly execute arbitrary shell commands.

### Design principle

```text
Natural Language
       │
       ▼
Intent Detection
       │
       ▼
Validated Command
       │
       ▼
Specific Windows Action
```

---

## Development

Run the individual test modules when making changes:

```bash
python test_brain.py
python test_memory.py
```

Test a command without starting the complete assistant:

```bash
python -c "from commands import execute_command; execute_command('open chrome')"
```

For debugging microphone input:

```bash
python -c "import sounddevice as sd; print(sd.query_devices())"
```

---

## Performance Notes

JARVIS currently uses a CPU-oriented Faster-Whisper configuration:

```python
WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)
```

Recognition latency depends on CPU performance, recording duration, model size, microphone quality, and background noise.

For lower latency on weaker hardware, a smaller speech model can be considered. For higher accuracy, a larger model may be appropriate if the hardware can support it.

---

## Security

JARVIS has access to system-level functionality. Treat it as a privileged local application.

Recommended safeguards:

- Keep API keys in `.env`
- Never commit `.env`
- Validate destructive commands
- Require confirmation for shutdown/restart operations
- Avoid executing arbitrary AI-generated shell commands
- Keep logs of sensitive automation actions
- Restrict remote access unless authentication is implemented
- Review memory contents before sharing the repository

Example `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc

input.wav
output.mp3
command.wav

memory.json
```

---

## Roadmap

### Phase 1 — Core Assistant

- [x] Voice input
- [x] Speech recognition
- [x] Text-to-speech
- [x] Wake word
- [x] Basic Windows commands

### Phase 2 — Intelligence

- [x] Gemini AI
- [x] Persistent memory
- [x] Web search
- [x] Vision integration

### Phase 3 — Automation

- [ ] Application discovery
- [ ] File management
- [ ] Keyboard automation
- [ ] Mouse automation
- [ ] Process management
- [ ] Multi-step workflows
- [ ] Better intent routing

### Phase 4 — User Interface

- [ ] Futuristic desktop dashboard
- [ ] Live audio waveform
- [ ] Command history
- [ ] AI activity stream
- [ ] System monitoring
- [ ] Memory management UI
- [ ] Settings panel

### Phase 5 — Advanced Platform

- [ ] Offline AI fallback
- [ ] Plugin architecture
- [ ] Long-term contextual memory
- [ ] Smart-home integration
- [ ] Mobile companion
- [ ] User authentication
- [ ] Configurable automation policies

---

## UI Direction

The planned interface follows a restrained futuristic style rather than a purely decorative "movie UI":

```text
┌─────────────────────────────────────────────────────┐
│  JARVIS                              SYSTEM ONLINE ● │
├─────────────────────────────────────────────────────┤
│                                                     │
│                 ┌──────────────┐                    │
│                 │      ◉       │                    │
│                 │    JARVIS    │                    │
│                 │      ◉       │                    │
│                 └──────────────┘                    │
│                                                     │
│  STATUS                                             │
│  Listening...                                       │
│                                                     │
│  COMMAND                                            │
│  "Open Chrome"                                      │
│                                                     │
│  ACTIVITY                                           │
│  ✓ Wake word detected                               │
│  ✓ Command recognized                               │
│  ✓ Chrome launched                                 │
│                                                     │
│  CPU  ███████░░░   RAM  █████░░░░░                  │
└─────────────────────────────────────────────────────┘
```

The UI is planned as a monitoring and control layer over the existing modular backend.

---

## Contributing

Contributions are welcome.

### Workflow

```bash
git checkout -b feature/your-feature
```

Make your changes, test them, then:

```bash
git add .
git commit -m "feat: add your feature"
git push origin feature/your-feature
```

Open a Pull Request with:

- What changed
- Why it changed
- How it was tested
- Any known limitations

### Commit style

Recommended:

```text
feat: add application launcher
fix: improve microphone handling
refactor: separate command routing
docs: update installation guide
test: add memory regression tests
```

---

## Project Principles

JARVIS is being developed around a few engineering principles:

**Modular** — each subsystem should have a clear responsibility.

**Deterministic** — computer-control actions should be validated and predictable.

**Extensible** — new capabilities should be addable without rewriting the core loop.

**Observable** — important actions and failures should be easy to diagnose.

**Privacy-aware** — secrets and local memory should remain outside source control.

---

## License

No open-source license has been selected yet.

If this repository is intended for public reuse, add a license file such as MIT before accepting external contributions.

---

<div align="center">

## JARVIS AI

**Voice → Intent → Action → Intelligence**

Built with Python.

<br>

If you find the project useful, consider giving it a ⭐.

</div>
