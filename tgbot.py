# import telebot
# from telebot import types


# bot = telebot.TeleBot("7788008366:AAEK56DWkzb7rWDWMnTKSCIl0mZf-pBIkRe")


# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup()
#     btn1 = types.KeyboardButton('Перейти на игру')
#     markup.row(btn1)
#     bot.send_message(message.chat.id, 'Привет! Я БОТ ИГРА 🎮', reply_markup=markup)
#     bot.register_next_step_handler(message, on_click)


# def on_click(message):
#     if message.text == 'Перейти на игру':
#         bot.send_message(message.chat.id, "https://vseigru.net/")
    

# bot.polling()



