from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import keyboard
import Sheets

bot=Bot(token="2080056712:AAHNlgVIsNF6YrFCcuMxAgEbrUOb3XLmpzQ")
dp = Dispatcher(bot)

@dp.message_handler(commands="helps")
async def helps_command(msg: types.Message):
    await bot.send_message(msg.from_user.id,Sheets.res[0])

@dp.message_handler()
async def send(msg: types.Message):
    if msg.text=="Покажи клавиатуру":
        await msg.reply("Hi")
        await bot.send_message(msg.from_user.id,"Вот твоя клавиатура",reply_markup=keyboard.menu1)
    elif msg.text == "Фильтры для поиска":
        await bot.send_message(msg.from_user.id,"Вот твои фильтры",reply_markup=keyboard.menu2)
    elif msg.text == "Назад":
        await bot.send_message(msg.from_user.id, "Вот твой первый список", reply_markup=keyboard.menu1)
    elif msg.text == "Купить блогера":
        await bot.send_message(msg.from_user.id, "Вот твой первый список блогеров", reply_markup=keyboard.menu3)
    elif msg.text =="Открыть список блогеров":
        await bot.send_message(msg.from_user.id, "Вот твой первый список блогеров", reply_markup=keyboard.inline_menu)

@dp.callback_query_handler(lambda call:True)
async def callback_inline(call):
    if call.message:
        if call.data=="give":
            await bot.answer_callback_query(call.id)
            await bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Отдал")



executor.start_polling(dp)