# Jarvis - Python Virtual Assistant

Jarvis is a voice-activated virtual assistant built using Python. It can perform tasks like opening websites, playing songs, reading news, and answering questions using OpenAI's GPT API.

---

## 🔧 Features

- Voice-activated with wake word **"Jarvis"**
- Opens popular websites (Google, YouTube, Instagram, LinkedIn, X, ChatGPT)
- Plays songs from a local music dictionary
- Fetches Indian news headlines using NewsAPI
- AI assistant replies using OpenAI GPT-3.5
- Text-to-speech (TTS) using **`pyttsx3`** (offline), or optionally `gTTS + pygame` (online)

---

## 🧩 Requirements

Install required Python packages:

```bash
pip install speechrecognition pyttsx3 openai requests

Optional (if using gTTS + pygame instead of pyttsx3):
pip install gTTS pygame

🔑 Setup
API Keys:

1. Replace "Api-key" with your NewsAPI key.

2. Replace "***" in OpenAI(api_key="***") with your OpenAI key.

3. Add a file called musicLibrary.py in the same folder:

# musicLibrary.py

music = {
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
    "faded": "https://www.youtube.com/watch?v=60ItHLz5WEA"
    }

🗣️ Text-to-Speech Options
✅ Option 1: pyttsx3 (default - offline)
No internet needed. Already integrated in speak().

import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

🔁 Option 2: gTTS + pygame (online)
Uncomment the alternate speak() function in your code if you prefer this:

from gtts import gTTS
import pygame
import os

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass
    pygame.mixer.music.stop()
    os.remove("temp.mp3")

💬 Usage
Run your assistant:

python main.py

🧠 Example Commands
1. "Jarvis, open Instagram"

2. "Jarvis, play faded"

3. "Jarvis, tell me a joke"

4. "Jarvis, what's the latest news in India?"


"You can use both — pyttsx3 is open-source, and gTTS is free for some days, but may require payment later."

........................................................



