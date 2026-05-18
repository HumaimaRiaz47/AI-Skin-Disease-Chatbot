# 🩺 AI Skin Disease Chatbot

An intelligent **AI-powered Skin Disease Chatbot** built with **Generative AI, Computer Vision, Speech Recognition, and Text-to-Speech** technologies.

This chatbot can:

- 👁️ Analyze skin disease images
- 🎤 Understand patient voice input
- 🧠 Generate AI-based medical responses
- 🔊 Reply with realistic AI voice
- 🌐 Run inside an interactive Gradio web interface

Built using:

- Python
- Llama 3 Vision
- Whisper
- Groq API
- Gradio
- gTTS / ElevenLabs

---

# 🚀 Features

✅ AI Skin Disease Assistant  
✅ Voice-to-Text using Whisper  
✅ Text-to-Speech Response  
✅ Skin Image Understanding  
✅ Gradio Web Interface  
✅ Real-time AI Conversation  
✅ Open Source & Beginner Friendly  
✅ Cross Platform Support (Windows/macOS/Linux)

---

# 🏗️ Project Architecture

```text
Patient Voice/Image
        │
        ▼
Speech-to-Text (Whisper)
        │
        ▼
Multimodal LLM (Llama Vision)
        │
        ▼
AI Skin Disease Analysis
        │
        ▼
Text-to-Speech
        │
        ▼
Doctor Voice Output
```

---

# 📂 Project Structure

```bash
├── brain_of_the_doctor.py
├── voice_of_the_patient.py
├── voice_of_the_doctor.py
├── gradio_app.py
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core Programming Language |
| Groq API | Fast LLM Inference |
| Llama 3 Vision | Multimodal AI Model |
| Whisper | Speech Recognition |
| gTTS / ElevenLabs | Voice Generation |
| Gradio | Web Interface |
| FFmpeg | Audio Processing |
| PortAudio | Audio Input/Output |

---

# 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

---

# 🛠️ Installation Guide

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/ai-skin-disease-chatbot.git
cd ai-skin-disease-chatbot
```

---

# 2️⃣ Install FFmpeg and PortAudio

## macOS

### Install Homebrew (if not installed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Install Dependencies

```bash
brew install ffmpeg portaudio
```

---

## Linux (Ubuntu/Debian)

### Update Packages

```bash
sudo apt update
```

### Install Dependencies

```bash
sudo apt install ffmpeg portaudio19-dev
```

---

## Windows

### Install FFmpeg

1. Visit:
   https://ffmpeg.org/download.html

2. Download the latest Windows static build.

3. Extract it to:

```text
C:\ffmpeg
```

4. Add this path to Environment Variables:

```text
C:\ffmpeg\bin
```

---

### Install PortAudio

1. Visit:
   http://www.portaudio.com/download.html

2. Download and install PortAudio binaries.

---

# 🐍 Python Environment Setup

You can use **Pipenv**, **venv**, or **Conda**.

---

## Option 1 — Using Pipenv

### Install Pipenv

```bash
pip install pipenv
```

### Install Dependencies

```bash
pipenv install
```

### Activate Environment

```bash
pipenv shell
```

---

## Option 2 — Using pip and venv

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### macOS/Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### Install Requirements

```bash
pip install -r requirements.txt
```

---

## Option 3 — Using Conda

### Create Environment

```bash
conda create --name myenv python=3.11
```

### Activate Environment

```bash
conda activate myenv
```

### Install Requirements

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

## Phase 1 — Brain of the Doctor

Runs the multimodal AI reasoning engine.

```bash
python brain_of_the_doctor.py
```

---

## Phase 2 — Voice of the Patient

Converts patient speech into text.

```bash
python voice_of_the_patient.py
```

---

## Phase 3 — Voice of the Doctor

Converts AI response into voice output.

```bash
python voice_of_the_doctor.py
```

---

## Phase 4 — Launch Gradio App

Starts the complete chatbot UI.

```bash
python gradio_app.py
```

---

# 🌐 Gradio Interface

Once the application starts, open:

```text
http://127.0.0.1:7860
```

---

# 🧠 How It Works

1. User uploads a skin image or speaks through microphone
2. Whisper converts voice → text
3. Llama Vision analyzes skin image + prompt
4. AI generates a medical response
5. Text-to-Speech converts response → audio
6. Gradio displays the complete interaction

---

# 📸 Demo Use Cases

- 🩺 Skin disease analysis
- 📋 Skin condition explanation
- 🧠 Dermatology assistant
- 🎤 Voice-based AI consultation
- 👁️ Skin image interpretation
- 🤖 AI healthcare assistant MVP

---

# ⚠️ Disclaimer

> This project is for educational and research purposes only.
> It should NOT be used as a replacement for professional medical advice, diagnosis, or treatment.

---
# 🎥 Demo Video

https://github.com/HumaimaRiaz47/AI-Skin-Disease-Chatbot/assets/demo.mp4
---

# ⭐ Support

If you found this project helpful:

⭐ Star the repository  
🍴 Fork the project  
📢 Share it with others

---

# 👨‍💻 Author

Developed with ❤️ using Generative AI and Python.

---

# 📄 License

This project is licensed under the MIT License.