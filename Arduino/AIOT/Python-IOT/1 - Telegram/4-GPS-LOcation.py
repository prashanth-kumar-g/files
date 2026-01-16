import telepot

import geocoder # For GPS Location

# Connect to our bot
bot = telepot.Bot(token="5334877955:AAHzONXFqd6_kBnDIotxD5NChQRcNn7_XYA")

# Sets the id for the active chat
chat_id=614882195 # Your Chat ID

#g = geocoder.ip('me')
lat,lon = 12.9245, 77.5788
bot.sendLocation(chat_id, lat, lon)

