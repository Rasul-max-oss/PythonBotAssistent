import telebot
import random
from telebot import types

f = open('facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()
f = open('thinks.txt', 'r', encoding='UTF-8')
thinks = f.read().split('\n')
f.close()
f = open('jokes.txt', 'r', encoding='UTF-8')
jokes = f.read().split('\n')
f.close()


# Создаем бота
bot = telebot.TeleBot('5456039417:AAHS1rxlhMOo5dzMJ6JD8d109tNmYL12lDI')
# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Факт")
        item2=types.KeyboardButton("Поговорка")
        item3=types.KeyboardButton("Анекдот")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(m.chat.id, 'Нажми: \nФакт для получения интересного факта\nПоговорка — для получения мудрой цитаты ',  reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Факт' :
            answer = random.choice(facts)
    elif message.text.strip() == 'Поговорка':
            answer = random.choice(thinks)
    elif message.text.strip()=="Анекдот":
            answer=random.choice(jokes)


    bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True, interval=0)