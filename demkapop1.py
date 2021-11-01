from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types import InputFile
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token='2017969126:AAFnwoUBblbLrfwgeovN-HwJgYr74liy5_Q')

dp = Dispatcher(bot)

but1 = KeyboardButton('Сегодня')
but2 = KeyboardButton('Завтра')
but3 = KeyboardButton('Послезавтра')

menu1 = ReplyKeyboardMarkup(resize_keyboard=True).add(but1).row(but2, but3)


descrip1 = InlineKeyboardButton('Подробнее', callback_data='Сегодня')
descrip2 = InlineKeyboardButton('Подробнее', callback_data='Завтра')
descrip3 = InlineKeyboardButton('Подробнее', callback_data='Послезавтра')


inline_menu1 = InlineKeyboardMarkup().add(descrip1)
inline_menu2 = InlineKeyboardMarkup().add(descrip2)
inline_menu3 = InlineKeyboardMarkup().add(descrip3)

@dp.message_handler()
async def send(msg: types.Message):
    if msg.text ==  '/start':
        await bot.send_message(msg.from_user.id, 'Привет, я бот, который подскажет, какие мероприятия будут проводиться \
в ближайшее время в ЮУрГУ\nВыбери день', reply_markup = menu1)
    elif msg.text == 'Сегодня':
        await bot.send_message(msg.from_user.id, 'Что? *Здесь будет название*\nГде? *Здесь будет место*\nКогда? *Здесь будет время*', reply_markup = menu1)
        await bot.send_message(msg.from_user.id, 'О чём?', reply_markup= inline_menu1)
    elif msg.text == 'Завтра':
        await bot.send_message(msg.from_user.id, 'Что? *Здесь будет название*\nГде? *Здесь будет место*\nКогда? *Здесь будет время*', reply_markup= menu1)
        await bot.send_message(msg.from_user.id, 'О чём?', reply_markup= inline_menu2)
    elif msg.text == 'Послезавтра':
        await bot.send_message(msg.from_user.id, 'Что? *Здесь будет название*\nГде? *Здесь будет место*\nКогда? *Здесь будет время*', reply_markup= menu1)
        await bot.send_message(msg.from_user.id, 'О чём?', reply_markup= inline_menu3)
    else:
        await bot.send_message(msg.from_user.id, 'Это не чат-бот!\nНажимай на кнопки.')

@dp.callback_query_handler(lambda call: True)
async def callback_inline(call):
    if call.message:
        if call.data == 'Сегодня' or 'Завтра' or 'Послезавтра':
            await bot.answer_callback_query(call.id)
            await bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.message_id, text ='*Инфа о мероприятии из описания группы*')


executor.start_polling(dp)