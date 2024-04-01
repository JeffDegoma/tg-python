import requests
import telebot
import os

token = "your_TOKEN"
chat_id = "your_ID"
BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)


def send_message(text):
   url_req = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text 
   results = requests.get(url_req)
   print(results.json())
   #bot.sendPhoto(chat_id, 'URL_OF_YOUR_PHOTO')

send_message("YOUR_MESSAGE")
