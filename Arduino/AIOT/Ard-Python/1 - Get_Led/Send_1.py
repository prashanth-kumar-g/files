from cvzone.SerialModule import SerialObject
from time import sleep


arduino = SerialObject('/dev/ttyUSB0')

while True:
    arduino.sendData([1])
    sleep(2)
    arduino.sendData([0])
    sleep(2)
    

