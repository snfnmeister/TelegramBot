import telebot  # telegram-bot API
from src.favorites_unit import FavoritesUnit

# read key from txt file

f = open('/home/snfn/PycharmProjects/keys/telegram_key')
key_value = str(f.read()).rstrip()
bot = telebot.TeleBot(key_value)
f.close()

# keyboard config
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Favorites', 'Add to favorites', 'Help')
# keyboard1.row('Favorites', 'Add to favorites', 'Delete from favorites', 'Settings', 'Help')

favorites_list = []
favorites_list.extend(['URL1', 'URL2', 'URL3', 'URL4', 'URL5'])
fav_len = len(favorites_list)
favorite_data = ""

for i in range(fav_len):
    temp_string = '{0}. {1}\n'.format(i, favorites_list[i])
    favorite_data += temp_string


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello there!', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == "Favorites":
        bot.send_message(message.chat.id, favorite_data)
    elif message.text == 'Add to favorites':
        bot.send_message(message.chat.id, 'Bye general Kenobi')
    elif message.text == 'Help':
        bot.send_message(message.chat.id, 'Help')
    else:
        bot.send_message(message.chat.id, "I don't get it!")


bot.polling()

# elif message.text.lower() == 'Add to favorites':
