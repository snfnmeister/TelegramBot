import telebot  # telegram-bot API

bot = telebot.TeleBot('token will be added')

#keyboard config
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Help', 'Add')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello there!', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'Hello':
        bot.send_mesasge(message.chat.id, 'Hello general Kenobi')
    elif message.text.lower() == 'Bye-bye':
        bot.send_message(message.chat.id, 'Bye general Kenobi')
    else:
        bot.send_message(message.chat.id, "I don't get it!")


bot.polling()
