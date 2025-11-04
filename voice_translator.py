import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound
import os

def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print(" Speak something...")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    print("Voice captured. Processing...")
    
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print(" Could not understand audio.")
        return None
    except sr.RequestError:
        print(" Network error.")
        return None

def translate_text(text, target_lang='en'):
    translator = Translator()
    translated = translator.translate(text, dest=target_lang)
    print(f" Translated ({translated.dest}): {translated.text}")
    return translated.text

def speak_text(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")
    playsound.playsound("output.mp3")
    os.remove("output.mp3")

if __name__ == "__main__":
    original_text = listen()
    if original_text:
        translated = translate_text(original_text, target_lang='en')  # change 'en' to your desired language
        speak_text(translated, lang='en')
