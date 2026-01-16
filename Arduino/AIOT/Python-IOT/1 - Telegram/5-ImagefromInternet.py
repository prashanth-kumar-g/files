import telepot

# Connect to our bot
bot = telepot.Bot(token="5334877955:AAHzONXFqd6_kBnDIotxD5NChQRcNn7_XYA")

# Sets the id for the active chat
chat_id=614882195 # Your Chat ID


# Sends a Image from Internet
url ="https://images.app.goo.gl/C54MEkkNNNsUtJXb7"
#url = "https://images.shiksha.com/mediadata/images/1488189189phpalmxG9.jpeg"
bot.sendPhoto(chat_id=chat_id,photo=url)

