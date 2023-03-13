from config import dp
from aiogram import types
from classes.init_class import sec, ud, vk, us
from text import list_text


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
                            await message.answer('Не понял, повтори:')
                    case 2:
                        if not ' →  ' in message.text:
                            vk.fill(us_id, 1, message.text)
                            vk.change_support_flag(us_id, 0)
                            vk.change_head_flag(us_id, 0)
                            us.app_str(us_id)
                            vk.kick_tmp_data(us_id)
                            await message.answer(' 👌 ')
                        else:
                            await message.answer('Засунь свой " →  " сам знаешь куда! ')
            case 2: # поиск

                result = ud.search(us_id, message.text, flag=True)
                if result:
                    await message.answer(result)
                    ud.kick_data(us_id)
                    vk.change_head_flag(us_id, 0)
                else:
                    await message.answer('Нет совпадений, возможно список пуст.\n\n/back – вернуться в начало\n\nПопробуй еще раз:')
                    

            case 3: # удаление

                    len_list = ud.return_len(us_id)

                    if message.text.strip().isdigit():

                        if -1 < int(message.text.strip()) < len_list:

                            ud.del_event(us_id, int(message.text.strip()))
                            ud.overwrite_data(us_id)
                            vk.change_head_flag(us_id, 0)
                            ud.kick_data(us_id)
                            await message.answer(' 👌 ')
                        else:
                            await message.answer('Неверный ID.\n\n/back – Вернуться в начало\n/search – Найти событие\n\nПопробуй еще раз:')
                    else:
                        await message.answer('ERROR!\n\n/back – Вернуться в начало\n/search – Найти событие\n\nПопробуй еще раз:')

                   
            case _:
                await message.answer(list_text, parse_mode="HTML")
    else:
        await message.answer('Тебя нет в списке.')