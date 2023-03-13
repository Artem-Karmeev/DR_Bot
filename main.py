from handlers import dp
from aiogram import executor
from config import bot


async def startup(_):
    print('Hello!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=startup)