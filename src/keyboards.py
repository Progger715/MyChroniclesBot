from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

keyboard_main = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_main.add("Посмотреть фото").add("Получить голосовое сообщение").add("Перейти к репозиторию с кодом бота")

buttons_select_photo = InlineKeyboardMarkup(row_width=1)
buttons_select_photo.add(InlineKeyboardButton("Последнее селфи", callback_data="photo_last_selfie"),
                         InlineKeyboardButton("Фото из старшей школы", callback_data="photo_height_school"))

buttons_select_audio = InlineKeyboardMarkup(row_width=1)
buttons_select_audio.add(InlineKeyboardButton("Что такое GPT для бабушки", callback_data='audio_GPT'),
                         InlineKeyboardButton("Разница между SQL и NoSQL", callback_data='audio_SQL_or_NoSQL'),
                         InlineKeyboardButton("История первой любви", callback_data='audio_love_store'))
