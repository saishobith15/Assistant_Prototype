import speech_recognition as sr
import pyttsx3
import os
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize speech recognizer
r = sr.Recognizer()

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def open_files(drive):
    """Handle file opening logic."""
    try:
        speak("Name the folder or file to open.")
        with sr.Microphone() as source:
            audio = r.listen(source)
            folder_or_file = r.recognize_google(audio).strip()
            path = fr"{drive}:\{folder_or_file}"
            if os.path.exists(path):
                os.startfile(path)
                speak(f"Opening {folder_or_file}.")
            else:
                speak("File or folder not found.")
    except Exception as e:
        speak(f"An error occurred: {str(e)}")

def new_main():
    """Main function for the voice assistant."""
    speak("Hello! I'm your developing assistant. I hope I can help you.")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)
                user_input = r.recognize_google(audio).lower()
                print(f"User said: {user_input}")

                if user_input == 'internet':
                    speak("Opening the internet browser.")
                    webbrowser.open("https://www.google.com")
                elif user_input == 'files':
                    speak("Which drive should I look into, C or D?")
                    with sr.Microphone() as source:
                        audio = r.listen(source)
                        drive = r.recognize_google(audio).lower()
                        if drive in ['c', 'd']:
                            open_files(drive.upper())
                        else:
                            speak("Invalid drive specified.")
                elif user_input in ['exit', 'quit', 'stop']:
                    speak("Goodbye!")
                    break
                else:
                    speak("I didn't understand. Please try again.")
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    new_main()
