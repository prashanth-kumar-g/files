import telepot
import time
while True:
    
    # Connect to your bot
    bot = telepot.Bot(token="8516134409:AAH7cbhJ816w9osZlIsE9Jq-TyV0t16ckFw")

    # Sets the id for the active chat
    chat_id=5102989677 # Your Chat ID

    # Sends a message to the chat
    #a=input("Enter Some Thing")
    bot.sendMessage(chat_id=chat_id,text="Hello Prashanth")
    time.sleep(1)
