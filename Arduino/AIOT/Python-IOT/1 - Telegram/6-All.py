import telepot
#import cv2
#import geocoder
# Connect to our bot
bot = telepot.Bot(token="5388068474:AAHr_Qz5GHRXh_O2SY7DymOeOtFptMlSz4g")

# Sets the id for the active chat
chat_id=614882195 # Your Chat ID
# Sends a message to the chat
print("-"*60)
print("Sending Text Message ")
print("-"*60)
bot.sendMessage(chat_id=chat_id, text="Attention!!!, Object Detected in Camera 1")

print("-"*60)
print("Sending Image Message ")
print("-"*60)
bot.sendPhoto(chat_id=chat_id,photo=open('Python.jpg', 'rb'))

print("-"*60)
print("Sending GPS Location ")
print("-"*60)
#g = geocoder.ip('me')
lat,lon = 12.9245, 77.5788
bot.sendLocation(chat_id, lat, lon)

print("-"*60)
print("Sending Video File ")
print("-"*60)
bot.sendVideo(chat_id=chat_id,video=open('Python.mp4', 'rb'))
