from config import dp
from aiogram import types
from classes.init_class import vk, ud


@dp.message_handler(commands=['back'])
async def back_flag(message: types.Message):
    entry = vk.check(message.from_user.id)
    if entry:
        ud.change_head_flag(message.from_user.id, 0)
        ud.change_support_flag(message.from_user.id, 0)
        vk.kick(message.from_user.id)


@dp.message_handler(commands=['on'])
async def on_alerts(message: types.Message):
    pass


@dp.message_handler(commands=['off'])
async def on_alerts(message: types.Message):
    pass