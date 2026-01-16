# Displays the Real Time Date and Time on Video

import cv2
import datetime
from cvzone.SerialModule import SerialObject
from time import sleep


arduino = SerialObject('COM5')

cap = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX

while cap.isOpened():
    success, frame = cap.read()

    text = str(datetime.datetime.now())
    ##########################################################################
    Data = arduino.getData()    #For Receiving data from arduino
    data="The Distance == " + Data[0]
    print("The Distnce == ", Data[0])
    frame = cv2.putText(frame, data, (10,50), font, 1, (0,0,255), 2, cv2.LINE_AA)
    ##########################################################################

    cv2.imshow("Output-Video",frame)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):     
        break

cap.release()                       
cv2.destroyAllWindows()       
