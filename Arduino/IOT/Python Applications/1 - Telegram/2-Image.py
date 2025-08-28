import telepot

# Connect to our bot
bot = telepot.Bot(token="6363502528:AAH8GIqcY16mixUOCN9jGsmv_wNt2nzlPdA")

# Sets the id for the active chat
chat_id=5172950600 # Your Chat ID

# Sends a Image to the chat
while True:
    bot.sendPhoto(chat_id=chat_id,photo=open('Python.jpg', 'rb'))

