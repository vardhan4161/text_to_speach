# 🎙️ Neural TTS Agent - Indian Language Speech Synthesizer

A production-ready, high-performance Text-to-Speech (TTS) web application featuring a neural speech engine, auto-translation for Indian languages, and a premium Glassmorphism UI.

![Premium UI](https://img.shields.io/badge/UI-Glassmorphism-blueviolet)
![Python](https://img.shields.io/badge/Backend-Python%203.11-blue)
![Framework](https://img.shields.io/badge/Framework-Flask-green)
![TTS](https://img.shields.io/badge/TTS-Edge--Neural-orange)

---

## ✨ Features

- **🧠 Agentic Architecture**: Business logic encapsulated in a standalone `SpeechAgent` for scalability.
- **🔊 Neural Voices**: High-quality **Male & Female** voices powered by Microsoft Edge TTS.
- **🌍 Auto-Translation**: Type in English and convert automatically to your preferred Indian language.
- **🇮🇳 Indian Language Suite**:
  - Telugu (తెలుగు)
  - Hindi (हिंदी)
  - Tamil (தமிழ்)
  - Kannada (ಕನ್ನಡ)
  - Malayalam (മലയാളം)
  - Bengali (বাংলা)
  - Marathi (మరాఠీ)
  - Gujarati (ગુજરાતી)
  - Punjabi (ਪੰਜਾਬੀ)
  - Urdu (اردو)
- **🎨 Modern UI**: Premium glassmorphism design with responsive layout and animated backgrounds.
- **📦 Zero-Setup Local Environment**: Includes pre-installed portable Python and Git runtimes.

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **TTS Engine**: `edge-tts` (Microsoft Neural Voices)
- **Translation**: `deep-translator`
- **Frontend**: Vanilla CSS (Glassmorphism), HTML5, JavaScript
- **Runtimes**: Portable Python 3.11, Portable Git

---

## 🚀 Quick Start

### 1. Run the Application
You don't need to install anything globally! The project includes its own runtime.

```bash
# Run the local Python environment
.\app.sys\python.exe app.py
```

### 2. Access the Application
Open your browser and navigate to:
`http://127.0.0.1:5000`

---

## 📂 Project Structure

```text
tts_agent_app/
│
├── app.py           # Flask Controller
├── agent.py         # Speech Agent (Translation + TTS Logic)
├── requirements.txt # Project Dependencies
├── app.sys/         # Local Python & Git Runtimes
├── templates/       # HTML Templates (UI)
└── static/
    ├── style.css    # Premium Glassmorphism Styles
    └── audio/       # Generated Audio Cache
```

---

## 🤝 Contribution

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

**Developed with ❤️ for Advanced Speech Synthesis.**
