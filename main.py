import telebot
# from telebot import types
from telebot import types


bot = telebot.TeleBot("5930354248:AAGtL1XeJTu0P84wz-FMHZAWRKiFhajlHwk");

@bot.message_handler(commands = ["start"])
def start(message):
    mess = f"Hello, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>"  # <u>подчеркнутый, андерлайн</u>  <b>жирный</b>
    bot.send_message(message.chat.id, mess, parse_mode="html")  #можно задавать формат в тегах, жирный шрифт

# @bot.message_handler(content_types=["text"])
# def get_user_text(message):
#     if message.text == "Hello":
#         bot.send_message(message.chat.id, "And Hello to you", parse_mode = "html")
#     elif message.text == "id":
#         bot.send_message(message.chat.id, f"Your id is: {message.from_user.id}", parse_mode="html")
#     elif message.text == "photo":
#         photo = open("Kenguru2.png", "rb")
#         bot.send_photo(message.chat.id, photo)
#     elif message.text == "photo2":
#         photo2 = open("Kenguru.png", "rb")
#         bot.send_photo(message.chat.id, photo2)
#     elif message.text == "song1":
#         song1 = open("ivanushki-etazhi.mp3", "rb")
#         bot.send_audio(message.chat.id, song1)
#     else:
#         bot.send_message(message.chat.id, "I dont undestand you", parse_mode="html")

@bot.message_handler(content_types=["photo"])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Wow, it is super photo")

@bot.message_handler(commands = ["website"])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Welcome website", url="https://www.youtube.com/"))
    bot.send_message(message.chat.id, "Go to the website", reply_markup=markup)

@bot.message_handler(commands = ["help"])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)  # 1 кнопка в рядуу и подстраивался чтоб под мобилки
    website = types.KeyboardButton("WebSite")
    start = types.KeyboardButton("Start")
    markup.add(website, start)
    bot.send_message(message.chat.id, "куда Вы хотите перейти??", reply_markup=markup)

bot.polling(none_stop=True) #Чтоб бот работал постоянно
