from aiogram import Bot, Dispatcher, executor, types
from src import keyboards
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)


# команды /
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Добро пожаловать!",
                         reply_markup=keyboards.keyboard_main)


# текстовые команды
@dp.message_handler(text='Посмотреть фото')
async def get_photo(message: types.Message):
    await message.answer("Photo no found", reply_markup=keyboards.buttons_select_photo)


@dp.message_handler(text='Получить голосовое сообщение')
async def get_audio(message: types.Message):
    await message.answer("Audio not found", reply_markup=keyboards.buttons_select_audio)


@dp.message_handler(text='Перейти к репозиторию с кодом бота')
async def get_url(message: types.Message):
    await message.answer("Url not found")


# действие по умолчанию
@dp.message_handler()
async def answer(message: types.Message):
    await message.reply("Неизвестная команда")


# обработчик кнопок
@dp.callback_query_handler()
async def callback_query_keyboards(callback_query: types.CallbackQuery):
    if callback_query.data == 'photo_last_selfie':
        photo = open("", "rb")
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo)
    elif callback_query.data == 'photo_height_school':
        photo = open("", "rb")
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo)
    elif callback_query.data == 'audio_GPT':
        voice = open("", "rb")
        await bot.send_voice(chat_id=callback_query.from_user.id, voice=voice)
    elif callback_query.data == 'audio_SQL_or_NoSQL':
        voice = open("", "rb")
        await bot.send_voice(chat_id=callback_query.from_user.id, voice=voice)
    elif callback_query.data == 'audio_love_store':
        voice = open("", "rb")
        await bot.send_voice(chat_id=callback_query.from_user.id, voice=voice)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
