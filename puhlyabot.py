import telebot
import subprocess

bot = telebot.TeleBot("1308961991:AAFMZ1dV0ODPJhahmWU9n9Rt2HWH-z_f7XU")



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет, Пухляк! :-)")


@bot.message_handler(commands=['weather'])
def send_weather(message):
	temp = subprocess.check_output('curl -s http://wttr.in/{Ulyanovsk,Moscow}?format=3', shell=True)
	bot.reply_to(message, temp)
	print(temp)


bot.polling()
