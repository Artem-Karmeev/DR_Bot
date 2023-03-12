from config import dp
from aiogram import types
from classes.init_class import vk, ud, us

@dp.message_handler(commands=['del'])
async def my_del(message: types.Message):
    ud.extract_data(message.from_user.id)
    vk.change_head_flag(message.from_user.id, 3)
    vk.change_support_flag(message.from_user.id, 1)
    await message.answer('Какое событие удалить?', parse_mode="html")

