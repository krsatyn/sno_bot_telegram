import sqlite3
import telebot

from telebot import types
from settings import bot_token, db_name
from database_functionals import get_gamedev_raspis, get_web_raspis
#Основное тело программы

"""Подключение базы данных"""
db_connect = sqlite3.connect(db_name, check_same_thread=False)
cursor = db_connect.cursor()

"""Подключение бота"""
token = bot_token
bot = telebot.TeleBot(token=bot_token)

#Ключ слово используется для контроля текущей задачи (задача назначается кнопкой)
BOT_ANSWER_KEY = ""

"""Реализация кнопок"""
@bot.message_handler(commands=['start'])
def start_answer(message):
    #создаём разметку
    markup = types.ReplyKeyboardMarkup(row_width=1)
    #Кнопки
    button_join_sno = types.InlineKeyboardButton("Я хочу вступить в SNO ITS SAMGUPS", callback_data="join_sno")
    button_get_raspisanie = types.InlineKeyboardButton("Я хочу получить расписание", callback_data="get_raspisanie")
    #Добавляем кнопки в разметку
    markup.add(button_join_sno, button_get_raspisanie)
    bot.send_message(message.chat.id, text="Приветствую тебя всеми своими лапами!\nЯ создан, что бы облегчить жизнь кожаным существам, таким как ты, человек)\nЧем могу быть полезен?", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def logic_response(message):
    global BOT_ANSWER_KEY
    
    #меню после возврата
    if message.text == "Назад в меню":
        #создаём разметку
        markup = types.ReplyKeyboardMarkup(row_width=1)
        #Кнопки
        button_join_sno = types.InlineKeyboardButton("Я хочу вступить в SNO ITS SAMGUPS", callback_data="join_sno")
        button_get_raspisanie = types.InlineKeyboardButton("Я хочу получить расписание", callback_data="get_raspisanie")
        #Добавляем кнопки в разметку
        markup.add(button_join_sno, button_get_raspisanie)
        bot.send_message(message.chat.id, text="Хорошо, я верну тебя назад, мой кожанный господин\nЧем могу быть полезен?", reply_markup=markup)
    
    #заявка
    elif message.text == "Я хочу вступить в SNO ITS SAMGUPS":
        bot.send_message(message.chat.id, text="Хорошо, мой кожанный друг, я отпрвил тебе ссылку на анкетку, заполни её и жди ответа!\n//место для ссылки//")
    
    #Расписание
    elif message.text == "Я хочу получить расписание":
        
        BOT_ANSWER_KEY = "raspisan_menu"
        markup = types.ReplyKeyboardMarkup(row_width=1)
        button_get_gamedev = types.InlineKeyboardButton("Расписание GameDev", callback_data="get_gamedev")
        button_get_web = types.InlineKeyboardButton("Расписание WEB", callback_data="get_web")
        button_back_menu = types.InlineKeyboardButton("Назад в меню", callback_data="back_menu")
        markup.add(button_get_gamedev, button_get_web, button_back_menu)
        bot.send_message(message.chat.id, text="Хорошо, выбери направление, которое тебя интересует!", reply_markup=markup)
    
    #Расписание GameDev
    elif message.text == "Расписание GameDev":
        respone = get_gamedev_raspis()
        bot.send_message(message.chat.id, text=f"Твоё расписание, ковбой:\n{respone}")
    
    #Расписание web
    elif message.text == "Расписание WEB":
        respone = get_web_raspis()
        bot.send_message(message.chat.id, text=f"Твоё расписание, ковбой:\n{respone}")
    
    #Загушка
    else:
        bot.send_message(message.chat.id, text=f"Ой ой, я не знаю такие команды, пожалуйста выбери что нибудь из кнопочек")
#запуск бота   
bot.polling()