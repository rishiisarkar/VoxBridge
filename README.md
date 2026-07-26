# VoxBridge 🎙️

A lightweight Python toolkit for converting text to speech (TTS) and speech to text (STT).

## Features
- 🔊 **Text-to-Speech** — offline, cross-platform voice synthesis using `pyttsx3`
- 🎤 **Speech-to-Text** — transcribe live microphone input or audio files using Google's Speech API
- 🎛️ Adjustable speech rate, volume, and voice selection
- 💾 Export speech to audio files

## Installation
```bash
pip install pyttsx3 SpeechRecognition pyaudio
```

> **Linux users:** `sudo apt-get install portaudio19-dev` before installing pyaudio
> **Mac users:** `brew install portaudio` before installing pyaudio

## Usage

**Text-to-Speech:**
```python
from voxbridge import text_to_speech

text_to_speech("Hello, world!")
```

**Speech-to-Text:**
```python
from voxbridge import speech_to_text_from_mic

result = speech_to_text_from_mic()
print(result)
```

## Requirements
- Python 3.7+
- Internet connection (for Google STT engine)

## License
MIT
