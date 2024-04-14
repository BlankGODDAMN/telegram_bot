import telebot;
from telebot import types
bot = telebot.TeleBot(<токен>)
question = ['Компьютер это -',
            'Выберите из списка устройство ввода.',
            'Перед отключением компьютера информацию можно сохранить...',
            'Какое устройство не находится в системном блоке?',
            'Какого вида принтеров не существует?']
answers = [['устройство для обработки аналоговых сигналов',
            'устройство для решения математических задач',
            'устройство для обработки информации',
            'устройство для работы с числами'],
           ['принтер', 'мышь', 'монитор', 'наушники'],
           ['в оперативной памяти', 'во внешней пямяти', 'в процессоре', 'на материнской плате'],
           ['жесткий диск', 'видеокарта', 'материнская плата', 'монитор'],
           ['матричный', 'струйный', 'лазерный', 'фотографический']]
key = ['3', '2', '2', '4', '3']
@bot.message_handler(content_types=['text'])
def start(message):
    global i, right
    i = 0
    right = 0
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Начало теста")
        test(message)
    else:
        bot.send_message(message.from_user.id, 'Чтобы запустить тест введи команду /start')
def test(message):
    global i
    keyboard = types.InlineKeyboardMarkup()
    key_1 = types.InlineKeyboardButton(text=answers[i][0], callback_data='1')
    keyboard.add(key_1)
    key_2= types.InlineKeyboardButton(text=answers[i][1], callback_data='2')
    keyboard.add(key_2)
    key_3 = types.InlineKeyboardButton(text=answers[i][2], callback_data='3')
    keyboard.add(key_3)
    key_4= types.InlineKeyboardButton(text=answers[i][3], callback_data='4')
    keyboard.add(key_4)
    bot.send_message(message.from_user.id, text=question[i], reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global i, right
    if call.data == key[i]:
        right += 1
    i += 1
    if i < len(question):
        test(call)
    else:
        bot.send_message(call.message.chat.id, 'Вы набрали ' + str(right) + ' балл(а/ов) из ' + str(len(question)))
bot.polling(none_stop=True, interval=0.1)