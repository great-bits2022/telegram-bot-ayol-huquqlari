from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text='Raqam jonatish. 📲', request_contact=True))
