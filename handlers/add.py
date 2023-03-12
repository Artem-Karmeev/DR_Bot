from config import dp
from aiogram import types
from classes.init_class import vk, ud
import text 

@dp.message_handler(commands=['add'])
async def add(message: types.Message):
    have = ud.check_id(message.from_user.id)
    if have:
        vk.change_head_flag(message.from_user.id, 1)
        vk.change_support_flag(message.from_user.id, 1)
        vk.add(message.from_user.id)
        await message.answer(text.add_text, parse_mode="HTML")
        await message.answer("Введи дату:")
    else:
        await message.answer(text.init_text)
