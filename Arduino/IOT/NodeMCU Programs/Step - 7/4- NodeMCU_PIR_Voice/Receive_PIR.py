from cvzone.SerialModule import SerialObject
from time import sleep
from playsound import playsound


arduino = SerialObject("com14")

while True:
    Data = arduino.getData()
    print("Motion Status == ", Data[0])
    if int(Data[0]) < 7:
        playsound('welcome.mp3')
    

