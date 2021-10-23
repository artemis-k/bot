import json
import telebot
from telebot import types

token = '2012966113:AAFYO_gwt462cM8nzxPmk2pNqtGnlAHN7aI'

bot = telebot.TeleBot(token, parse_mode=None)


def gen_menu():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(types.InlineKeyboardButton('Информатика', callback_data='inf'),
               types.InlineKeyboardButton('Основы программирования', callback_data='op'))
    return markup


def inf_menu():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(types.InlineKeyboardButton('Занять место', callback_data='inf_join'),
               types.InlineKeyboardButton('Выйти из очереди', callback_data='inf_leave'),
               types.InlineKeyboardButton('Список очереди', callback_data='inf_check'))
    return markup


def op_menu():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(types.InlineKeyboardButton('Занять место', callback_data='op_join'),
               types.InlineKeyboardButton('Выйти из очеред', callback_data='op_leave'),
               types.InlineKeyboardButton('Список очереди', callback_data='op_check'))
    return markup


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'inf':
        bot.edit_message_text('Вы выбрали информатику теперь выберите действие', reply_markup=inf_menu(),
                              chat_id=call.from_user.id, message_id=call.message.message_id)
    elif call.data == 'op':
        bot.edit_message_text('Вы выбрали ОП теперь выберите действие.', reply_markup=op_menu(),
                              chat_id=call.from_user.id, message_id=call.message.message_id)
    elif call.data == 'inf_join':
        with open('queue_info.json', 'w') as f:
            queue_info = list(json.load(f))
            queue_info.append(call.from_user.id)
            f.clear()
            f.write(json.dumps(queue_info))
            f.close()
        bot.send_message(chat_id=call.from_user.id, text='Вы вступили в очередь по информатике')
    elif call.data == 'op_join':
        with open('queue_op.json', 'w') as f:
            queue_op = list(f.load(f))
            queue_op.append(call.from_user.id)
            f.clear()
            f.write(json.dumps(queue_op))
            f.close()
        bot.send_message(chat_id=call.from_user.id, text='Вы вступили в очередь по ОП')
    elif call.data == 'inf_leave':
        with open('queue_inf.json', 'r+') as f:
            queue_info = list(json.load(f))
            queue_info.pop([0])
            f.clear()
            f.write(json.dumps(queue_info))
            f.close()
        bot.send_message(chat_id=call.from_user.id, text='Вы вышли из очереди по информаd')
        with open('queue_op.json', 'r+') as f:
            queue_op = list(f.load(f))
            queue_op.pop([0])
            f.clear()
            f.write(json.dumps(queue_op))
            f.close()
        bot.send_message(chat_id=call.from_user.id, text='Вы вышли из очереди по ОП')
    elif call.data == 'inf_check':
        bot.send_message(chat_id=call.from_user.id, text='Очередь на информатику')
    elif call.data == 'op_check':
        bot.send_message(chat_id=call.from_user.id, text='Очередь на ОП')


@bot.message_handler(func=lambda message: True)
def category(message):
    bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=gen_menu())


bot.infinity_polling()

def get_users():
    data = get_file_data()
    return data.users

def set_user(user_data):
    data = get_file_data()
    data.users.append(user_data)
    save_file_date(data)

def get_file_data():
    filename = 'db.json'
    with open(filename, 'r+') as f:
        data = list(json.load(f))
        f.close()
        return data

def save_file_date(data):
    filename = 'db.json'
    with open(filename, 'w') as f:
        f.write(json.dumps(data))
        f.close()
