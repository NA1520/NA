import telebot
from telebot import types
import random

API_TOKEN = '7788008366:AAEK56DWkzb7rWDWMnTKSCIl0mZf-kRepBI'

bot = telebot.TeleBot(API_TOKEN)

translation_history = {}
user_settings = {}
guessing_games = {}

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.chat.id
    user_settings.setdefault(user_id, {})
    main_menu(message)

def main_menu(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    reminder_button = types.KeyboardButton('⏰ Напоминания')
    guess_number_button = types.KeyboardButton('🔢 Угадай число')
    btn1 = types.KeyboardButton('🎮 Перейти на игру')
    markup.add(reminder_button, guess_number_button, btn1)
    
    bot.reply_to(message, f"Привет, {message.from_user.first_name}! Я БОТ ПОМОЩНИК 💁‍♂️. Выбери опцию для продолжения:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '🎮 Перейти на игру')
def on_click(message):
    bot.send_message(message.chat.id, "Ссылка на игру: https://vseigru.net/")
    main_menu(message)

@bot.message_handler(func=lambda message: message.text == '⏰ Напоминания')
def handle_reminders(message):
    user_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(row_width=1)
    add_reminder_button = types.KeyboardButton('Добавить напоминание')
    view_reminders_button = types.KeyboardButton('Посмотреть напоминания')
    back_button = types.KeyboardButton('🔙 Назад')
    markup.add(add_reminder_button, view_reminders_button, back_button)
    bot.reply_to(message, "Выберите действие:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '🔙 Назад')
def handle_back(message):
    main_menu(message)

@bot.message_handler(func=lambda message: message.text == 'Добавить напоминание')
def handle_add_reminder_prompt(message):
    user_id = message.chat.id
    user_settings[user_id]['adding_reminder'] = True
    bot.reply_to(message, "Введите текст напоминания:")

@bot.message_handler(func=lambda message: user_settings.get(message.chat.id, {}).get('adding_reminder', False))
def handle_add_reminder(message):
    user_id = message.chat.id
    user_settings[user_id]['adding_reminder'] = False
    user_settings[user_id].setdefault('reminders', []).append(message.text)
    bot.reply_to(message, "Напоминание добавлено.")
    main_menu(message)

@bot.message_handler(func=lambda message: message.text == 'Посмотреть напоминания')
def handle_view_reminders(message):
    user_id = message.chat.id
    reminders = user_settings.get(user_id, {}).get('reminders', [])
    
    if reminders:
        reminders_text = '\n'.join([f"{idx + 1}. {reminder}" for idx, reminder in enumerate(reminders)])
        bot.reply_to(message, f"Ваши напоминания:\n{reminders_text}")
    else:
        bot.reply_to(message, "У вас пока нет напоминаний.")
    main_menu(message)

@bot.message_handler(func=lambda message: message.text == '🔢 Угадай число')
def handle_guess_number_prompt(message):
    user_id = message.chat.id
    guessing_games[user_id] = {
        'number': random.randint(1, 100),
        'attempts': 0
    }
    bot.reply_to(message, "Я загадал число от 1 до 100. Попробуй угадать!")

@bot.message_handler(func=lambda message: message.chat.id in guessing_games)
def handle_guess_number(message):
    user_id = message.chat.id
    game = guessing_games[user_id]
    
    try:
        guess = int(message.text)
    except ValueError:
        bot.reply_to(message, "Пожалуйста, введите число.")
        return
    
    game['attempts'] += 1
    
    if guess == game['number']:
        bot.reply_to(message, f"Поздравляю! Ты угадал число {game['number']} за {game['attempts']} попыток!")
        del guessing_games[user_id]
        main_menu(message)  
    elif guess < game['number']:
        bot.reply_to(message, "Мое число больше.")
    else:
        bot.reply_to(message, "Мое число меньше.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.chat.id
    bot.reply_to(message, "Извините, я не понимаю это сообщение. Попробуйте выбрать опцию из меню.")
    
    translation_history.setdefault(user_id, []).append(message.text)

if __name__ == '__main__':
    bot.polling()