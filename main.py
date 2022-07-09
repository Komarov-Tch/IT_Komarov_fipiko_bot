import telebot
import datetime
from telebot import types
from config import Config

bot = telebot.TeleBot(Config.token)
contacts = ['https://vk.com/itcube.norilsk',
            'https://kvantorium-norilsk.ru/',
            '+79139999999',
            '+79999999999']

timetable_info = {'line1': ['PY-1/22-1', 'PYJ-1/22-2', 'PY-2/22-5'],
                  'line2': ['PY-3/22-2', 'PY-1/21-4', 'PY-3/22-1'],
                  'line3': ['PY-3/22-5', 'PY-5/20-2', 'PY-3/22-1'],
                  'line4': ['Yandex-2', 'Yandex-3', 'Yandex-1']}


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_hello = types.KeyboardButton("Поздороваться")
    btn_table = types.KeyboardButton("Расписание занятий")
    btn_weather = types.KeyboardButton("Контакты")
    btn_site = types.KeyboardButton("Перейти на сайт")
    btn_news = types.KeyboardButton("Новости")
    markup.add(btn_table, btn_weather, btn_site)
    markup.add(btn_hello, btn_news)
    bot.send_message(message.chat.id, f'Привет, я бот для связи с сайтом. Выбери одну из кнопок', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Поздороваться":
        bot.send_message(message.chat.id, text="Привеееет человече!)")
    elif message.text == "Контакты":
        for contact in contacts:
            bot.send_message(message.chat.id, text=f"{contact}")
    elif (message.text == "Расписание занятий"):
        num_weekday = datetime.datetime.today().weekday()
        info = ''
        if num_weekday == 0 or num_weekday == 3:
            info = [timetable_info[i][0] for i in timetable_info.keys()]
        elif num_weekday == 1 or num_weekday == 4:
            info = [timetable_info[i][1] for i in timetable_info.keys()]
        elif num_weekday == 2 or num_weekday == 5:
            info = [timetable_info[i][2] for i in timetable_info.keys()]
        if info:
            for i in info:
                bot.send_message(message.chat.id, f"Сегодня занятие у группы {i}")
        else:
            bot.send_message(message.chat.id, f'Сегодня выходной')
    elif message.text == "Перейти на сайт":
        bot.send_message(message.chat.id, text="Тут будет ссылка на сайт")
    elif message.text == "Новости":
        bot.send_message(message.chat.id, text="Тут будут новости, но пока их нет")
    else:
        bot.send_message(message.chat.id, text="На такую команду я не запрограммировал.")


bot.polling(none_stop=True, interval=0)
