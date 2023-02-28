from aiogram import types
from config import dp
from text import help_text
from classes.init_class import us, sec, ud

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer(help_text)
    