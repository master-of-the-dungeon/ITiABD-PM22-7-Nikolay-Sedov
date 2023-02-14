import telebot
import time
bot = telebot.TeleBot('6169167160:AAH-uPjPKasDAN02EoAUklyvythODeuaGFs')
@bot.message_handler(commands=['start'])
def start(message):
    for i in range(20):
        bot.send_message(message.chat.id,'@erorka404 @cliqqque @ViMan_2033 ВСТАВАЙТЕ БЛЯДИ')
        time.sleep(1)
bot.polling()