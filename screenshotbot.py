//screenshot taking bot
import sys
import time
import random
import datetime
import telepot
import pyscreenshot as image
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setwarnings(False)
def function(msg):
    chat_id= msg['chat']['id']
    command= msg['text']
    if command=='ss':
        img= image.grab()
        img.save("fullscreen.png")
        f=open("/desktop/s5/fullscreen.png",'rb')
        bot.sendPhoto(chat-id,f)

bot=telepot.Bot('1745798317:AAGkep1jM5Gmi7C3D3lkm3dB67r-A3nuooo')

bot.message_loop(handle)
while 1:
    time.sleep(10)
