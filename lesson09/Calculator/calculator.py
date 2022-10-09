import telebot
from telebot import types
import parsing
import parsecomplex

# иницируем бота
bot = telebot.TeleBot("5606269494:AAFngD9467jJo8nS8icVEdEYHAIGtoQPCBY")

expr = ''

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/stop' :
        bot.stop_polling()
    try:
        if '[' in message.text :
            expr = parsecomplex.calculate(message.text)
        else :
            expr = parsing.calculate(message.text)
        bot.send_message(message.from_user.id, expr)
    except :
        bot.send_message(message.from_user.id, "Ой-ой. Что-то введено не так")

bot.infinity_polling()