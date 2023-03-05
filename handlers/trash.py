from config import dp
from aiogram import types
from classes.init_class import sec, ud, vk, us


@dp.message_handler()
async def trash(message: types.Message):
    us_id = message.from_user.id
    entry = ud.check_id(us_id)

    if entry:
        flag = ud.check_flag(us_id)
        match flag[1]:
            case 1:
                match flag[2]:
                    case 1: 
                        vk.fill(us_id, 0, message.text)
                        ud.change_support_flag(us_id, 2)
                        await message.answer("Введи дату:")
                    case 2:
                        res = sec.verifi_date(message.text)
                        if res:
                            vk.fill(us_id, 1, res[0])
                            ud.change_support_flag(us_id, 3)
                            await message.answer("Введи имя события:")
                        else:
                            await message.answer("Миша, все хуйня, давай по новой!")
                    case 3:
                        vk.fill(us_id, 2, message.text)
                        ud.change_support_flag(us_id, 0)
                        ud.change_head_flag(us_id, 0)
                        us.app_str(us_id)
                        vk.kick(us_id)
            case 2:

                pass

            case 3:

                pass

            case _:
                await message.answer('выбери действие')
    else:
        pass