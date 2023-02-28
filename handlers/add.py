from config import dp
from aiogram import types
from classes.init_class import us, sec, ud
import text 

@dp.message_handler(commands=['add'])
async def add(message: types.Message):
    have = ud.check_id(message.from_user.id)
    if have:
        ud.change_flag(message.from_user.id, 1, 1)
        ud.change_flag(message.from_user.id, 3, 2)
        await message.answer(text.add_text, parse_mode="HTML")
        await message.answer("Введи имя:")
    else:
        await message.answer(text.init_text)