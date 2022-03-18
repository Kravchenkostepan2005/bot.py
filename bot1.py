"""telegram bot who works with NBU API"""

import requests
import datetime
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup, chat
from lib2to3.fixes.fix_input import context

TOKEN = '5109879811:AAHhjXil990ryl0C4eCF5oM3DEjFojl0lxQ'
print("Bot is up")
updater = Updater(TOKEN)


def welcome(update, context):
    chat = update.effective_chat
    buttons = [[KeyboardButton('USD')], [KeyboardButton('EUR')], [KeyboardButton('PLN')], [KeyboardButton('GEL')]]
    context.bot.send_message(chat_id=chat.id, text='Hello! I am your currency bot',
                             reply_markup=ReplyKeyboardMarkup(buttons))


def currency_rate1(update, context):
    global message
    chat = update.effective_chat
    currency_code = update.message.text
    if currency_code in ('USD', 'EUR', 'PLN', 'GEL'):
        currency_rate1 = requests.get(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode='
                                      f'{currency_code}&date=20220313&json').json()
        rate = currency_rate1[0]['rate']
        message = f'{currency_code} rate: {rate} UAH'
    context.bot.send_message(chat_id=chat.id, text=message)

def create_message_to_json(currency_code, date, rate):
    data = {"currency code" : currency_code, "date" : date, "rate" : rate}
    d = json.dumps(data)
    print(d)

def write_to_file(message):
    with open("f.json", "a") as f:
        f.append(json.dumps(data))


def get_details_from_api(currency_code, date):
    api = requests.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=")
                 f'{currency_code}&date={date}&json').json
    print(api)

def create_2_dates():
    date1 = datetime.datetime.now()
    date2 = date1 - 1
    print(date1, date2)

def currency_rate1(update, context):
    global message
    chat = update.effective_chat
    currency_code = update.message.text
    date1, date2 = create_2_dates()
    if currency_code in ('USD', 'EUR', 'PLN', 'GEL'):
        currency_rate1 = get_details_from_api(currency_code, date1)
        currency_rate2 = get_details_from_api(currency_code, date2)
        rate = currency_rate1[0]['rate']
        currency_difference = currency_rate1 - currency_rate2
        message = f'{currency_code} rate: {rate} UAH'
        write_to_file(create_message_to_json())


        def load_file_currency(currency):
            with open("accounts1.txt") as f:
                json.load = load_file_currency
                json.load["information"].append(currency)
                with open("accounts1.txt", "w") as f1:
                    json.dump(load_file_currency, f1, ensure_ascii=False, indent=2)
                print(load_file_currency())
            write_to_file(create_message_to_json())
    context.bot.send_message(chat_id=chat.id, text=message)
    rate = currency_rate1[0]['rate']
    message = f'{currency_code} rate: {rate} UAH'
    context.bot.send_message(chat_id=chat.id, text=message)
    message1 = f'{currency_code}'
    context.bot.send_message(chat_id=chat.id, text=message1)

disp = updater.dispatcher
disp.add_handler(CommandHandler('start', welcome))
disp.add_handler(MessageHandler(Filters.all, currency_rate))

updater.start_polling()
updater.idle()
