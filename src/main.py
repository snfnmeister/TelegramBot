import telebot  # telegram-bot API

# open file with key
key_value = 'will be added'
bot = telebot.TeleBot(key_value)

# keyboard config
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Favorites', 'Add to favorites', 'Help')
# keyboard1.row('Favorites', 'Add to favorites', 'Delete from favorites', 'Settings', 'Help')

favorites_list = ['URL1', 'URL2']


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello there!', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == "Favorites":
        bot.send_message(message.chat.id, favorites_list[0] + '\n' + favorites_list[1])
    elif message.text == 'Add to favorites':
        bot.send_message(message.chat.id, 'Bye general Kenobi')
    elif message.text == 'Help':
        bot.send_message(message.chat.id, 'Help')
    else:
        bot.send_message(message.chat.id, "I don't get it!")


bot.polling()

# elif message.text.lower() == 'Add to favorites':
