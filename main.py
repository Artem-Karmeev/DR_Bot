from handlers import dp
from aiogram import executor
from classes.init_class import us, sec, ud


async def startup(_):
    print('Start')
    us.open()
    


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=startup)