from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import keyboard
import Sheets

bot=Bot(token="2017969126:AAFnwoUBblbLrfwgeovN-HwJgYr74liy5_Q")
dp = Dispatcher(bot)
"""
@dp.message_handler(commands="helps")
async def helps_command(msg: types.Message):
    await bot.send_message(msg.from_user.id,Sheets.res[0])"""

@dp.message_handler()
async def send(msg: types.Message):
    if msg.text ==  '/start': 
        await bot.send_message(msg.from_user.id, 'Привет, я бот, который подскажет, какие мероприятия будут проводиться \
в ближайшее время в ЮУрГУ\nВыбери день', reply_markup = keyboard.menu1)
    elif msg.text == 'Сегодня':
        await bot.send_message(msg.from_user.id, Sheets.res[0], reply_markup = keyboard.menu1)
        await bot.send_message(msg.from_user.id, 'О чём?', reply_markup= keyboard.inline_menu1)
    elif msg.text == 'Завтра':
        await bot.send_message(msg.from_user.id, Sheets.res[1], reply_markup= keyboard.menu1)
        await bot.send_message(msg.from_user.id, 'О чём?', reply_markup= keyboard.inline_menu2)
    elif msg.text == 'Послезавтра':
        await bot.send_message(msg.from_user.id, 'Что? *Здесь будет название*\nГде? *Здесь будет место*\nКогда? *Здесь будет время*', reply_markup= keyboard.menu1)
        await bot.send_message(msg.from_user.id, 'О чём?', reply_markup= keyboard.inline_menu3)
    else:
        await bot.send_message(msg.from_user.id, 'Это не чат-бот!\nНажимай на кнопки.')

@dp.callback_query_handler(lambda call: True)
async def callback_inline(call):
    if call.message:
        if call.data == 'Сегодня' or 'Завтра' or 'Послезавтра':
            await bot.answer_callback_query(call.id)
            await bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.message_id, text ='*Инфа о мероприятии из описания группы*')



executor.start_polling(dp)
