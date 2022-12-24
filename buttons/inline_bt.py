from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from buttons.callback_data import lang, main

btn_lang = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Uz 🇺🇿', callback_data=lang.new(name='uz')),
            InlineKeyboardButton(text='Ru 🇷🇺', callback_data=lang.new(name='ru'))
        ]
    ]
)

btn_info = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Ayollarni himoya orderi haqida ma’lumot. 🧕',
                                 web_app=WebAppInfo(url="https://iiv.uz/news/himoya-orderi-haqida-bilasizmi")),
        ],
        [
            InlineKeyboardButton(text='Ayollar huquqlari. 👮',
                                 web_app=WebAppInfo(url="https://nhrc.uz/oz/menu/prava-zhenschin"))
        ],
        [
            InlineKeyboardButton(text='Asosiy menuga qaytish 🔙', callback_data=main.new(name='back'))
        ]

    ]
)

btn_main = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ayollar haq va huquqlari haqida ma'lumot 🧕",
                                 callback_data=main.new(name='order')),
        ],
        [
            InlineKeyboardButton(text='Bola puli olish tartibi. 🗃',
                                 web_app=WebAppInfo(url="https://www.youtube.com/watch?v=lILU9yri0WE"))
        ],
        [
            InlineKeyboardButton(text='Bola puli uchun ariza yuborish. 📃', callback_data=main.new(name='ariza'))
        ]
    ]
)
