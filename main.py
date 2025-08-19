from xml.etree.ElementTree import parse

from config import TOKEN
from telebot import TeleBot
from telebot import types
from telebot.types import ReplyKeyboardMarkup
import text_messages

bot = TeleBot(token=TOKEN)
bot.remove_webhook()   # или bot.delete_webhook()

@bot.message_handler(commands=['start'])
def start_message(message):
    # Создаём клавиатуру
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # Добавляем кнопки по порядку, как в твоем скриншоте
    btn1 = types.KeyboardButton("УНИВЕРСИТЕТЫ")
    btn2 = types.KeyboardButton("Создатели")
    btn3 = types.KeyboardButton("Добавить свои материалы")


    # Каждая кнопка на отдельной строке
    keyboard.add(btn1)
    keyboard.add(btn2)
    keyboard.add(btn3)

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, f"{text_messages.start_message}", reply_markup=keyboard)

reply_keyboard_subject_czu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for item in text_messages.list_sub_czu:
    reply_keyboard_subject_czu.add(item)


reply_keyboard_subject_vse = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for item in text_messages.list_sub_vse:
    reply_keyboard_subject_vse.add(item)


reply_keyboard_univers = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for item in text_messages.list_of_universetes:
    reply_keyboard_univers.add(item)

reply_keyboard_primers = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for item in text_messages.list_of_primers:
    reply_keyboard_primers.add(item)


@bot.message_handler(func=lambda message: True)
def check_button(message):
    match (message.text):
        case "УНИВЕРСИТЕТЫ":
            bot.reply_to(message, "Выберите университет:", reply_markup=reply_keyboard_univers)
        case "Создатели":
            bot.reply_to(message, "Создатели")
        case "Добавить свои материалы":
            bot.reply_to(message, text="<a href='https://www.google.com/'>123</a>", parse_mode="HTML")
        case "Česká zemědělská univerzita v Praze ČZU":
            bot.reply_to(message, "Česká zemědělská univerzita v Praze ČZU", reply_markup=reply_keyboard_subject_czu)
        case "Vysoká Škola Ekonomická v Praze (VŠE)":
            bot.reply_to(message, "Vysoká Škola Ekonomická v Praze (VŠE)", reply_markup=reply_keyboard_subject_vse)
        case "Algoritmizace":
            bot.reply_to(message, "АЛГОРИТМИЗАЦЕ --- ИНФОРМАЦИЯ")
        case "Angličtina ve výpočetní technice - B1":
            bot.reply_to(message, "АНГЛИЙСКИЙ --- ИНФОРМАЦИЯ")
        case "Architektura počítačů":
            bot.reply_to(message, "АРХИТЕКТУРА --- ИНФОРМАЦИЯ")
        case "Matematika":
            bot.reply_to(message, "МАТЕМАЦИЯ --- ИНФОРМАЦИЯ")
        case "Objektové modelování":
            bot.reply_to(message, "ОБЪЕКТЫ --- ИНФОРМАЦИЯ")
        case "Programming in Python":
            bot.reply_to(message, "ПЯТОН --- ИНФОРМАЦИЯ")
        case "Programovací jazyk C++":
            bot.reply_to(message, "ПРОГРАММИРОВАНИЕ --- ИНФОРМАЦИЯ")
        case "Psychologie osobnosti a sociální psychologie":
            bot.reply_to(message, "ПСИХОЛОГИЯ --- ИНФОРМАЦИЯ")
        case "Teorie řízení organizačního systému":
            bot.reply_to(message, "ТРОС --- ИНФОРМАЦИЯ")
        case "Informační a komunikační technologie":
            bot.reply_to(message, "СЕТИ --- ИНФОРМАЦИЯ")
        case "Matematické základy informatiky":
            bot.reply_to(message, "ДИСКРЕТКА --- ИНФОРМАЦИЯ")
        case "Angličtina pro ekonomická studia 1 (B2/C1)":
            bot.reply_to(message, "АНГЛИЙСКИЙ ДЛЯ ЭКОНОМОВ --- ИНФОРМАЦИЯ")
        case "Umělá inteligence a její aplikace":
            bot.reply_to(message, "ИИ --- ИНФОРМАЦИЯ")
        case "Kvantitativní management":
            bot.reply_to(message, "МЕНЕДЖМЕНТ --- ИНФОРМАЦИЯ")
        case "Teorie her a rozhodování":
            bot.reply_to(message, "ТЕОРИЯ ИГР --- ИНФОРМАЦИЯ")
        case "Matematika 2":
            bot.reply_to(message, "МАТЕМАЦИЯ ДЛЯ РАЗВИТЫХ --- ИНФОРМАЦИЯ")
        case "Základy marketingu pro informatiky a statistiky":
            bot.reply_to(message, "ОСНОВЫ МАРКЕТИНГА --- ИНФОРМАЦИЯ")
        case "Datové minimum":
            bot.reply_to(message, "ОСНОВЫ АНАЛИТИКИ ДАННЫХ --- ИНФОРМАЦИЯ")
        case "UX design":
            bot.reply_to(message, "ИНТЕРФЕЙС --- ИНФОРМАЦИЯ")
        case "Právo":
            bot.reply_to(message, "ПРАВО --- ИНФОРМАЦИЯ")
        case "НАЗАД В ОСН. МЕНЮ":
            bot.reply_to(message, "Vysoká Škola Ekonomická v Praze (VŠE)", reply_markup=reply_keyboard_univers)
        case "НАЗАД В ГЛ. МЕНЮ":
            bot.reply_to(message, "ВЫБИРЕТЕ КУДА ХОТИТЕ", reply_markup=start_message(message))


bot.polling()


