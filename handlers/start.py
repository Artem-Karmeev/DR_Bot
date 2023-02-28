from config import dp
from aiogram import types
from classes.init_class import us, ud

@dp.message_handler(commands=['start'])
async def start(message: types.Message):

    have = ud.check_id(message.from_user.id)

    if have:
        await message.answer('Че как?')
    else:
        us.add_user(message.from_user.id)
        await message.answer(f'{message.from_user.first_name}, добро пожаловать!')
    

