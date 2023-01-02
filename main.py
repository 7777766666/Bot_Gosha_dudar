import telebot

bot = telebot.TeleBot("5930354248:AAGtL1XeJTu0P84wz-FMHZAWRKiFhajlHwk");

@bot.message_handler(commands = ["start"])
def start(message):
    mess = f"Hello, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>"  # <u>подчеркнутый, андерлайн</u>  <b>жирный</b>
    bot.send_message(message.chat.id, mess, parse_mode="html")  #можно задавать формат в тегах, жирный шрифт

@bot.message_handler(content_types=["text"])
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, "And Hello to you", parse_mode = "html")
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Your id is: {message.from_user.id}", parse_mode="html")
    elif message.text == "photo":
        photo = open("Kenguru2.png", "rb")
        bot.send_photo(message.chat.id, photo)
    elif message.text == "photo2":
        photo2 = open("Kenguru.png", "rb")
        bot.send_photo(message.chat.id, photo2)
    elif message.text == "song1":
        song1 = open("ivanushki-etazhi.mp3", "rb")
        bot.send_audio(message.chat.id, song1)
    else:
        bot.send_message(message.chat.id, "I dont undestand you", parse_mode="html")

# @bot.message_handler(content_types=["photo"])
# def

bot.polling(none_stop=True) #Чтоб бот работал постоянно
