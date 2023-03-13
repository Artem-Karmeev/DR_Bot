from config import dp
from aiogram import types
from classes.init_class import vk, ud, us
import text

@dp.message_handler(commands=['back'])
async def back_flag(message: types.Message):

    vk.change_head_flag(message.from_user.id, 0)
    vk.change_support_flag(message.from_user.id, 0)
    vk.kick_tmp_data(message.from_user.id)
    ud.kick_data(message.from_user.id)
    await message.answer(text.list_text, parse_mode='HTML')


@dp.message_handler(commands=['on'])
async def on_alerts(message: types.Message):

    entry = ud.check_id(message.from_user.id)
    if entry:
        us.switch(message.from_user.id, True)
        await message.answer('Вкл')


@dp.message_handler(commands=['off'])
async def off_alerts(message: types.Message):

    entry = ud.check_id(message.from_user.id)
    if entry:
        us.switch(message.from_user.id, False)
        await message.answer('Выкл')