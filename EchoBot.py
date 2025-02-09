# Импорт библиотек
import telebot
from telebot import types

try:
    # Берём у BotFather токен (бот должен быть заранее создан)
    token = '8080066714:AAH8JI7BrLukLmOsluQ1yQY3uEDPT9qph87'
    # Определяем нашего бота с помощью токена
    bot = telebot.TeleBot(token)


    # Определяем команду боту для /start
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id,
                         "Йоу, рад видеть! Это Эхо-бот, можешь написать сообщение и я его повторю!")
        # Отправляем сообщение по id чата


    # Функция для отправки сообщения пользователю
    @bot.message_handler(content_types='text')  # Для текстовых сообщений
    def message_reply(message):
        bot.send_message(message.chat.id, message.text)


    bot.infinity_polling()

except BaseException:
    print("Что-то пошло не так.")