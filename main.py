import telebot

TOKEN = 

bot = telebot.TeleBot(TOKEN)

students = {
    "Михаил Дружинин": [3, 3, 3, 3],
    "Дарья Подшивалова": [4, 3, 5, 3],
    "Максим Вялов": [5, 3, 3, 5],
    "Чесноков Руслан": [4, 3, 3, 5],
    "Игорь Ковязин": [3, 4, 3, 4],
}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот для родителей. Введите имя вашего ребенка, чтобы начать.")

@bot.message_handler(func=lambda message: True)
def check_progress(message):
    child_name = message.text

    if child_name in students:
        grades = students[child_name]
        average_grade = sum(grades) / len(grades)
        bot.reply_to(message, f"Успеваемость ребенка {child_name} - средний балл {average_grade}")
    else:
        bot.reply_to(message, "Ребенок с таким именем не найден. Попробуйте еще раз.")
bot.polling()
