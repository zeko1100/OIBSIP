import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen and recognize speech
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Recognized command: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, there seems to be an issue with the service.")
        return ""

# Function to perform actions based on voice commands
def handle_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}.")
    elif "search for" in command:
        search_query = command.replace("search for", "").strip()
        if search_query:
            speak(f"Searching the web for {search_query}.")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
        else:
            speak("Please provide something to search for.")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        return False
    else:
        speak("I'm sorry, I didn't catch that. Could you please repeat?")
    return True

# Main function to run the voice assistant
def main():
    speak("Voice assistant activated. How can I help you?")
    while True:
        command = listen()
        if not handle_command(command):
            break

if __name__ == "__main__":
    main()
