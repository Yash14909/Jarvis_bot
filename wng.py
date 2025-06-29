def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    

         # Initialize the mixer module
pygame.mixer.init()

         # Load your MP3 file
pygame.mixer.music.load("temp.mp3")

         # Play the music
pygame.mixer.music.play()

         # Keep the program running while the music plays
while pygame.mixer.music.get_busy():
        pass
            # pygame.time.Clock().tick(10)
        os.remove("temp.mp3")         
