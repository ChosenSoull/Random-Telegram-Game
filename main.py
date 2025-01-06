import telebot
import random

bot = telebot.TeleBot("7925654342:AAE5FBb6eAcCVww2pi9dyca0Gp86NHM-YsQ")

def game(message):
    secret_number = random.randint(1, 100)
    message = bot.send_message(message.chat.id, "Я загадал число от 1 до 100. Попробуй угадать!")

    @bot.message_handler(func=lambda message: True)
    def guess_number(message):
        try:
            guess = int(message.text)
            if guess > secret_number:
                bot.reply_to(message, "Загаданное число меньше.")
            elif guess < secret_number:
                bot.reply_to(message, "Загаданное число больше.")
            else:
                bot.reply_to(message, "Поздравляю, ты угадал!")
                return
        except ValueError:
            bot.reply_to(message, "Введите число!")

@bot.message_handler(commands=['start'])
def start(message):
    game(message)

bot.polling()

bot.polling()


