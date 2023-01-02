import telebot

bot = telebot.TeleBot("5930354248:AAGtL1XeJTu0P84wz-FMHZAWRKiFhajlHwk");

@bot.message_handler(commands = ["start"])
def start(message):
    mess = f"Hello, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>"  # <u>подчеркнутый, андерлайн</u>  <b>жирный</b>
    bot.send_message(message.chat.id, mess, parse_mode="html")  #можно задавать формат в тегах, жирный шрифт

@bot.message_handler()
def get_user_text(message):
    bot.send_message(message.chat.id, message, parse_mode = "html")



bot.polling(none_stop=True) #Чтоб бот работал постоянно
