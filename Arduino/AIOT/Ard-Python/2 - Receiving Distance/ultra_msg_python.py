from cvzone.SerialModule import SerialObject
from time import sleep
from playsound import playsound

arduino = SerialObject('COM5')

while True:
    Data = arduino.getData()
    print("The Distance == ", Data[0])
    a=int(Data[0])
    if(a < 7):
        playsound('welcome.mp3')
    

