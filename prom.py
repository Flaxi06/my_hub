from telebot import TeleBot
from telebot import types
import requests
from bs4 import BeautifulSoup
import random



bot = TeleBot(token="5907962261:AAG6J7OpA5jNkActqrCnpT0XNkkCjsPpYAU")



@bot.message_handler(commands = ["start" ])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True)
    button1 = types.KeyboardButton("UP-X" )
    button2 = types.KeyboardButton("CS-GO POLYGON")
    button3 = types.KeyboardButton("EZ CASH")
    button4 = types.KeyboardButton("CS FAIL")
    button5 = types.KeyboardButton("Поддержка")
    keyboard.add(button1 ,button2 , button3 , button4 , button5 )
    bot.send_message(message.from_user.id, text="Привет, я вижу ты здесь за промо 💰. Выбирай на каком сайте тебе нужно промо " , reply_markup=keyboard )


@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "UP-X"):
        keyboard = types.InlineKeyboardMarkup(row_width= 1 )
        key_prom1 = types.InlineKeyboardButton(text="Ссылка на UP-X", callback_data='1')
        keyboard.add(key_prom1)
        bot.send_message(message.from_user.id, text="Для того чтобы получить промик нужно зарегаться по ссылке)", reply_markup=keyboard)
    elif(message.text == "CS-GO POLYGON"):
        keyboard = types.InlineKeyboardMarkup(row_width= 1 )
        key_prom1 = types.InlineKeyboardButton(text="Ссылка на CS-GO POLYGON", callback_data='2')
        keyboard.add(key_prom1)
        bot.send_message(message.from_user.id, text="Для того чтобы получить промик нужно зарегаться по ссылке)", reply_markup=keyboard)
    elif(message.text == "EZ CASH"):
        keyboard = types.InlineKeyboardMarkup(row_width= 1 )
        key_prom1 = types.InlineKeyboardButton(text="Ссылка на EZ CASH", callback_data='3')
        keyboard.add(key_prom1)
        bot.send_message(message.from_user.id, text="Для того чтобы получить промик нужно зарегаться по ссылке)", reply_markup=keyboard)   
    elif(message.text == "CS FAIL"):
        keyboard = types.InlineKeyboardMarkup(row_width= 1 )
        key_prom1 = types.InlineKeyboardButton(text="Ссылка на CS FAIL", callback_data='4')
        keyboard.add(key_prom1)
        bot.send_message(message.from_user.id, text="Для того чтобы получить промик нужно зарегаться по ссылке)", reply_markup=keyboard)
    elif(message.text == "Поддержка"):
        
        bot.send_message(message.from_user.id, text="По всем вопросам пиши - @nety222")

    elif (message.text == "Вернуться в главное меню"):
        keyboard = types.ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True)
        button1 = types.KeyboardButton("UP-X" )
        button2 = types.KeyboardButton("CS-GO POLYGON")
        button3 = types.KeyboardButton("EZ CASH")
        button4 = types.KeyboardButton("CS FAIL")
        button5 = types.KeyboardButton("Поддержка")
        keyboard.add(button1 ,button2 , button3 , button4 , button5 )
        bot.send_message(message.from_user.id, text="Привет, я вижу ты здесь за промо 💰. Выбирай на каком сайте тебе нужно промо " , reply_markup=keyboard )

    





    else:
                   keyboard = types.InlineKeyboardMarkup()
                   key_nepon = types.InlineKeyboardButton(text="🔄Начать сначала🔄", callback_data='5')
                   keyboard.add(key_nepon)
                   bot.send_message(message.from_user.id, "Видимо ты еще не зарегался начни сначала " , reply_markup=keyboard )  
       
       
       

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
   if call.data == "1":
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Вернуться в главное меню")
        keyboard.add(button1)
        bot.send_message(call.from_user.id, text="Для того чтобы получить промик нужно зарегаться по ссылке )" + "https://up5rc7x.life/p/cPEyjcMiTr если ты не можешь зарагаться на этом сайте , но нужен промо тогда зарегайся на другом по другой кнопке",reply_markup=keyboard)
       
   elif call.data == "2":
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Вернуться в главное меню")
        keyboard.add(button1)
        bot.send_message(call.from_user.id, text="Для того чтобы получить промик нужно зарегаться по ссылке) ввести промокод - GOFREEMONEY"+ " https://plg4x.com/ru  если ты не можешь зарагаться на этом сайте , но нужен промо тогда зарегайся на другом по другой кнопке",reply_markup=keyboard )
   elif call.data == "3":
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Вернуться в главное меню")
        keyboard.add(button1)
        bot.send_message(call.from_user.id, text="Для того чтобы получить промик нужно зарегаться по ссылке )"+"  https://ezcash.link/r/owzm7m если ты не можешь зарагаться на этом сайте , но нужен промо тогда зарегайся на другом по другой кнопке", reply_markup=keyboard)
   elif call.data == "4":
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Вернуться в главное меню")
        keyboard.add(button1)
        bot.send_message(call.from_user.id, text="Для того чтобы получить промик нужно зарегаться по ссылке )"+"https://csfail.org/r/GOFREEMONEY если ты не можешь зарагаться на этом сайте  или уже зареган, но нужен промо тогда зарегайся на другом по другой кнопке", reply_markup=keyboard)
   elif call.data == "5":
    keyboard = types.ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True)
    button1 = types.KeyboardButton("UP-X" )
    button2 = types.KeyboardButton("CS-GO POLYGON")
    button3 = types.KeyboardButton("EZ CASH")
    button4 = types.KeyboardButton("CS FAIL")
    button5 = types.KeyboardButton("Поддержка")
    keyboard.add(button1 ,button2 , button3 , button4 , button5)
    bot.send_message(call.from_user.id, text="Привет, я вижу ты здесь за промо 💰. Выбирай на каком сайте тебе нужно промо " , reply_markup=keyboard )





bot.polling(none_stop=True, interval=0)