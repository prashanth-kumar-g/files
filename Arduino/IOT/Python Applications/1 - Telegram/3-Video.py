import telepot

# Connect to our bot
bot = telepot.Bot(token="8516134409:AAH7cbhJ816w9osZlIsE9Jq-TyV0t16ckFw")

# Sets the id for the active chat
chat_id=5102989677 # Your Chat ID


# Sends a Video File to the chat
while True:
    bot.sendVideo(chat_id=chat_id,video=open('Python.mp4', 'rb'))
