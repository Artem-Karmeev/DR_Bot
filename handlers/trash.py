from config import dp
from aiogram import types
from classes.init_class import sec, ud, vk, us
from text import help_text


@dp.message_handler()
async def trash(message: types.Message):
    us_id = message.from_user.id
    entry = ud.check_id(us_id)

    if entry:
        flag = vk.check_flag(us_id)
        match flag[1]:
            case 1: # добавить значение
                match flag[2]:
                    case 1: 
                        res = sec.verifi_date(message.text)
                        if res:
                            vk.fill(us_id, 0, res[0])
                            vk.change_support_flag(us_id, 2)
                            await message.answer("Введи комментарий:")
                        else:
                            await message.answer('Не понял, повтори', parse_mode="HTML")
                    case 2:
                        if not ' →  ' in message.text:
                            vk.fill(us_id, 1, message.text)
                            vk.change_support_flag(us_id, 0)
                            vk.change_head_flag(us_id, 0)
                            us.app_str(us_id)
                            vk.kick_tmp_data(us_id)
                        else:
                            await message.answer('Засунь свой " →  " сам знаешь куда! ')
            case 2: # поиск

                result = ud.search(us_id, message.text)
                if result:
                    await message.answer(result)
                else:
                    await message.answer('Нет совпадений, возможно список пуст.')
                    ud.kick_data(us_id)

            case 3: # удаление

                match flag[2]:
                    case 1:
                        res = ud.search(us_id, message.text, flag=True)
                        if res:
                            if len(res.split('\n')) == 2:
                                ud.del_event(us_id, int(res[:1]))
                                ud.overwrite_data(us_id)
                                vk.change_head_flag(us_id, 0)
                                vk.change_support_flag(us_id, 0)
                                ud.kick_data(us_id)
                                await message.answer(f'Событие удалено.')
                            else:
                                vk.change_support_flag(us_id, 2)
                                await message.answer(res)
                                await message.answer(f'Нашлось несколько событий:\n\n{res} \nотправь ID события, чтобы его удалить:')
                        else:
                            await message.answer('Нет совпадений, возможно список пуст.')
                            vk.change_head_flag(us_id, 0)
                            vk.change_support_flag(us_id, 0)
                            ud.kick_data(us_id)
                    case 2:

                        len_list = ud.return_len(us_id)

                        if message.text.strip().isdigit():

                            if -1 < int(message.text.strip()) < len_list:

                                ud.del_event(us_id, int(message.text.strip()))
                                ud.overwrite_data(us_id)
                                vk.change_head_flag(us_id, 0)
                                vk.change_support_flag(us_id, 0)
                                ud.kick_data(us_id)
                                await message.answer(f'Событие удалено.')
                            else:
                                await message.answer('В списке нет записи с таким ID.')
                        else:
                            await message.answer('Введи число которое находится левее от 📅.')

                                
            case _:
                await message.answer(help_text, parse_mode="HTML")
    else:
        pass