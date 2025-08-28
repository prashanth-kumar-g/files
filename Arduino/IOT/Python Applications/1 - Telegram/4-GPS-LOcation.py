import telepot

import geocoder # For GPS Location

# Connect to our bot
bot = telepot.Bot(token="6363502528:AAH8GIqcY16mixUOCN9jGsmv_wNt2nzlPdA")

# Sets the id for the active chat
chat_id=5172950600 # Your Chat ID

#g = geocoder.ip('me')
lat,lon = 12.9245, 77.5788
while True:
    bot.sendLocation(chat_id, lat, lon)

