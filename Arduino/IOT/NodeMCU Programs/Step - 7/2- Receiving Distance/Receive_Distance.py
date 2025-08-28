from cvzone.SerialModule import SerialObject
from time import sleep


arduino = SerialObject('COM14')

while True:
    Data = arduino.getData()
    print("The Distnce == ", Data[0])
    

