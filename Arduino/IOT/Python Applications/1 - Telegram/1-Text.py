import telepot
import time
while True:
    
    # Connect to your bot
    bot = telepot.Bot(token="6363502528:AAH8GIqcY16mixUOCN9jGsmv_wNt2nzlPdA")

    # Sets the id for the active chat
    chat_id=5172950600 # Your Chat ID

    # Sends a message to the chat
    #a=input("Enter Some Thing")
    bot.sendMessage(chat_id=chat_id,text="Hello Prashanth")
    time.sleep(1)


