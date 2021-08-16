import telebot
import configure

client = telebot.TeleBot(configure.config['token'])
print('Токен принят...')


@client.message_handler(content_types=['text', 'document', 'audio'])
def get_text(message):
    if message.text.lower() == 'привет':
        client.send_message(message.from_user.id, 'Привет, неизвестный user!')
    elif message.text.lower() == '/help':
        client.send_message(message.from_user.id, 'Напиши "привет"')
    else:
        client.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши /help.')

client.polling(none_stop=True, interval=0)
