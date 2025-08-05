import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import datetime
import wikipedia
import pywhatkit
import pyjokes
import webbrowser
import os
import uuid

# 🎤 Speak function with faster speech + "Devaaanshh Sir"
def speak(text):
    text = text.replace("Devansh Sir", "Devaaanshh Sir")
    print(f"\n🤖 JARVIS: {text}")
    try:
        tts = gTTS(text=text, lang='en', tld='co.in', slow=False)  # Fast voice
        filename = f"temp_{uuid.uuid4()}.mp3"
        tts.save(filename)
        sound = AudioSegment.from_mp3(filename)
        faster_sound = sound.speedup(playback_speed=1.25)  # 25% faster
        play(faster_sound)
        os.remove(filename)
    except Exception as e:
        print("❌ Voice Error:", e)

# 🎧 Listen function
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎙️ Listening for your command, Devaaanshh Sir...\n")
        speak("I am listening, Devaaanshh Sir")
        try:
            voice = r.listen(source, timeout=5, phrase_time_limit=7)
            command = r.recognize_google(voice).lower()
            print(f"🗣️ You said: {command}")
            return command
        except sr.WaitTimeoutError:
            speak("I didn't catch anything, Devaaanshh Sir.")
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that.")
        except sr.RequestError:
            speak("Speech service is not working right now.")
    return ""

# 💡 Command processing
def run_jarvis():
    command = listen()

    if 'time' in command:
        now = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The current time is {now}")

    elif 'date' in command:
        today = datetime.datetime.now().strftime('%A, %d %B %Y')
        speak(f"Today is {today}")

    elif 'who is' in command or 'what is' in command or 'tell me about' in command:
        topic = command.replace('who is', '').replace('what is', '').replace('tell me about', '')
        try:
            info = wikipedia.summary(topic, sentences=2)
            speak(info)
        except:
            speak("Sorry, I couldn't find anything about that.")

    elif 'play' in command:
        song = command.replace('play', '')
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        speak(joke)

    elif 'open google' in command:
        speak("Opening Google for you.")
        webbrowser.open("https://www.google.com")

    elif 'hello jarvis' in command:
        speak("Hello Devaaanshh Sir, I am Jarvis, your AI assistant. What can I do for you today?")

    elif 'terminate' in command or 'stop' in command or 'exit' in command:
        speak("Goodbye Devaaanshh Sir. Jarvis signing off.")
        exit()

    elif command != "":
        speak("Sorry, I didn’t understand that, Devaaanshh Sir.")

# 🚀 Intro
speak("Jarvis activated.")
speak("Hello Devaaanshh Sir, I am Jarvis, your personal AI assistant.")
speak("I can tell you the time, date, search Wikipedia, play songs, crack jokes, or open Google.")
speak("Say something like 'what is gravity', or 'play Tu Hai Kahan'.")
speak("Say 'terminate' anytime to stop me.")

# 🔁 Keep Running
while True:
    run_jarvis()
