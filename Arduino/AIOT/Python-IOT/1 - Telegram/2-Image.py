import telepot

# Connect to our bot
bot = telepot.Bot(token="5388068474:AAHr_Qz5GHRXh_O2SY7DymOeOtFptMlSz4g")

# Sets the id for the active chat
chat_id=614882195 # Your Chat ID


while True:
    # Sends a Image to the chat
    bot.sendPhoto(chat_id=chat_id,photo=open('Capture.png', 'rb'))

