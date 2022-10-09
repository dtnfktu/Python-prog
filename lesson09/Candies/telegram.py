import candies
# import colorama
# import emoji
import telebot

bot = telebot.TeleBot('5606269494:AAFngD9467jJo8nS8icVEdEYHAIGtoQPCBY')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, это калькулятор. Введи выражение")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)
