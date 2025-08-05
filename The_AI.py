import speech_recognition as sr
import edge_tts
import asyncio
import datetime
import wikipedia
import pywhatkit
import pyjokes
import webbrowser
import os
from playsound import playsound

VOICE = "hi-IN-MadhurNeural"
SPEED = "+52%"
PITCH = "-25Hz"

# 🎙️ Speak Function
async def talk(text):
    print(f"\n🤖 DeeDee AI: {text}")
    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE,
        rate=SPEED,
        pitch=PITCH
    )
    await communicate.save("temp.mp3")
    playsound("temp.mp3")
    os.remove("temp.mp3")

# 🎧 Listen Function
async def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎙️ I'm listening, Deevaaanshh sir...")
        await talk("I am listening sir ...................")
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=15)
            command = recognizer.recognize_google(audio, language="en-IN")  # understands Hindi+English
            command = command.lower()
            print(f"🗣️ You said: {command}")
            return command
        except:
            await talk("I apologize, I couldn’t understand. Kindly repeat, Devaaanshh sir.")
            return ""

# 👋 Greeting
async def greet():
    await talk("Greetings Deevaaanshh sir. I am DeeDee, your personal AI assistant.")
    await talk("I can play music, fetch time and date, tell jokes,access Wikipedia , and search on web")
    await talk("You may speak in English, Hindi, or both. I'm ready.")

# 🔁 Main Logic
async def run_deedee():
    await greet()
    while True:
        command = await listen()

        if command == "":
            continue
        elif "band" in command or "terminate" in command or "shut" in command or "exit" in command:
            await talk("Acknowledged. Shutting down, Deevaaanshh sir. Thank you for your precious time. I am always here to help you. See you soon sir")
            break
        
        elif "time" in command or "samay" in command or "kitna baje" in command:
            time_now = datetime.datetime.now().strftime('%I:%M %p')
            await talk(f"The time now is {time_now}, Deevaaanshh sir.")
        elif "date" in command or "aaj" in command or "tareekh" in command:
            date_today = datetime.datetime.now().strftime('%A, %d %B %Y')
            await talk(f"Today is {date_today}, Deevaaanshh sir.")
        elif "who is" in command or "what is" in command or "kaun hai" in command or "bata" in command:
            topic = command.replace("who is", "").replace("what is", "").replace("kaun hai", "").replace("tell me about", "").strip()
            try:
                info = wikipedia.summary(topic, sentences=2)
                await talk(info)
            except:
                await talk("Apologies, Deevaaanshh sir. I couldn’t find relevant details.")
        elif "play" in command or "baja" in command or "gaana" in command:
            song = command.replace("play", "").replace("baja", "").replace("gaana", "").strip()
            await talk(f"Playing {song} on YouTube for you, Deevaaanshh sir.")
            pywhatkit.playonyt(song)
        elif "joke" in command or "majak" in command or "mazaak" in command or "chutkula" in command:
            joke = pyjokes.get_joke()
            await talk(f"Here's a joke for you, Deevaaanshh sir: {joke}")
        elif "google" in command or "chrome" in command or "google khol" in command:
            await talk("Opening Google in your browser, Deevaaanshh sir.")
            webbrowser.open("https://search.brave.com/search?q=google")
             # 👇 New command: About DeeDee
        elif "who are you" in command or "tell me about yourself" in command  or "hu r u" in command or "about yourself" in command:
            await talk("I am DeeDee, your advanced virtual assistant. I was created to serve you, Deevaaanshh sir, with intelligence, precision, and a bit of charm.")
        elif "search" in command:
            query = command.replace("search", "").replace("on google", "").strip()
            if query:
                await talk(f"Searching for {query} on Google, Deevaaanshh sir.")
                webbrowser.open(f"https://search.brave.com/search?q={query}")
            else:
                await talk("Deevaaanshh sir, please specify what you want me to search.")

        # 👇 New command: About YOU
        elif "who am i" in command or "tell me about me" in command or "hu m i" in command or "about me" in command:
            await talk("You are Deevaaanshh Dubey sir — a tall, intelligent and ambitious engineer in the making. Passionate about coding, tech, and learning new things and I’m here to help you sir                                                       ")
        else:
            await talk("I'm unable to process that command. Please try again, Deevaaanshh sir.")

# 🚀 Start Assistant
if __name__ == "__main__":
    asyncio.run(run_deedee())
  