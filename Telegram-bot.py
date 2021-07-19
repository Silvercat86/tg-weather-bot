import os
import requests
from telegram.ext import CommandHandler,Updater, dispatcher,MessageHandler, Filters

#  ---------------------------------------
#  response= requests.get('https://api.ipify.org')#получает данные с заданного сайта
#  print(response)#выводит даные своего типа
#  print(response.text)#выводит данные типом str

#  response= requests.get('https://api.telegram.org/bot1800458602:AAHWEOruS7iy4980Ul0rBYyMzqkrI4rYkQE/getUpdates')
#  data = (response.json())
#  print(data['result'][1]['message']['text'])#путь значений в словаре

#  Бот в телеге----------------------------------------------
BOT_TOKEN=os.getenv('BOT_TOKEN')

updater = Updater(token='BOT_TOKEN',use_context=True)  # проверяет если что нового в памяти бота'''

dispatcher = updater.dispatcher#управляет командами


#  ------------------------


def start(update , context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="C тебя город, с меня погода")#реагриует на старт (см след)
    print (update.effective_chat.id)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)#задает название команды

#  ------------------------


def weather(update, context):
    city = update.message.text
    w = requests.get(f'https://wttr.in/{city}?format=2')
    context.bot.send_message(chat_id=update.effective_chat.id, text=w.text)# отправляет тоже сообщение что и человек


weather_handler = MessageHandler(Filters.text & (~Filters.command), weather)
dispatcher.add_handler(weather_handler)

print('Hello')

updater.start_polling()#запуск пограммы
updater.idle()#что бы продолжало работать вечно(зацикливает)
