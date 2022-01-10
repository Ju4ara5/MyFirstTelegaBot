#  в этом файле будет запускаться бот
import asyncio
from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN

#  поток в котором будут обрабатываться все события:
loop = asyncio.get_event_loop()

#  сам бот:
bot = Bot(BOT_TOKEN, parse_mode='HTML')

#  создаем обработчика и доставщика (диспачер):
dp = Dispatcher(bot, loop=loop)

if __name__ == '__main__':
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)
