from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()


from telebot.async_telebot import AsyncTeleBot

# import telebot
from telebot import types, util

BOT_TOKEN = os.environ.get('BOT_TOKEN')

# bot = telebot.TeleBot(BOT_TOKEN)

bot = AsyncTeleBot(BOT_TOKEN)

app = Flask(__name__)

# print("bot",bot)

@app.route('/')
def hello_world():
    return 'Hello, Docker!!!!!!' 


@bot.message_handler(commands=['start', 'hello'])
async def send_welcome(message):
    await bot.reply_to(message, "Hi there, how are you doing today?")
# def send_welcome(message):
    # bot.reply_to(message, "Heya, how are you doing today?")


@bot.chat_member_handler()
async def chat_m(message: types.ChatMemberUpdated):
    old = message.old_chat_member
    new = message.new_chat_member
    if new.status == "member":
        print(new.user)
        await bot.send_message(message.chat.id,"Hello @{name}!".format(name=new.user.username)) # Welcome message
        



import asyncio
# asyncio.run(bot.infinity_polling(allowed_updates=util.update_types))
asyncio.run(bot.infinity_polling(allowed_updates=util.update_types))


if __name__ == '__app__':
    # app.run()
    # app.run(host='0.0.0.0', debug=True) 
    app.run(host='0.0.0.0') 

# bot.infinity_polling(allowed_updates=util.update_types)