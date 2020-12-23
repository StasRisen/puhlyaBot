import telebot

bot = telebot.TeleBot('1308961991:AAFMZ1dV0ODPJhahmWU9n9Rt2HWH-z_f7XU')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()
