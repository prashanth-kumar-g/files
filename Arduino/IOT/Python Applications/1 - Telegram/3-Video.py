import telepot

# Connect to our bot
bot = telepot.Bot(token="6363502528:AAH8GIqcY16mixUOCN9jGsmv_wNt2nzlPdA")

# Sets the id for the active chat
chat_id=5172950600 # Your Chat ID


# Sends a Video File to the chat
while True:
    bot.sendVideo(chat_id=chat_id,video=open('Python.mp4', 'rb'))
