import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia

engine = pyttsx3.init()
engine.setProperty('rate', 200)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your voice assistant.... How can I assist you today?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    return query.lower()

def main():
    greet()

    while True:
        query = take_command()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")

        elif "open google" in query:
            webbrowser.open("https://www.google.com")

        elif "time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {current_time}")

        elif "music" in query or "song" in query:
            speak("Playing music")
            webbrowser.open("https://www.spotify.com")  
            
        else:
            speak("I don't understand. Let me search it for you.")
            webbrowser.open(f"https://www.google.com/search?q={query}")

if __name__ == "__main__":
    main()
