import telepot

import geocoder # For GPS Location

# Connect to our bot
bot = telepot.Bot(token="8516134409:AAH7cbhJ816w9osZlIsE9Jq-TyV0t16ckFw")

# Sets the id for the active chat
chat_id=5102989677 # Your Chat ID

#g = geocoder.ip('me')
lat,lon = 12.9245, 77.5788
while True:
    bot.sendLocation(chat_id, lat, lon)

