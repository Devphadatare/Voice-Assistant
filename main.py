import pyttsx3          #pip install pyttsx3
import speech_recognition as sr    #This is used to take commands  #pip install speechRecognition
import datetime
import wikipedia         #pip install wikipedia
import webbrowser
import os
import smtplib
from selenium import webdriver
import pyautogui
import time      # We'll use this for a small delay
import openai

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):  # This function allows the pc to speak
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may i help you")


def takeCommand():
    # It takes the microphone input from the user and returns string output

    r = sr.Recognizer()  # This will help to recognize our audio
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete
        # r.energy_threshold = 300      # minimum audio energy to consider for recording
        audio = r.listen(source)  # ye sab sr module se arahi hai

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n ")

    except Exception as e:
        # print(e)            #kabhi kabhi console mein error na dekhe so comment it
        print("Say that again please...")
        return "None"  # ye string mein kyu bcoz its just none
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('devphadtare2003@gmail.com', '')
    server.sendmail('devphadtare2003@gmail.com', to, content)
    server.close()

# Set the path to your web driver. Download the appropriate driver for your browser (e.g., Chrome or Firefox).
# Make sure to specify the path to the driver executable here.
webdriver_path = 'path/to/your/webdriver/executable'

def search_google(query):
    if query:
        try:
            driver = webdriver.Chrome(executable_path=webdriver_path)  # You can use any other supported browser
            driver.get("https://www.google.com")
            search_box = driver.find_element_by_name("q")
            search_box.send_keys(query)
            search_box.submit()
            speak(f"Here are the Google search results for '{query}'.")
        except Exception as e:
            print(e)
        finally:
            driver.quit()

def search_google(query):
    if query:
        try:
            # Open Google in the web browser
            webbrowser.open("https://www.google.com")

            # Wait for the browser to open (you can adjust the delay as needed)
            time.sleep(2)

            # Position the cursor in the search bar and click it
            pyautogui.click(x=600, y=320)  # Adjust the coordinates based on your screen resolution

            # Type the search query
            pyautogui.write(query)
            pyautogui.press("enter")  # Press Enter to perform the search

            speak(f"Here are the Google search results for '{query}'.")
        except Exception as e:
            print(e)
            speak("Sorry, I encountered an error while searching on Google.")

if __name__ == "__main__":
      wishMe()
      # while True:
      if 1:

          query = takeCommand().lower()

         # Logic for executing tasks based on query
          if 'wikipedia' in query:

              speak("Searching Wikipedia...")
              query = query.replace("wikipedia", "")
              results = wikipedia.summary(query, sentences=2)
              speak("According to Wikipedia")
              print(results)
              speak(results)

          elif 'open youtube' in query:
             webbrowser.open("youtube.com")

          elif 'open chatgpt' in query:
             webbrowser.open("https://www.google.com")

          # elif 'open google' in query:
          #    webbrowser.open("google.com")

          elif 'open google' in query:
              webbrowser.open("https://www.google.com")

          elif 'search google' in query:
              # Extract the query to be searched on Google
              search_query = query.replace("search google", "").strip()
              if search_query:
                  search_url = f"https://www.google.com/search?q={search_query}"
                  webbrowser.open(search_url)
                  speak(f"Here are the  results for '{search_query}'.")

          elif 'open google' in query:
              webbrowser.open("https://www.google.com")

          elif 'open stackoverflow' in query:
             webbrowser.open("stackoverflow.com")

          elif 'open amazon' in query:
            webbrowser.open("amazon.com")

          elif 'play music' in query:
             music_dir = 'This PC\\C\\Users\\HP\\videos\\DEV'   #yaha pe perfect path dalo music ka
             songs = os.listdir(music_dir)  # ye mere jetne bhi songs hai usko list karega
             print(songs)
             os.startfile(os.path.join(music_dir, songs[0]))  # khol dega file ko ye music ko pahele se start karega

          elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"Sir, the time is {strTime}")

          elif 'open code' in query:
             codePath = "C:\\Users\\HP\\AppData\\Local\Programs\\Microsoft VS Code\\Code.exe"
             os.startfile(codePath)

          elif 'email to dev' in query:
             try:
                 speak("What should I say?")
                 content = takeCommand()
                 to = "devphadtare1998@gmail.com"
                 sendEmail(to, content)
                 speak("Email has been sent!")
             except Exception as e:
                 print(e)
                 speak("Sorry my friend dev bhai. I am not able to send this email")

           

