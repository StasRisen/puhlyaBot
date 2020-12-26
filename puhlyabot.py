import telebot
import subprocess

bot = telebot.TeleBot("1308961991:AAFMZ1dV0ODPJhahmWU9n9Rt2HWH-z_f7XU")

command = 'curl wttr.in'

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет, Пухляк! :-)")


@bot.message_handler(commands=['weather'])
def send_weather(message):
	out = subprocess.check_output(command).decode('utf-8')
	temp = out[90:127]
	bot.reply_to(message, out[:30] + '\n' + temp)

bot.polling()