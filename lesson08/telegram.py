import telebot
bot = telebot.TeleBot('5606269494:AAFngD9467jJo8nS8icVEdEYHAIGtoQPCBY')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет!")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    elif message.text == '/stop' :
        bot.send_message(message.from_user.id, "Бот остановлен")
        bot.stop_bot()
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)