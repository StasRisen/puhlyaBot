import telebot
import requests

bot = telebot.TeleBot("1308961991:AAFMZ1dV0ODPJhahmWU9n9Rt2HWH-z_f7XU")



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет, Пухляк! :-)")


@bot.message_handler(commands=['weather'])
def send_weather(message):
	url = 'http://wttr.in'
	res = requests.get(url)
	temp = res.content.decode('utf-8')
	bot.reply_to(message, temp[:30] + '\n' + temp[158:160] + '..' +temp[177:179] + '°')

bot.polling()