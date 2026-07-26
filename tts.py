import pyttsx3

def text_to_speech(text, rate=150, volume=1.0, voice_index=0):
    engine = pyttsx3.init()
    
    # Configure voice properties
    engine.setProperty('rate', rate)      # Speed of speech
    engine.setProperty('volume', volume)  # Volume (0.0 to 1.0)
    
    voices = engine.getProperty('voices')
    if voice_index < len(voices):
        engine.setProperty('voice', voices[voice_index].id)
    
    engine.say(text)
    engine.runAndWait()

def save_to_file(text, filename="output.mp3"):
    engine = pyttsx3.init()
    engine.save_to_file(text, filename)
    engine.runAndWait()
    print(f"Saved audio to {filename}")

if __name__ == "__main__":
    text_to_speech("Hello! This is a text to speech demo.")
    # save_to_file("Hello! This will be saved as a file.")
