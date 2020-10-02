import telebot  # telegram-bot API
#open file with key
key_value = '1021237352:AAFgrsGq5Q6SA-B7XnWWgLAOyLW1fif9t9k'
bot = telebot.TeleBot(key_value)

#keyboard config
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Favorites', 'Add to favorites')
#keyboard1.row('Favorites', 'Add to favorites', 'Delete from favorites', 'Settings', 'Help')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello there!', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == "Favorites":
        bot.send_message(message.chat.id, 'Hello general Kenobi')
    elif message.text.lower() == 'Add to favorites':
        bot.send_message(message.chat.id, 'Bye general Kenobi')
    else:
        bot.send_message(message.chat.id, "I don't get it!")


bot.polling()
