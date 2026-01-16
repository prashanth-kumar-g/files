import telepot

# Connect to our bot
bot = telepot.Bot(token="5388068474:AAHr_Qz5GHRXh_O2SY7DymOeOtFptMlSz4g")

# Sets the id for the active chat
chat_id=614882195 # Your Chat ID


# Sends a Video File to the chat
bot.sendVideo(chat_id=chat_id,video=open('Python.mp4', 'rb'))
