from aiogram.types import Message, ContentType, CallbackQuery, ReplyKeyboardRemove
from user.cofig import dp, bot
from buttons.callback_data import lang, main
from buttons import btn_main, phone, btn_info, btn_lang
from data import data_

"""--------------------------***** start ****--------------------------"""


@dp.message_handler(commands='start')
async def start_command(message: Message):
    text = 'Tilni tanlang!\n\nВыбирайте язык!\n 👇'
    await message.answer(text=text, reply_markup=btn_lang)


"""----------***** Contact tekshirish va DATAga qo'shish ****------------"""


@dp.message_handler(content_types=ContentType.CONTACT)
async def num(message: Message):
    code = data_()['conf_code']
    await message.answer(f"Bizga tasdiqlash kodini yuboring.\n\n{code} 🔑", reply_markup=ReplyKeyboardRemove())
    await message.delete()

"""----------***** DATAga ma'lumot qo'shiladi qo'shish ****------------"""


@dp.message_handler(text=[data_()['conf_code'], data_()['name'], data_()["jshshir"], data_()['bola']])
async def answer(message: Message):
    await message.delete()
    if message.text == data_()['conf_code']:
        with open("image/jsh.jpg", 'rb') as photo:
            await bot.send_photo(message.from_user.id, photo, caption=f"\n\nJSHSHIR raqamingizni kiriting! 📄")
    elif message.text == data_()["jshshir"]:
        with open("image/meterka.jpg", 'rb') as photo:
            await bot.send_photo(message.from_user.id, photo, caption=f"\n\nBolani tugilganlik guvohnoma seriya raqamini kiriting 📃")
    elif message.text == data_()["bola"]:
        await message.answer(text=f"{data_()['name']} sizni arizangiz qabul qilindi tez orada bizning xodimlarimiz siz bilan bog'lanishadi ✅", reply_markup=btn_main)


"""-----------------------------------------------------------------------"""


@dp.callback_query_handler(lang.filter())
async def lang(call: CallbackQuery, callback_data: dict):
    # await call.message.edit_reply_markup(reply_markup=None)
    if callback_data.get('name') == 'uz':
        # await call.message.delete()
        await call.message.answer(text="Hurmatli fuqaro siz asosiy menudasiz 🏠", reply_markup=btn_main)
    elif callback_data.get('name') == 'ru':
        await call.message.delete()
        await call.message.answer(text="Привет Мир!", reply_markup=btn_main)


"""-----------------------------------------------------------------------"""


@dp.callback_query_handler(main.filter())
async def lang(call: CallbackQuery, callback_data: dict):
    await call.message.edit_reply_markup(reply_markup=None)
    if callback_data.get('name') == 'order':
        await call.message.delete()
        await call.message.answer(text="Qo'shimcha menu 🏡", reply_markup=btn_info)
    elif callback_data.get('name') == 'ariza':
        await call.message.delete()
        await call.message.answer(text="Ushbu tugma orqali raqamingizni yuboring! 📲", reply_markup=phone)
    elif callback_data.get('name') == 'back':
        await call.message.delete()
        await call.message.answer(text='Asosiy menu 🏠', reply_markup=btn_main)

"""-----------------------------------------------------------------------"""

@dp.message_handler()
async def all_answer(message: Message):
    await message.answer("Siz kiritgan malumot notog'ri\nIltimos tekshirib qaytadan tering ⚠")

