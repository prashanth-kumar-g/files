from playsound import playsound
#playsound('radha.mp3')
from gtts import gTTS
import os
while True:
    mytext = input("Enter Some Thing ")
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("mpg321 welcome.mp3")
    playsound('welcome.mp3')

