import telebot
from telebot import types

TOKEN = "8699516233:AAFtEQ9aNfHkmDpUyZ2qLOCOxr95FyBV350"
ADMIN_ID = 5133150161  # admin telegram id

bot = telebot.TeleBot(TOKEN)

users = {}
withdraw_type = {}

@bot.message_handler(commands=['start'])
def start(message):

    user_id = message.from_user.id

    if user_id not in users:
        users[user_id] = {"balance":0,"votes":0}

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("🗳 Ovoz berish")
    btn2 = types.KeyboardButton("💰 Balans")
    btn3 = types.KeyboardButton("🏆 Reyting")
    btn4 = types.KeyboardButton("🔗 Referal link")
    btn5 = types.KeyboardButton("💸 Yechib olish")

    markup.add(btn1)
    markup.add(btn2,btn3)
    markup.add(btn4)
    markup.add(btn5)

    bot.send_message(message.chat.id,"Botga xush kelibsiz",reply_markup=markup)


@bot.message_handler(func=lambda m: m.text=="🗳 Ovoz berish")
def vote(message):

    user_id = message.from_user.id

    users[user_id]["votes"]+=1
    users[user_id]["balance"]+=15000

    bot.send_message(message.chat.id,"+15000 token qo'shildi")


@bot.message_handler(func=lambda m: m.text=="💰 Balans")
def balance(message):

    user_id = message.from_user.id

    bot.send_message(message.chat.id,f"Balans: {users[user_id]['balance']} token")


@bot.message_handler(func=lambda m: m.text=="💸 Yechib olish")
def withdraw(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("📱 Telefon raqam")
    btn2 = types.KeyboardButton("💳 Karta")

    markup.add(btn1,btn2)

    bot.send_message(message.chat.id,"Qaysi usul bilan pul olmoqchisiz?",reply_markup=markup)


@bot.message_handler(func=lambda m: m.text=="📱 Telefon raqam")
def phone(message):

    withdraw_type[message.from_user.id]="phone"

    bot.send_message(message.chat.id,"Telefon raqamingizni yozing")


@bot.message_handler(func=lambda m: m.text=="💳 Karta")
def card(message):

    withdraw_type[message.from_user.id]="card"

    bot.send_message(message.chat.id,"Karta raqamingizni yozing")


@bot.message_handler(func=lambda m: True)
def get_data(message):

    user_id = message.from_user.id

    if user_id in withdraw_type:

        data = message.text

        bot.send_message(message.chat.id,"So'rov yuborildi. Admin tasdiqlashini kuting")

        bot.send_message(
            ADMIN_ID,
            f"Yangi yechib olish so'rovi\n\nUser: {user_id}\nUsul: {withdraw_type[user_id]}\nMa'lumot: {data}"
        )

        del withdraw_type[user_id]


bot.polling()