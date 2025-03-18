# import os for further update 
# Gemini 1.5 flash API is free
import speech_recognition as sr
import webbrowser
import pyttsx3
import groq
import requests
import musicLibrary


# for queries in brave browser f"https://search.brave.com/search?q={query.replace(" ","+")}&source=desktop"

with open("API_KEY_NEWS.txt") as f:
    newsapi = f.read()

with open("GROQ_API_KEY.txt") as f:
    groq_api = f.read()

groq_client = groq.Client(api_key = groq_api)

songs = musicLibrary.music

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook")
    elif "open youtube" in c.lower():
        speak("Opening Yoututbe")
        webbrowser.open("https://youtube.com")
    elif "play music" in c.lower():
        speak("Select a playlist: ")
    
        # Display available playlists
        for playlist_name in songs.keys():
            print(playlist_name)

        # Initialize the speech recognizer
        rec = sr.Recognizer()

        try:
            with sr.Microphone() as source:  # Corrected "Microphone as Source" to "Microphone() as source"
                print("Listening...")
                audio = rec.listen(source, timeout=5)
        
            # Recognize the playlist name from speech
            playlist = rec.recognize_google(audio)
            print(f"You said: {playlist}")

            # Match the recognized playlist with your dictionary
            for key in songs.keys():
                if key.lower() in playlist.lower():
                    webbrowser.open(songs[key])
                    speak(f"Playing {key} playlist.")
                    break
            else:
                speak("Playlist not found. Please try again.")
    
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please try again.")
        except sr.RequestError as e:
            speak(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            speak(f"An error occurred: {e}")

    elif "news" in c.lower():
        speak("Searching top headlines")
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
            r.raise_for_status()  # Raise an error for non-200 status codes
            data = r.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching news: {e}")
            speak("Unable to fetch the news at the moment. Please check your internet connection or API key.")
            return

        # Extract articles
        articles = data.get("articles", [])
        if not articles:
            speak("No news articles were found.")
            return

    # Read headlines (limit to 5 articles)
        max_articles = 5
        for i, article in enumerate(articles[:max_articles]):
            title = article.get("title", "No title available")
            print(f"{i + 1}. {title}")
            speak(title)

    else:
        # Let AI handle the request
        # For now the query is handled by brave browser
        # try:
        #     response = groq_client.analyze_text(c)
        #     intent = response["intent"]
        #     speak(f"I understood your intent as {intent}")
            
        #     # Add Groq intent-specific responses here
        #     if intent == "greeting":
        #         speak("Hello! How can I assist you?")
        #     elif intent == "weather":
        #         speak("Fetching the weather for you...")
        #         # Example: Call a weather API
        # except Exception as e:
        #     print(f"Groq API error: {e}")
        #     speak("I couldn't understand that.")
        speak(f"Searching {c} on Brave....")
        query = f"https://search.brave.com/search?q={c.replace(' ','+')}&source=desktop"
        webbrowser.open(query)

if __name__ == "__main__":
    speak("Initializing Assistant....")
    power_on = True
    while power_on:
        # Listen for the wake word "start"
        # obtain audio from the microphone 
        r = sr.Recognizer()
        
        print("recognizing....")
        # recognise speech using Google
        try:
            with sr.Microphone() as source:
               print("Listening....")
               audio = r.listen(source, timeout = 5)
            word = r.recognize_google(audio)
            if(word.lower() == "start" or word.lower() == "jarvis"):
                speak("Hello User!")
                # Listen for command
                with sr.Microphone() as source:
                    print("Assistant Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
            elif(word.lower() == "exit"):
                speak("Power off....")
                print("Power off....")
                power_on = False
        except Exception as e:
            print("error: {0}".format(e))