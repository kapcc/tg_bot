from aiogram import types, Dispatcher 
from create_bot import dp, bot 
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Command, Text, ChatTypeFilter
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ChatType


import sqlite3
kb_client = InlineKeyboardMarkup(row_width=2)
kb_client.add(
        InlineKeyboardButton("🇬🇧 English", callback_data='English'),
        InlineKeyboardButton("🇷🇺 Русский", callback_data='Русский'),
        InlineKeyboardButton("🇰🇿 Қазақша", callback_data='Қазақша')
    )
kb_client_RMENU = InlineKeyboardMarkup(row_width=1)
kb_client_KMENU = InlineKeyboardMarkup(row_width=1)
kb_client_EMENU = InlineKeyboardMarkup(row_width=1)

class LanguageMode(StatesGroup):
    LANG_CHOICE = State()  # Состояние для выбора языка
    ENGLISH_MODE = State()  # Состояние для режима английского языка
    RUSSIAN_MODE = State()  # Состояние для режима русского языка
    KAZAKH_MODE = State()  # Состояние для режима русского языка
    ENGLISH_MODE_MENU = State()  # Состояние для режима английского языка
    RUSSIAN_MODE_MENU = State()  # Состояние для режима русского языка
    KAZAKH_MODE_MENU = State()  # Состояние для режима русского языка
    ENGLISH_MODE_CHECKCERTS = State()  # Состояние для режима английского языка
    RUSSIAN_MODE_CHECKCERTS = State()  # Состояние для режима русского языка
    KAZAKH_MODE_CHECKCERTS = State()  # Состояние для режима русского языка

db = sqlite3.connect('server_certHappyChoice.db')
sql = db.cursor()

@dp.message_handler(Command('start'), ChatTypeFilter('private'))
async def start_command(message: types.Message, state: FSMContext):
    # Определение клавиатуры с кнопками
    
    

    # Отправляем сообщение с выбором языка и клавиатурой
    await message.answer("Выберите язык общения:", reply_markup=kb_client)
    

    # Переходим в состояние выбора языка
    await LanguageMode.LANG_CHOICE.set()



@dp.callback_query_handler(lambda c: c.data.startswith('Вернуться в главное меню'), state=LanguageMode.RUSSIAN_MODE_MENU)
async def process_english(callback_query: types.CallbackQuery, state: FSMContext):
    await LanguageMode.LANG_CHOICE.set()
    await bot.send_message(callback_query.from_user.id, "Выберите язык общения:",reply_markup=kb_client)
@dp.callback_query_handler(lambda c: c.data.startswith('Вернуться в главное меню'), state=LanguageMode.ENGLISH_MODE_MENU)
async def process_english(callback_query: types.CallbackQuery, state: FSMContext):
    await LanguageMode.LANG_CHOICE.set()
    await bot.send_message(callback_query.from_user.id, "Выберите язык общения:",reply_markup=kb_client)
@dp.callback_query_handler(lambda c: c.data.startswith('Вернуться в главное меню'), state=LanguageMode.KAZAKH_MODE_MENU)
async def process_english(callback_query: types.CallbackQuery, state: FSMContext):
    await LanguageMode.LANG_CHOICE.set()
    await bot.send_message(callback_query.from_user.id, "Выберите язык общения:",reply_markup=kb_client)
@dp.callback_query_handler(lambda c: c.data.startswith('Вернуться в главное меню'), state=LanguageMode.RUSSIAN_MODE_CHECKCERTS)
async def process_english(callback_query: types.CallbackQuery, state: FSMContext):
    await LanguageMode.LANG_CHOICE.set()
    await bot.send_message(callback_query.from_user.id, "Выберите язык общения:",reply_markup=kb_client)
@dp.callback_query_handler(lambda c: c.data.startswith('Вернуться в главное меню'), state=LanguageMode.ENGLISH_MODE_CHECKCERTS)
async def process_english(callback_query: types.CallbackQuery, state: FSMContext):
    await LanguageMode.LANG_CHOICE.set()
    await bot.send_message(callback_query.from_user.id, "Выберите язык общения:",reply_markup=kb_client)
@dp.callback_query_handler(lambda c: c.data.startswith('Вернуться в главное меню'), state=LanguageMode.KAZAKH_MODE_CHECKCERTS)
async def process_english(callback_query: types.CallbackQuery, state: FSMContext):
    await LanguageMode.LANG_CHOICE.set()
    await bot.send_message(callback_query.from_user.id, "Выберите язык общения:",reply_markup=kb_client)


################################################# ПЕРЕЗОД В СЕРТИФИКАТ МОД
@dp.callback_query_handler(lambda c: c.data.startswith('проверка сертификата'), state=LanguageMode.RUSSIAN_MODE_MENU)
async def process_english(callback_query: types.CallbackQuery, state: FSMContext):
    kb_client_RMENU = InlineKeyboardMarkup(row_width=1)
    kb_client_RMENU.add(
        #InlineKeyboardButton("✅ ПРОВЕРКА СЕРТИФИКАТА", callback_data='проверка сертификата'),
       # InlineKeyboardButton("📖 ОСТАВИТЬ ОБРАЩЕНИЕ", callback_data='Обращение'),
        InlineKeyboardButton("↪️ Вернуться в главное меню", callback_data='Вернуться в главное меню')
    )
    await LanguageMode.RUSSIAN_MODE_CHECKCERTS.set()
    await bot.send_message(callback_query.from_user.id, "Чтобы проверить сертификат введите серийный номер \n Например: AA001",reply_markup=kb_client_RMENU)


@dp.callback_query_handler(lambda c: c.data.startswith('checkcerts'), state=LanguageMode.ENGLISH_MODE_MENU)
async def process_english(callback_query: types.CallbackQuery, state: FSMContext):
    kb_client_EMENU = InlineKeyboardMarkup(row_width=1)
    kb_client_EMENU.add(
        #InlineKeyboardButton("✅ CHECK THE CERTIFICATE", callback_data='checkcerts'),
        #InlineKeyboardButton("📖 leave a message", callback_data='Обращение'),
        InlineKeyboardButton("↪️ Return to main menu", callback_data='Вернуться в главное меню')
    )
    await LanguageMode.ENGLISH_MODE_CHECKCERTS.set()
    await bot.send_message(callback_query.from_user.id, "To check the certificate, enter the serial number \n For example: AA001:",reply_markup=kb_client_EMENU)

@dp.callback_query_handler(lambda c: c.data.startswith('Сертификат тексеру'), state=LanguageMode.KAZAKH_MODE_MENU)
async def process_english(callback_query: types.CallbackQuery, state: FSMContext):
    kb_client_KMENU = InlineKeyboardMarkup(row_width=1)
    kb_client_KMENU.add(
        #InlineKeyboardButton("✅ Сертификат тексеру", callback_data='Сертификат тексеру'),
        #InlineKeyboardButton("📖 хабарлама қалдыру", callback_data='Обращение'),
        InlineKeyboardButton("↪️ негізгі мәзірге оралу", callback_data='Вернуться в главное меню')
    )
    await LanguageMode.KAZAKH_MODE_CHECKCERTS.set()
    await bot.send_message(callback_query.from_user.id, "Куәлікті тексеру үшін сериялық нөмірді енгізіңіз \n Мысалы: AA001:",reply_markup=kb_client_KMENU)    




@dp.callback_query_handler(lambda c: c.data.startswith('English'), state=LanguageMode.LANG_CHOICE)
async def process_english(callback_query: types.CallbackQuery, state: FSMContext):  
    kb_client_EMENU = InlineKeyboardMarkup(row_width=1)
    kb_client_EMENU.add(
        InlineKeyboardButton("✅ CHECK THE CERTIFICATE", callback_data='checkcerts'),
        #InlineKeyboardButton("📖 leave a message", callback_data='Обращение'),
        InlineKeyboardButton("↪️ Return to main menu", callback_data='Вернуться в главное меню')
    )
    # Обработка выбора английского языка
    await bot.send_message(callback_query.from_user.id, "You have selected the English language mode",reply_markup=kb_client_EMENU)
    await LanguageMode.ENGLISH_MODE_MENU.set()
    

@dp.callback_query_handler(lambda c: c.data.startswith('Русский'), state=LanguageMode.LANG_CHOICE)
async def process_english(callback_query: types.CallbackQuery):
    kb_client_RMENU = InlineKeyboardMarkup(row_width=1)
    kb_client_RMENU.add(
        InlineKeyboardButton("✅ ПРОВЕРКА СЕРТИФИКАТА", callback_data='проверка сертификата'),
       # InlineKeyboardButton("📖 ОСТАВИТЬ ОБРАЩЕНИЕ", callback_data='Обращение'),
        InlineKeyboardButton("↪️ Вернуться в главное меню", callback_data='Вернуться в главное меню')
    )
    # Обработка выбора английского языка
    await bot.send_message(callback_query.from_user.id, "Вы выбрали режим русского языка",reply_markup=kb_client_RMENU)
    
    await LanguageMode.RUSSIAN_MODE_MENU.set()

@dp.callback_query_handler(lambda c: c.data.startswith('Қазақша'), state=LanguageMode.LANG_CHOICE)
async def process_english(callback_query: types.CallbackQuery):
    kb_client_KMENU = InlineKeyboardMarkup(row_width=1)
    kb_client_KMENU.add(
        InlineKeyboardButton("✅ Сертификат тексеру", callback_data='Сертификат тексеру'),
        #InlineKeyboardButton("📖 хабарлама қалдыру", callback_data='Обращение'),
        InlineKeyboardButton("↪️ негізгі мәзірге оралу", callback_data='Вернуться в главное меню')
    )
    # Обработка выбора английского языка
    await bot.send_message(callback_query.from_user.id, "Сіз қазақ тілі режимін таңдадыңыз",reply_markup=kb_client_KMENU)
    await LanguageMode.KAZAKH_MODE_MENU.set()    












@dp.message_handler(state=LanguageMode.ENGLISH_MODE_CHECKCERTS, content_types=types.ContentTypes.TEXT)
async def russian_mode(message: types.Message):
    kb_client_EMENU = InlineKeyboardMarkup(row_width=1)
    kb_client_EMENU.add(
        #InlineKeyboardButton("✅ CHECK THE CERTIFICATE", callback_data='checkcerts'),
        #InlineKeyboardButton("📖 leave a message", callback_data='Обращение'),
        InlineKeyboardButton("↪️ Return to main menu", callback_data='Вернуться в главное меню')
    )
    key_value = message.text
    sql.execute("SELECT * FROM Certificates WHERE CertNumber = ?", (key_value,))
    rows = sql.fetchall()
    lst = []
    if len(rows) > 0:
        lst = [item for row in rows for item in row]
        text = f" Certificate with serial number <b>{lst[0]}</b>,\n The student who received the certificate - <b>{lst[4]}</b>,\n Certificate at the end of the course - <b>{lst [1]}</b>,\n Certificate Issued - <b>{lst[3]}</b>,\n Course Instructor - <b>{lst[2]}</b>,\n Academic institution - <b>{lst[5]}</b>"
        await message.answer(text, parse_mode="HTML",reply_markup=kb_client_EMENU)            
                             
    else:
        await message.answer("A certificate with this serial number does not exist in the database. Try again.", reply_markup=kb_client_EMENU)


@dp.message_handler(state=LanguageMode.KAZAKH_MODE_CHECKCERTS, content_types=types.ContentTypes.TEXT)
async def russian_mode(message: types.Message):
    kb_client_KMENU = InlineKeyboardMarkup(row_width=1)
    kb_client_KMENU.add(
        #InlineKeyboardButton("✅ Сертификат тексеру", callback_data='Сертификат тексеру'),
        #InlineKeyboardButton("📖 хабарлама қалдыру", callback_data='Обращение'),
        InlineKeyboardButton("↪️ негізгі мәзірге оралу", callback_data='Вернуться в главное меню')
    )
    key_value = message.text
    sql.execute("SELECT * FROM Certificates WHERE CertNumber = ?", (key_value,))
    rows = sql.fetchall()
    lst = []
    if len(rows) > 0:
        lst = [item for row in rows for item in row]
        text = f" Сертификаттың сериялық нөмірі <b>{lst[0]}</b>,\n Сертификат алған оқушы - <b>{lst[4]}</b>,\n Курс өткендігі туралы сертификат - <b> {lst[1]}</b>,\n Сертификат берілді - <b>{lst[3]}</b>,\n Курс жетекшісі - <b>{lst[2]} </b>,\n Оқу орны - <b>{lst[5]}</b>"
        await message.answer(text, parse_mode="HTML", reply_markup=kb_client_KMENU)                                 
    else:
        await message.answer("Бұл сериялық нөмірі бар сертификат дерекқорда жоқ. Қайталап көріңіз.",reply_markup=kb_client_KMENU)
@dp.message_handler(state=LanguageMode.RUSSIAN_MODE_CHECKCERTS, content_types=types.ContentTypes.TEXT)
async def russian_mode(message: types.Message):
    
    kb_client_RMENU = InlineKeyboardMarkup(row_width=1)
    kb_client_RMENU.add(
        #InlineKeyboardButton("✅ ПРОВЕРКА СЕРТИФИКАТА", callback_data='проверка сертификата'),
       # InlineKeyboardButton("📖 ОСТАВИТЬ ОБРАЩЕНИЕ", callback_data='Обращение'),
        InlineKeyboardButton("↪️ Вернуться в главное меню", callback_data='Вернуться в главное меню')
    )
    key_value = message.text
    sql.execute("SELECT * FROM Certificates WHERE CertNumber = ?", (key_value,))
    rows = sql.fetchall()
    lst = []
    if len(rows) > 0:
        lst = [item for row in rows for item in row]
        text = f"Сертификат с серийным номером <b>{lst[0]}</b>,\n Ученик получивший сертификат - <b>{lst[4]}</b>,\n Сертификат по окончанию курса - <b>{lst[1]}</b>,\n Сертификат выдан - <b>{lst[3]}</b>,\n Преподаватель курса - <b>{lst[2]}</b>,\n Учебное заведение - <b>{lst[5]}</b>"
        await message.answer(text, parse_mode="HTML", reply_markup=kb_client_RMENU)            
                             
    else:
        await message.answer("Сертификата с таким серийным номерм не существует в базе. Попробуйте еще раз.", reply_markup=kb_client_RMENU)







###############################################ЗДЕСЬ ФУНКЦИИ КОТОРЫЕ ОТВЕЧАЮТ ЗА ОБРАЩЕНИЕ БОТА В СЛУЧАЕ ОБРЫВА СОЕДИНЕНИЯ

@dp.message_handler(state=LanguageMode.LANG_CHOICE, content_types=types.ContentTypes.TEXT)
async def russian_mode(message: types.Message):
    kb_client = InlineKeyboardMarkup(row_width=2)
    kb_client.add(
        InlineKeyboardButton("🇬🇧 English", callback_data='English'),
        InlineKeyboardButton("🇷🇺 Русский", callback_data='Русский'),
        InlineKeyboardButton("🇰🇿 Қазақша", callback_data='Қазақша')
    )

    # Отправляем сообщение с выбором языка и клавиатурой
    await message.answer("Выберите язык общения:", reply_markup=kb_client)
    

    # Переходим в состояние выбора языка
    await LanguageMode.LANG_CHOICE.set()

@dp.message_handler(state=LanguageMode.RUSSIAN_MODE_MENU, content_types=types.ContentTypes.TEXT)
async def russian_mode(message: types.Message):
    kb_client = InlineKeyboardMarkup(row_width=2)
    kb_client.add(
        InlineKeyboardButton("✅ ПРОВЕРКА СЕРТИФИКАТА", callback_data='проверка сертификата'),
       # InlineKeyboardButton("📖 ОСТАВИТЬ ОБРАЩЕНИЕ", callback_data='Обращение'),
        InlineKeyboardButton("↪️ Вернуться в главное меню", callback_data='Вернуться в главное меню')
    )
    await message.answer("Вы выбрали режим русского языка:", reply_markup=kb_client)
    # Переходим в состояние выбора языка
    await LanguageMode.RUSSIAN_MODE_MENU.set()
@dp.message_handler(state=LanguageMode.KAZAKH_MODE_MENU, content_types=types.ContentTypes.TEXT)
async def russian_mode(message: types.Message):
    kb_client_KMENU = InlineKeyboardMarkup(row_width=1)
    kb_client_KMENU.add(
        InlineKeyboardButton("✅ Сертификат тексеру", callback_data='Сертификат тексеру'),
        #InlineKeyboardButton("📖 хабарлама қалдыру", callback_data='Обращение'),
        InlineKeyboardButton("↪️ негізгі мәзірге оралу", callback_data='Вернуться в главное меню')
    )
    # Обработка выбора английского языка
    await message.answer("Сіз қазақ тілі режимін таңдадыңыз:", reply_markup=kb_client_KMENU)
    await LanguageMode.KAZAKH_MODE_MENU.set()
@dp.message_handler(state=LanguageMode.ENGLISH_MODE_MENU, content_types=types.ContentTypes.TEXT)
async def russian_mode(message: types.Message):
    kb_client_EMENU = InlineKeyboardMarkup(row_width=1)
    kb_client_EMENU.add(
        InlineKeyboardButton("✅ CHECK THE CERTIFICATE", callback_data='checkcerts'),
        #InlineKeyboardButton("📖 leave a message", callback_data='Обращение'),
        InlineKeyboardButton("↪️ Return to main menu", callback_data='Вернуться в главное меню')
    )
    # Обработка выбора английского язык
    await message.answer("You have selected the English language mode", reply_markup=kb_client_EMENU)
    await LanguageMode.ENGLISH_MODE_MENU.set()



@dp.message_handler(ChatTypeFilter('private'))
async def handle_private_message(message: types.Message):
   
    # Отправляем сообщение с выбором языка и клавиатурой
    await message.answer("Выберите язык общения:",  reply_markup=kb_client)
    

    # Переходим в состояние выбора языка
    await LanguageMode.LANG_CHOICE.set()