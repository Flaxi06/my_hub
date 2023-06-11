from telebot import TeleBot
from telebot import types
import requests
from bs4 import BeautifulSoup
import random



bot = TeleBot(token="5919564224:AAGbUPzOK0wF3FzdRcfLJJz02qzedbihJ8I")

@bot.message_handler(commands = ["start" ])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True)
    button1 = types.KeyboardButton("👋 Поздороваться"  )
    button2 = types.KeyboardButton("Задать вопрос ❓")
    button3 = types.KeyboardButton("🏆 Спортивные cобытия")
    button4 = types.KeyboardButton("😜 Случайная шутка")
    button5 = types.KeyboardButton("💰 Поддержать автора")
    button6 = types.KeyboardButton("📈 Курс к рублю 📉" )
    keyboard.add(button1 ,button2 , button3 , button4, button5 , button6 )
    bot.send_message(message.from_user.id, text="Нажимай на панель ↘ " , reply_markup=keyboard )
    

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет.. Спасибо что пользуешься мной!👋)")
        
    elif(message.text == "Задать вопрос ❓"):
        markup = types.ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True)
        btn1 = types.KeyboardButton("🍊 Как меня зовут? 🍊")
        btn2 = types.KeyboardButton("🍓 Что я могу? 🍓")
        btn3 = types.KeyboardButton("🥝 Сколько мне лет? 🥝")
        btn4 = types.KeyboardButton("🍌 Кто тебя создал? 🍌")
        back = types.KeyboardButton("🍋 Вернуться в главное меню 🍋")
        markup.add(btn1, btn2,btn3,btn4, back)
        bot.send_message(message.from_user.id, text=" Задай мне вопрос ❓↘", reply_markup=markup)
    
    elif(message.text == "🍊 Как меня зовут? 🍊"):
        bot.send_message(message.from_user.id, "У меня нет имени...😔")
    
    

    elif message.text == "🥝 Сколько мне лет? 🥝":
      bot.send_message(message.from_user.id, "Вы представляете я сам не знаю  , наверное 1321 год☠")


    elif message.text == "🍌 Кто тебя создал? 🍌":
      bot.send_message(message.from_user.id, "🤫Оооо.. мне запретили произносить его имя, но начинается оно на А.....")

    elif message.text == "🍓 Что я могу? 🍓":
        keyboard = types.ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться" )
        button2 = types.KeyboardButton("Задать вопрос ❓")
        button3 = types.KeyboardButton("🏆 Спортивные cобытия")
        button4 = types.KeyboardButton("😜 Случайная шутка" )
        button5 =types. KeyboardButton("💰 Поддержать автора")
        button6 = types.KeyboardButton("📈 Курс к рублю 📉")
        keyboard.add(button1 ,button2 , button3 , button4, button5 , button6 , )
        bot.send_message(message.from_user.id, text="Всё это🤯↘" , reply_markup=keyboard )

    elif message.text == "🍋 Вернуться в главное меню 🍋":
                   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=2)
                   button1 = types.KeyboardButton("👋 Поздороваться " )
                   button2 = types.KeyboardButton("Задать вопрос ❓")
                   button3 = types.KeyboardButton("🏆 Спортивные cобытия")
                   button4 = types.KeyboardButton("😜 Случайная шутка")
                   button5 =types. KeyboardButton("💰 Поддержать автора")
                   button6 = types.KeyboardButton("📈 Курс к рублю 📉")
                   keyboard.add(button1 ,button2 , button3 , button4, button5 , button6)
                   bot.send_message(message.from_user.id, text="🍏 Вы вернулись в главное меню ↘", reply_markup=keyboard)


    elif message.text == "📈 Курс к рублю 📉":
                keyboard = types.InlineKeyboardMarkup(row_width= 2 )
                key_dollar = types.InlineKeyboardButton(text="USD", callback_data='12')
                key_euro = types.InlineKeyboardButton(text="EUR", callback_data='13')
                keyboard.row(key_dollar , key_euro)
                bot.send_message(message.from_user.id, text="Выбери)", reply_markup=keyboard)


    elif message.text == "Рост":
                keyboard = types.InlineKeyboardMarkup()
                key_rost = types.InlineKeyboardButton(text="Стать выше", callback_data='14')
                keyboard.add(key_rost)
                bot.send_message(message.from_user.id, text="Жми)", reply_markup=keyboard)
                   
                  

        


    elif message.text == "😜 Случайная шутка":
      response = requests.get("https://randstuff.ru/joke/")
      soup = BeautifulSoup(response.text, "html.parser")
      fact = random.choice(soup.find_all(class_="text"))
      bot.send_message(message.from_user.id,   fact.td.text )


    elif message.text == "💰 Поддержать автора":
      bot.send_message(message.from_user.id, "✅ Поддержать) ✅ https://www.donationalerts.com/r/andrey_hqdishkin" )


    elif(message.text == "🏆 Спортивные cобытия"):
                keyboard = types.InlineKeyboardMarkup()
                key_football = types.InlineKeyboardButton(text="⚽Футбол⚽", callback_data='1')
                keyboard.add(key_football)
                key_hockey = types.InlineKeyboardButton(text="🏒Хоккей🏒", callback_data='2')
                keyboard.add(key_hockey)
                key_tennis = types.InlineKeyboardButton(text="🎾Теннис🎾", callback_data='3')
                keyboard.add(key_tennis)
                key_basketball = types.InlineKeyboardButton(text="🏀Баскетбол🏀", callback_data='4')
                keyboard.add(key_basketball)
                key_volleyball = types.InlineKeyboardButton(text="🏐Волейбол🏐", callback_data='5')
                keyboard.add(key_volleyball)
                key_boks = types.InlineKeyboardButton(text="🤜Бокс🤛", callback_data='6')
                keyboard.add(key_boks)
                key_sand_volleyball = types.InlineKeyboardButton(text="🏐Пляжный волейбол🏐", callback_data='7')
                keyboard.add(key_sand_volleyball)
                key_gandball = types.InlineKeyboardButton(text="✨Гандбол✨", callback_data='8')
                keyboard.add(key_gandball)
                key_ping_pong = types.InlineKeyboardButton(text="🏓Настольный теннис🏓", callback_data='9')
                keyboard.add(key_ping_pong)
                key_kiber_sport = types.InlineKeyboardButton(text="🎮Киберспорт🎮", callback_data='10')
                keyboard.add(key_kiber_sport)
                bot.send_message(message.from_user.id, "Что тебя интересует?" ,reply_markup=keyboard )


    
    
    else:
                   keyboard = types.InlineKeyboardMarkup()
                   key_nepon = types.InlineKeyboardButton(text="🔄Начать сначала🔄", callback_data='11')
                   keyboard.add(key_nepon)
                   bot.send_message(message.from_user.id, "Что-то непонятное начни сначала" , reply_markup=keyboard )





@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
   number = 0
   if call.data == "1":
       keyboard = types.InlineKeyboardMarkup()
       button1 = types.InlineKeyboardButton("Футбол", url='https://www.flashscore.com.ua/')
       keyboard.add(button1)
       bot.send_message(call.from_user.id, "Привет, друг! Нажми на кнопку и перейди на сайт)" , reply_markup=keyboard )



   elif call.data == "2":
     keyboard = types.InlineKeyboardMarkup()
     button1 = types.InlineKeyboardButton("Хоккей", url='https://www.flashscore.com.ua/hockey/')
     keyboard.add(button1)
     bot.send_message(call.from_user.id, "Привет, друг! Нажми на кнопку и перейди на сайт)" , reply_markup=keyboard )


   elif call.data == "3":
      keyboard = types.InlineKeyboardMarkup()
      button1 = types.InlineKeyboardButton("Теннис", url='https://www.flashscore.com.ua/tennis/')
      keyboard.add(button1)
      bot.send_message(call.from_user.id, "Привет, друг! Нажми на кнопку и перейди на сайт)" , reply_markup=keyboard )



   elif call.data == "4":
      keyboard = types.InlineKeyboardMarkup()
      button1 = types.InlineKeyboardButton("Баскетболл", url='https://www.flashscore.com.ua/basketball/')
      keyboard.add(button1)
      bot.send_message(call.from_user.id, "Привет, друг! Нажми на кнопку и перейди на сайт)" , reply_markup=keyboard )


   elif call.data == "5":
      keyboard = types.InlineKeyboardMarkup()
      button1 = types.InlineKeyboardButton("Воллейбол", url='https://www.flashscore.com.ua/volleyball/')
      keyboard.add(button1)
      bot.send_message(call.from_user.id, "Привет, друг! Нажми на кнопку и перейди на сайт)" , reply_markup=keyboard )


   elif call.data == "6":
      keyboard = types.InlineKeyboardMarkup()
      button1 = types.InlineKeyboardButton("Бокс", url='https://www.flashscore.com.ua/boxing/')
      keyboard.add(button1)
      bot.send_message(call.from_user.id, "Привет, друг! Нажми на кнопку и перейди на сайт)" , reply_markup=keyboard )


   elif call.data == "7":
      keyboard = types.InlineKeyboardMarkup()
      button1 = types.InlineKeyboardButton("Пляжный волейбол", url='https://www.flashscore.com.ua/beach-volleyball/')
      keyboard.add(button1)
      bot.send_message(call.from_user.id, "Привет, друг! Нажми на кнопку и перейди на сайт)" , reply_markup=keyboard )



   elif call.data == "8":
      keyboard = types.InlineKeyboardMarkup()
      button1 = types.InlineKeyboardButton("Гандболл", url='https://www.flashscore.com.ua/handball/')
      keyboard.add(button1)
      bot.send_message(call.from_user.id, "Привет, друг! Нажми на кнопку и перейди на сайт" , reply_markup=keyboard )



   elif call.data == "9":
      keyboard = types.InlineKeyboardMarkup()
      button1 = types.InlineKeyboardButton("Настольнный теннис", url='https://www.flashscore.com.ua/table-tennis/')
      keyboard.add(button1)
      bot.send_message(call.from_user.id, "Привет, друг! Нажми на кнопку и перейди на сайт" , reply_markup=keyboard )



   elif call.data == "10":
      keyboard = types.InlineKeyboardMarkup()
      button1 = types.InlineKeyboardButton("Киберспорт", url='https://www.flashscore.com.ua/esports/')
      keyboard.add(button1)
      bot.send_message(call.from_user.id, "Привет, друг! Нажми на кнопку и перейди на сайт" , reply_markup=keyboard )


   elif call.data == "11":
      keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
      button1 = types.KeyboardButton("👋 Поздороваться" )
      button2 = types.KeyboardButton("Задать вопрос ❓")
      button3 = types.KeyboardButton("🏆 Спортивные cобытия")
      button4 = types.KeyboardButton("😜 Случайная шутка" )
      button5 =types. KeyboardButton("💰 Поддержать автора")
      button6 = types.KeyboardButton("📈 Курс к рублю 📉")
      keyboard.add(button1 ,button2 , button3 , button4, button5 , button6  )
      bot.send_message(call.from_user.id, text="Нажимай на панель ↘" , reply_markup=keyboard )

   elif call.data == "12":
      response = requests.get("https://quote.rbc.ru/ticker/59111?ysclid=lc4vtst07w123625597")
      soup = BeautifulSoup(response.text, "html.parser")
      fact = random.choice(soup.find_all(class_="chart__info__row js-ticker"))
      bot.send_message(call.from_user.id, "📉 Курс доллара к рублю 📈"  )
      bot.send_message(call.from_user.id, fact.span.text  )

   elif call.data == "13":
     response = requests.get("https://quote.ru/ticker/72383")
     soup = BeautifulSoup(response.text, "html.parser")
     fact = random.choice(soup.find_all(class_="chart__info__row js-ticker"))
     bot.send_message(call.from_user.id, "📉 Курс евро к рублю 📈"  )
     bot.send_message(call.from_user.id, fact.span.text  )


   elif call.data == "15":
      number = + 1
      bot.send_message(call , 1308823526 , number )










bot.polling(none_stop=True, interval=0)



