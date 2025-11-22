import speech_recognition as sr
import pyttsx3
import logging
import os
import datetime
import wikipedia
import webbrowser
import random
import subprocess

#Logging configuration
LOG_DIR="logs"
LOG_FILE_NAME="application.log"
os.makedirs(LOG_DIR,exist_ok=True)
log_path=os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

#Activating voice from our system
engine = pyttsx3.init("sapi5")
engine.setProperty('rate', 150)  # Speed percent (can go over 100)
voices = engine.getProperty("voices")

# Set voice (0 = male, 1 = female)
engine.setProperty('voice', voices[1].id)

#This is speak function
def speak(text):
    """_summary_
        This function converts text to voice

    Args:
        text (_type_): _description_
    return 
        voice
    """
    engine.say(text)
    engine.runAndWait()
    

#This function recognize the voice command speech to text
def takeCommand():
    """_summary_
        This function takes microphone input from the user and returns string output
    Returns:
        str: _description_
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        logging.info(e)
        print("Say that again please...")
        return "None"
    return query

def greeting():
    """_summary_
        This function greets the user based on the time of day
    """
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning,Sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon,Sir!")
    else:
        speak("Good Evening,Sir!")
    speak("I am Peya. How can I help you today?")
    
greeting()
  
while True:
    quiry=takeCommand().lower()
    print(quiry)
    
    if 'your name' in quiry:
        speak("My name is Peya")
        logging.info("User asked for assistant's name.")
    elif 'time' in quiry:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
        logging.info("User asked for current time.")
    elif 'how are you' in quiry:
        speak("I am fine, Sir. How can I assist you today?")
        logging.info("User asked how the assistant is doing.")
    elif 'who made you' in quiry or 'who created you' in quiry:
        speak("I was created by an amazing developer and his name is Mijanur Rahman.")
        logging.info("User asked about the creator of the assistant.")
    elif 'thank you' in quiry:
        speak("You are welcome, Sir!")
        logging.info("User expressed gratitude.")
    elif 'open google' in quiry:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
        logging.info("User requested to open Google.")
    #Calculator opening
    elif 'open calculator' in quiry:
        subprocess.Popen('calc.exe')
        speak("Opening Calculator")
        logging.info("User requested to open Calculator.")
    #Opening notepad
    elif 'open notepad' in quiry:
        subprocess.Popen('notepad.exe')
        speak("Opening Notepad")
        logging.info("User requested to open Notepad.")
    #Opening command prompt
    elif 'open terminal' in quiry or 'open command prompt' in quiry:
        subprocess.Popen('cmd.exe')
        speak("Opening Command Prompt")
        logging.info("User requested to open Command Prompt.")
    #Opening Google Calendar
    elif 'open calendar' in quiry:
        webbrowser.open("https://calendar.google.com")
        speak("Opening Google Calendar")
        logging.info("User requested to open Google Calendar.")
    #YouTube searching
    elif 'open youtube' in quiry:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
        logging.info("User requested to open YouTube.")
    #Facebook opening
    elif 'open facebook' in quiry:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook")
        logging.info("User requested to open Facebook.")
    elif 'joke' in quiry:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't skeletons fight each other? They don't have the guts!"
        ]
        joke = random.choice(jokes)
        speak(joke)
        logging.info("User requested a joke.")
    #Wikipedia search
    elif 'wikipedia' in quiry:
        speak("Searching Wikipedia...")
        quiry = quiry.replace("wikipedia", "")
        results = wikipedia.summary(quiry, sentences=3)
        speak("According to Wikipedia")
        speak(results)
        logging.info("User requested a Wikipedia search.")
    
    #Weather information
    elif 'weather' in quiry:
        webbrowser.open("https://www.weather.com")
        speak("Opening Weather Information")
        logging.info("User requested weather information.")
    #Play music on YouTube randomly
    elif 'play music' in quiry:
        music_list = [
            "https://www.youtube.com/watch?v=3JZ4pnNtyxQ",  # Example music links
            "https://www.youtube.com/watch?v=LsoLEjrDogU",
            "https://www.youtube.com/watch?v=fLexgOxsZu0"
        ]
        music_link = random.choice(music_list)
        webbrowser.open(music_link)
        speak("Playing music on YouTube")
        logging.info("User requested to play music.")
    #Exiting the application
    elif 'exit' in quiry or 'quit' in quiry:
        speak("Goodbye, Sir! Have a great day.")
        logging.info("User exited the application.")
        exit()
    #Default response for unsupported questions
    else:
        speak("I am sorry, I can only respond to questions about my name right now.")
        logging.info("User asked an unsupported question.")