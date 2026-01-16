import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()


text_to_speak = "hi i am a sample  "
speak(text_to_speak)
