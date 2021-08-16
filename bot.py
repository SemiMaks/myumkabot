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

@client.message_handler(content_types=['text', 'document', 'audio'])
def get_text(message):
    if message.text.lower() == 'привет':
        client.send_message(message.chat.id, 'Привет, неизвестный user!')
    elif message.text.lower() == '/help':
        client.send_message(message.chat.id, 'Напиши "привет"')
    else:
        client.send_message(message.chat.id, 'Я тебя не понимаю. Напиши /help.')

client.polling(none_stop=True, interval=0)
