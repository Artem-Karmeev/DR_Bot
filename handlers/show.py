from aiogram import types
from config import dp
from classes.init_class import us, sec, ud

@dp.message_handler(commands=['show'])
async def show(message: types.Message):
    us.extract_data(message.from_user.id)
    st = ud.return_data(message.from_user.id)
    ud.kick_data(message.from_user.id)
    await message.answer(st)