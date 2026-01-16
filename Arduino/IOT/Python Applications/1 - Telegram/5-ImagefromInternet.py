import telepot

# Connect to our bot
bot = telepot.Bot(token="8516134409:AAH7cbhJ816w9osZlIsE9Jq-TyV0t16ckFw")

# Sets the id for the active chat
chat_id=5102989677 # Your Chat ID


# Sends a Image from Internet
url = 'https://acebott.com/wp-content/uploads/2025/03/ESP8266-2.webp'
bot.sendPhoto(chat_id=chat_id,photo=url)
