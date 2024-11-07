# Импортируем библиотеки
import telebot
from googletrans import Translator

# Создаем переводчик
translator = Translator()

# Задаем исходные язык и целевой язык
src = 'ru'
dest = 'en'

# Настраиваем бота
bot = telebot.TeleBot('8080090784:AAEVg49UtkzYX3RtaU4TF_mfzgW0XX9DOJQ')

# Определяем функцию для обработки сообщений
@bot.message_handler(func=lambda m: True)
def translate_message(message):
  # Берем полученное сообщение и переводим его
  translated_text = translator.translate(message.text, src=src, dest=dest).text
  # Отправляем переведенное сообщение
  bot.send_message(message.chat.id, translated_text)

# Запускаем бота
bot.polling()