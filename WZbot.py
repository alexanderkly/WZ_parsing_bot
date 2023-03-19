from aiogram.utils.markdown import hbold, hlink, hcode, hunderline
from aiogram import Dispatcher, executor, Bot, types
from parsingworkzilla import parsing
from aiogram.dispatcher.filters import Text
import asyncio

token = '6050222744:AAGXHZFi1igkAa3jY-gUdzCR83FmofOiwN4'
user_id = '1581750481'


bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_button = ['проверить задания']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_button)
    await message.answer('Хай', reply_markup=keyboard)




@dp.message_handler(Text(equals='проверить задания'))
async def get_fresh_missoins(message: types.Message):
    tasks = parsing()
    if "заданий по парсингу нет" in tasks:
        await bot.send_message(user_id, 'заданий по парсингу нет', disable_notification=True)
    else:
        await bot.send_message(user_id, tasks, disable_notification=True)

async def news_every_5_min():
    while True:
        tasks = parsing()
        if "заданий по парсингу нет" in tasks:
            await bot.send_message(user_id, 'заданий по парсингу нет', disable_notification=True)
        else:
            await bot.send_message(user_id, tasks, disable_notification=True)
        await asyncio.sleep(300)



async def main():
    task = asyncio.create_task(news_every_5_min())
    await dp.start_polling(dp)


if __name__ == '__main__':
    asyncio.run(main())