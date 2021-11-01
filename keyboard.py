from aiogram.types import ReplyKeyboardRemove,\
    ReplyKeyboardMarkup, KeyboardButton,\
    InlineKeyboardMarkup, InlineKeyboardButton

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