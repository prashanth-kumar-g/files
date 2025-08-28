import time, datetime
import telepot
from telepot.loop import MessageLoop
import cv2
import matplotlib.pyplot as plt

now = datetime.datetime.now()
def action(msg):
    print("Hi")
    chat_id = msg['chat']['id']
    command = msg['text']
    print ('Received: %s' % chat_id)

    print ('Received: %s' % command)
    
    if command == '/Menu':
        telegram_bot.sendMessage (chat_id, str("1. On \n 2. Off"))
    elif command == '1':
        telegram_bot.sendMessage (chat_id, str("Photo Captured"))
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            ret, frame = cap.read()
        else:
            ret = False

        img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imwrite('Manju.png',img1)
        cap.release()
        
    elif command == '2':
        telegram_bot.sendPhoto(chat_id=chat_id,photo=open('Manju.png', 'rb'))
    elif command == 'Hello':
        telegram_bot.sendMessage (chat_id, str("Hello! RVCE"))
    elif command == '3':
         telegram_bot.sendPhoto(chat_id=chat_id,photo=open('123.jpeg', 'rb'))
    elif command == '4':
        url = "https://images.shiksha.com/mediadata/images/1488189189phpalmxG9.jpeg"
        telegram_bot.sendPhoto(chat_id=chat_id,photo=url)
    elif command == 'Doc':
        telegram_bot.sendDocument(chat_id, document=open('123.txt'))
    else:
        telegram_bot.sendMessage (chat_id, str("Plz Send Correct Choice"))
    

telegram_bot = telepot.Bot('5388068474:AAHr_Qz5GHRXh_O2SY7DymOeOtFptMlSz4g')
print (telegram_bot.getMe())
MessageLoop(telegram_bot, action).run_as_thread()
print ('Up and Running....')
while 1:
    time.sleep(1)
    
