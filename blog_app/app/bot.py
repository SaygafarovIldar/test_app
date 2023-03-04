import telebot
from telebot import types

from django.conf import settings


bot = telebot.TeleBot(token=settings.BOT_TOKEN)


@bot.message_handler(commands=["start"])
def command_start(message: types.Message):
    chat_id = message.chat.id

    bot.send_message(chat_id, "Привет от Django")
