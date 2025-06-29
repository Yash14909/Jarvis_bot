import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
#from gtts import gTTS
#import pygame
#import os

recognizer=sr.Recognizer()
engine = pyttsx3.init()
newsapi ="Api-key"  #API key for news

    
def speak(text): #if you access gttS then make this speak--> speak_old
    engine.say(text)
    engine.runAndWait()

#def speak(text):
    #tts = gTTS(text)
    #tts.save('temp.mp3')

    #pygame.mixer.init()
    #pygame.mixer.music.load("temp.mp3")
    #pygame.mixer.music.play()

    #while pygame.mixer.music.get_busy():
        #pass  # Wait while playing

   # pygame.mixer.music.stop()  # ✅ Stop the playback before deleting
    #os.remove("temp.mp3")      # ✅ Now it's safe to delete


def aiProcess(command):
    client = OpenAI (api_key="***")
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
       {"role":"system", "content":"you are a virtual assistant named Jarvis skilled in general tasks like Alexa and google cloud "}, 
       {"role":"user","content": command}
        ]
    )
    return completion.choices[0].message.content
 

def processCommand(c):           
    if "open google" in c.lower():       #if else loop for access of diff platforms
        webbrowser.open("https://google.com")
    elif "open instagram" in c.lower():   
        webbrowser.open("https://www.instagram.com/?next=%2F")
    elif "open linkedin" in c.lower():   
        webbrowser.open("https://www.linkedin.com/in/yashvardhan-reddy-426004334/")
    elif "open X" in c.lower():   
        webbrowser.open("https://x.com/")
    elif "open chatgpt" in c.lower():   
        webbrowser.open("https://chatgpt.com/")    
    elif "open youtube" in c.lower():   
        webbrowser.open("https://youtube.com/")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibrary.music.get(song)
        webbrowser.open(link) 
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=f679c4306480481baf1395d1427180b9")       
        if r.status_code == 200:
            #parse the json response
            data = r.json()
            #Extract the articles
            articles = data.get("articles", [])
            #Print the headlines 
            for article in articles:
                print(article['title'])

    else:
        # let openai handle if the above cant 
        output=aiProcess(c) 
        speak(output)     
        pass

    

if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    while True:
        #Listen for the wake word Jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        # recognize speech using Google
        print('Recognizing....')
        try:
            with sr.Microphone() as source:
                print("Hearing....!")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)

                word=r.recognize_google(audio)
                if word.lower()=="jarvis":
                    speak("Ya")
                    #Listen for command!
                    with sr.Microphone() as source:
                        print("Jarvis active....")
                        audio = r.listen(source)
                        command=r.recognize_google(audio)
                        processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))



