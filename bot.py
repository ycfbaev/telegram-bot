import telebot
import time

TOKEN = "8699516233:AAFtEQ9aNfHkmDpUyZ2qLOCOxr95FyBV350"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"Bot ishlayapti ✅")

while True:
    try:
        print("Bot ishga tushdi...")
        bot.infinity_polling()
    except:
        time.sleep(5)
