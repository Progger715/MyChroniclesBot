from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
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


@dp.message_handler(commands=['menu'])
async def cmd_start(message: types.Message):
    await message.answer(text="Открыто меню", reply_markup=keyboards.keyboard_main)


@dp.message_handler(commands=['help'])
async def cmd_start(message: types.Message):
    await message.answer(f"Доступные команды:\n"
                         f"/start - запустить бота\n"
                         f"/help - помощь\n"
                         f"/menu - показать меню\n"
                         f"/get_post_about_hobby - получить пост о моем увлечении\n\n"
                         f"Для доступа к другому функционалу бота введите команду /menu и выберите интересующую "
                         f"Вас команду",
                         reply_markup=keyboards.keyboard_main)


@dp.message_handler(commands=['get_post_about_hobby'])
async def cmd_start(message: types.Message):
    await message.answer(f"Рок музыку я полюбил с детства, наверное с момента, когда впервые услышал динамичное и "
                         f"мощное звучание группы Rammstein. До определенного возраста (лет до 10) я вообще не "
                         f"признавал никакой музыки, кроме Rammstein и КиШ. Каждая нота, каждый аккорд переносит меня "
                         f"в мир энергии, страсти и свободы. Я думаю, что не нужно играть на инструментах, чтобы "
                         f"почувствовать этот драйв. Звуки гитары и мощный ритм барабанов помогают мне и расслабляться,"
                         f" и наоборот собираться с силами, стоит лишь понять свое желание и выбрать правильный трек."
                         f"С возрастом моя любовь к этой музыке только крепнет, я нахожу все новых и новых "
                         f"исполнителей. Я думаю, что это не просто музыкальное течение, это зов сердца.",
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
    keyboard = InlineKeyboardMarkup()
    url_button = InlineKeyboardButton("Открыть репозиторий",
                                      url="https://github.com/Progger715/MyChroniclesBot/tree/main")
    keyboard.add(url_button)
    await message.answer("Ссылка на репозиторий с кодом", reply_markup=keyboard)


# действие по умолчанию
@dp.message_handler()
async def answer(message: types.Message):
    await message.reply("Неизвестная команда")


# обработчик кнопок
@dp.callback_query_handler()
async def callback_query_keyboards(callback_query: types.CallbackQuery):
    if callback_query.data == 'photo_last_selfie':
        photo = open("data/selfie.jpg", "rb")
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo)
    elif callback_query.data == 'photo_height_school':
        photo = open("data/school.jpg", "rb")
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo)
    elif callback_query.data == 'audio_GPT':
        voice = open("data/gpt.ogg", "rb")
        await bot.send_voice(chat_id=callback_query.from_user.id, voice=voice)
    elif callback_query.data == 'audio_SQL_or_NoSQL':
        voice = open("data/sql.ogg", "rb")
        await bot.send_voice(chat_id=callback_query.from_user.id, voice=voice)
    elif callback_query.data == 'audio_love_store':
        voice = open("data/love store.ogg", "rb")
        await bot.send_voice(chat_id=callback_query.from_user.id, voice=voice)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
