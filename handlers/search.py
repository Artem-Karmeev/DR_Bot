from config import dp
from aiogram import types
from classes.init_class import vk, ud, us

@dp.message_handler(commands=['search'])
async def my_del(message: types.Message):

    entry = ud.check_id(message.from_user.id)
    if entry:
        ud.extract_data(message.from_user.id)
        vk.change_head_flag(message.from_user.id , 2)
        await message.answer('Введи искомое значение👀: ', parse_mode="html")
