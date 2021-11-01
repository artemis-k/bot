from aiogram.types import ReplyKeyboardRemove,\
    ReplyKeyboardMarkup, KeyboardButton,\
    InlineKeyboardMarkup, InlineKeyboardButton

open_list=KeyboardButton("Открыть список блогеров")
buy=KeyboardButton("Купить блогера")
filters=KeyboardButton("Фильтры для поиска")
menu1=ReplyKeyboardMarkup(resize_keyboard=True).add(open_list).row(buy,filters)

city=KeyboardButton("Город")
thematic=KeyboardButton("Тематика")
back=KeyboardButton("Назад")
menu2=ReplyKeyboardMarkup(resize_keyboard=True).add(open_list).row(city,thematic,back)

oneopen=KeyboardButton("1 открытие")
twoopen=KeyboardButton("2 открытие")
threeopen=KeyboardButton("3 открытие")
menu3=ReplyKeyboardMarkup(resize_keyboard=True).add(oneopen,twoopen,threeopen,back)

give_contact=InlineKeyboardButton("Дать контакт", callback_data="give")
inline_menu=InlineKeyboardMarkup().add(give_contact)