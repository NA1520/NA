# import telebot
# from telebot import types
# from dotenv import load_dotenv
# import random
# import os

# load_dotenv()
# BOT_TOKEN = os.getenv('BOT_TOKEN')


# bot = telebot.TeleBot(BOT_TOKEN)


# motivational_quotes = [
#     "Секрет вашего успеха в том, что вы не сдаетесь.",
#     "Сначала они смеются над тобой, потом они завидуют.",
#     "Делайте то, что любите, и вы никогда не будете работать ни дня в своей жизни.",
#     "Каждый день – это новый шанс изменить свою жизнь.",
#     "Не бойтесь делать ошибки. Ошибки – это часть успеха."
# ]

# poems = [
#     """
#         Сен - Пайгамбар! Кумон кылган эмесмин,
# Сен болбосон, шапаат кылып келет ким?
# Бийи заалым ушул заман ичинде,
# Билесинби, бизге кандай керексин?""",
#         """Куйуп-жанып батам туркун ойлорго,
# Кучтуу жандар кучсуздoрду кордоодо.
# Дурболонго тушпойт эле журоктор,
# Дуйнодо азыр сенин козун, болгондо."""
# ]


# PHOTOS_FOLDER = './photos'
# MUSIC_FOLDER = './music'




# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     button_motivation = types.KeyboardButton("Цитаты🍃")
#     button_poem = telebot.types.KeyboardButton("Стихи🎼")
#     button_photo = telebot.types.KeyboardButton("Фото🎨")
#     button_music = telebot.types.KeyboardButton("Нашиды🎵")
#     button_help = telebot.types.KeyboardButton("Помощь🆘")
#     markup.add(button_motivation,button_poem,button_photo,button_music,button_help)

#     inline_markup = types.InlineKeyboardMarkup()
#     instagram_button = types.InlineKeyboardButton("Мой Instagram" , url = "https://www.instagram.com/taalaibekovvv7/profilecard/?igsh=MW1jajVkenU3amR0bw==")
#     inline_markup.add(instagram_button)

#     bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}! Я твой мотивационный бот 😊", reply_markup=markup)

#     bot.send_message(
#         message.chat.id,
#         "Подпишись на мой Instagram",
#         reply_markup=inline_markup)

# @bot.message_handler(func=lambda message: message.text == "Цитаты🍃")
# def send_motivation(message):
#     quote = random.choice(motivational_quotes)
#     bot.send_message(message.chat.id, quote)


# @bot.message_handler(func=lambda message: message.text == "Стихи🎼")
# def send_motivation(message):
#     poem = random.choice(poems)
#     bot.send_message(message.chat.id, poem)


# @bot.message_handler(func=lambda message: message.text == "Фото🎨")
# def send_photo(message):
#     photo_files = [file for file in os.listdir(PHOTOS_FOLDER) if file.endswith(('.jpg', '.jpeg'))]
#     if photo_files:
#         photo_file = random.choice(photo_files)
#         with open(os.path.join(PHOTOS_FOLDER, photo_file), 'rb') as photo:
#             bot.send_photo(message.chat.id, photo)

# @bot.message_handler(func=lambda message: message.text == "Нашиды🎵")
# def send_music(message):
#     music_files = [file for file in os.listdir(MUSIC_FOLDER) if file.endswith('.mp3')]
#     if music_files:
#         music_file = random.choice(music_files)
#         with open(os.path.join(MUSIC_FOLDER, music_file), 'rb') as music:
#             bot.send_audio(message.chat.id, music)


# @bot.message_handler(func=lambda message: message.text == "Помощь🆘")
# def send_help(message):
#     bot.send_message(message.chat.id,"""Cделай дуА, молись Аллаху !
#                      Помощь Аллаха Близка!
#                     Сура аль-Бакара
# أَمْ حَسِبْتُمْ أَنْ تَدْخُلُوا الْجَنَّةَ وَلَمَّا يَأْتِكُمْ مَثَلُ الَّذِينَ خَلَوْا مِنْ قَبْلِكُمْ  مَسَّتْهُمُ الْبَأْسَاءُ وَالضَّرَّاءُ وَزُلْزِلُوا حَتَّىٰ يَقُولَ الرَّسُولُ وَالَّذِينَ آمَنُوا مَعَهُ مَتَىٰ نَصْرُ اللَّهِ  أَلَا إِنَّ نَصْرَ اللَّهِ قَرِيبٌ
# 2:214
# Или вы полагали, что войдете в Рай, не испытав того, что постигло ваших предшественников? Их поражали нищета и болезни. Они переживали такие потрясения, что Посланник и уверовавшие вместе с ним говорили: "Когда же придет помощь Аллаха?" Воистину, помощь Аллаха близка.
# Всеблагой и Всевышний Аллах сообщил о том, что рабы непременно будут подвергнуты испытанию благополучием, несчастьями или трудностями, подобно тому, как были подвергнуты испытанию предыдущие поколения. Таково установление Аллаха, которое всегда остается в силе и не подвергается изменению. Если человек исповедует религию и придерживается Божьих законов, то он обязательно должен пройти испытание, и если он терпеливо выполняет повеления Аллаха, не обращая внимания на трудности, возникающие на этом пути, то он является правдивым верующим и обретет наивысшее счастье и величие. Но если он принимает искушение людей за наказание Аллаха и сворачивает с прямого пути по причине невзгод и трудностей, если испытания мешают ему следовать намеченным курсом, то его притязания на веру лживы. Вера не зиждется на красивых словах, прекрасных пожеланиях и голословных заявлениях — она подтверждается или опровергается человеческими поступками и деяниями.
# Всевышний сообщил, что предыдущие поколения людей тоже поражали нищета и телесные болезни. Им угрожали смертью и изгнанием, лишением имущества и убийством возлюбленных, их подвергали мучительным пыткам, и трудности становились настолько невыносимыми, что правоверным казалось, что помощь Аллаха запаздывает, хотя они были твердо убеждены в том, что она непременно придет. А поскольку Всевышний Аллах всегда ниспосылает облегчение после трудностей и помогает тем, кто оказывается в стесненном положении, Аллах сообщил о том, что Божья помощь близка.
# Каждый, кто выполняет свои обязанности, неизбежно сталкивается с испытаниями, которые всякий раз становятся все сложнее и серьезнее. И если он проявляет должное терпение и продолжает выполнять свои обязанности, то испытания становятся для него милостью, а трудности сменяются благополучием и успокоением. Он одерживает победу над своими врагами и исцеляется от недугов, которыми страдала его душа. По этому поводу Всевышний сказал:
# «Или вы полагали, что войдете в Рай, пока Аллах не узнал тех из вас, кто сражался и кто был терпелив?» (3:142);
# «Алиф. Лям. Мим. Неужели люди полагают, что их оставят и не подвергнут искушению только за то, что они скажут: “Мы уверовали”? Мы уже подвергли искушению тех, кто был до них. Аллах непременно узнает тех, которые говорят правду, и непременно узнает лжецов» (29:1–3).
# Одним словом, во время испытаний человек либо обретает величие, либо обрекает себя на унижение. """)


# if __name__ == '__main__':
#   bot.polling(none_stop=True)



































# # @bot.message_handler(commands=['start', 'help'])
# # def send_welcome(message):
# #     user_name = message.from_user.first_name
# #     welcome_text = f"Привет, {user_name}! Нажми на кнопку, чтобы получить мотивационную цитату."
# #     markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
# #     button_quote = telebot.types.KeyboardButton("Цитаты ")
# #     button_poem = telebot.types.KeyboardButton("Стихи")
# #     button_photo = telebot.types.KeyboardButton(" Фото ")
# #     button_music = telebot.types.KeyboardButton("Музыка")
# #     button_help = telebot.types.KeyboardButton("Помощь")
# #     markup.add(button_quote,button_poem,button_photo,button_music,button_help)
# #     bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

# # @bot.message_handler(func=lambda message: True)
# # def send_quote(message):
# #     if message.text == "Цитаты":
# #         quote = random.choice(quotes)
# #         bot.send_message(message.chat.id, quote)

# # if __name__ == '__main__':
# #     bot.polling(none_stop=True)