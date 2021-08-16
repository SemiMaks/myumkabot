import telebot
import configure
from telebot import types

client = telebot.TeleBot(configure.config['token'])
print('Токен принят...')


@client.message_handler(commands=['get_info', 'info'])
def get_user_info(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text='ДА', callback_data='yes')
    item_no = types.InlineKeyboardButton(text='НЕТ', callback_data='no')

    markup_inline.add(item_yes, item_no)
    client.send_message(message.chat.id, 'Желаете узнать небольшую информацию о вас?')


@client.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'yes':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_id = types.KeyboardButton('МОЙ ID')
        item_username = types.KeyboardButton('МОЙ НИК')

        markup_reply.add(item_id, item_username)
        client.send_message(call.message.chat.id, 'Нажмите на одну из кнопок', reply_markup=markup_reply
                            )
    elif call.data == 'no':
        pass


@client.message_handler(content_types=['text', 'document', 'audio'])
def get_text(message):
    if message.text == 'МОЙ ID':
        client.send_message(message.chat.id, f'Your ID: {message.from_user.id}')
    elif message.text == 'МОЙ НИК':
        client.send_message(message.chat.id,
                            f'Your username: {message.from_user.first_name} {message.from_user.first_name}')
    else:
        client.send_message(message.chat.id, 'Я тебя не понимаю. Напиши /help.')


# @client.message_handler(content_types=['text', 'document', 'audio'])
# def get_text(message):
#     if message.text.lower() == 'привет':
#         client.send_message(message.chat.id, 'Привет, неизвестный user!')
#     elif message.text.lower() == '/help':
#         client.send_message(message.chat.id, 'Напиши "привет"')
#     else:
#         client.send_message(message.chat.id, 'Я тебя не понимаю. Напиши /help.')

client.polling(none_stop=True, interval=0)
