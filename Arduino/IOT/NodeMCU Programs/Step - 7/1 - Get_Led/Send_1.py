from cvzone.SerialModule import SerialObject
from time import sleep


arduino = SerialObject('COM14')

while True:
    arduino.sendData([1])
    sleep(0.5)
    arduino.sendData([0])
    sleep(0.5)
    

