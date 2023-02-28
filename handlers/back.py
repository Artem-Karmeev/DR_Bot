from config import dp
from aiogram import types
from classes.init_class import us, sec, ud

@dp.message_handler(commands=['back'])
async def back(message: types.Message):
    pass