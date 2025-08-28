from gtts import gTTS
import os
from playsound import playsound
import os
while True:
    mytext = input("Enter some Thing ")
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("mpg321 welcome.mp3")
    playsound('welcome.mp3')
    os.remove('welcome.mp3')
