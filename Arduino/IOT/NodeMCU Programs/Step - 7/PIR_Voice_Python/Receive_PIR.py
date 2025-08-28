from cvzone.SerialModule import SerialObject
from time import sleep
from playsound import playsound


arduino = SerialObject("COM14")

while True:
    Data = arduino.getData()
    print("Motion Status == ", Data[0])
    if Data[0] == "16":
        playsound('welcome.mp3')
    

