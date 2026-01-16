import time, datetime
import telepot
from telepot.loop import MessageLoop
import Specific
import cv2

now = datetime.datetime.now()
def action(msg):
    try:
        
        print("Hi")
        chat_id = msg['chat']['id']
        command = msg['text']
        print ('Received: %s' % chat_id)

        print ('Received: %s' % command)
    
        if command == '/Menu':
            telegram_bot.sendMessage (chat_id, str("1. Photo Capture \n 2. Send Photo"))
            telegram_bot.sendMessage (chat_id, str("1. Video Capture \n 2. Send Video"))
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
            telegram_bot.sendMessage (chat_id, str("Sending Photo"))
            telegram_bot.sendPhoto(chat_id=chat_id,photo=open('Manju.png', 'rb'))
        elif command == '3':
            telegram_bot.sendMessage (chat_id, str("Recording....."))
            Specific.Recording()
        elif command == '4':
            telegram_bot.sendMessage (chat_id, str("Sending...."))
            telegram_bot.sendVideo(chat_id=chat_id,video=open('output.avi', 'rb'))
        elif command == 'Hi':
            telegram_bot.sendMessage (chat_id, str("Hi Inchara and Priyanka"))
        elif command == 'BCA':
            telegram_bot.sendMessage (chat_id, str("hsfkhkchjkchjkcxhjkxchjk kjhjxchjhcjh"))
        elif command == 'Hello':
            telegram_bot.sendMessage (chat_id, str("Hello Hi Inchara and Priyanka, How Can i Help You"))
        elif command == 'RVCE':
            url = "https://images.shiksha.com/mediadata/images/1488189189phpalmxG9.jpeg"
            telegram_bot.sendPhoto(chat_id=chat_id,photo=url)
        elif command == 'Doc':
            telegram_bot.sendDocument(chat_id, document=open('123.txt'))
        elif command == 'Bye':
            telegram_bot.sendMessage (chat_id, str("Bye Hi Inchara and Priyanka, See you again"))    
        else:
            telegram_bot.sendMessage (chat_id, str("Plz Send Correct Choice"))
            
    except Exception as e:
        pass
    except KeyboardInterrupt:
        pass
    

telegram_bot = telepot.Bot('5388068474:AAHr_Qz5GHRXh_O2SY7DymOeOtFptMlSz4g')
print (telegram_bot.getMe())
MessageLoop(telegram_bot, action).run_as_thread()
print ('Up and Running....')
while 1:
    try:
        time.sleep(1)
    except Exception as e:
        pass
    except KeyboardInterrupt:
        pass
