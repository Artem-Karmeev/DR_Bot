from config import dp
from aiogram import types
from classes.init_class import us, sec, ud


@dp.message_handler()
async def trash(message: types.Message):
    us_id = message.from_user.id
    have = ud.check_id(us_id)
    if have:
        flag = ud.check_flag(us_id)

        match flag[1]:

            case 1:

                match flag[2]:

                    case 3:

                        ud.fill_list(us_id, 0, message.text)
                        ud.change_flag(us_id, 2, 2)
                        await message.answer("Введи дату:")

                    case 2:

                        print(message.text, type(message.text))
                        res = sec.verifi_date(message.text)
                        if res[0]:
                            ud.fill_list(us_id, 1, res[0])
                            ud.change_flag(us_id, 1, 2)
                            await message.answer("Введи имя события:")
                        else:
                            await message.answer("Миша, все хуйня, давай по новой!")

                    case 1:
                        ud.fill_list(us_id, 0, message.text)
                        ud.change_flag(us_id, 2, 2)
                        # await message.answer("Введи дату:")

                        ud.change_flag(us_id, 0, 2)
                        ud.change_flag(us_id, 0, 2)

            case 2:

                pass

            case 3:

                pass

            case _:

                await message.answer('выбери действие')

    else:
        pass