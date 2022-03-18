from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from pprint import pprint

TOKEN = '5147834401:AAFIrq8GtNN5y8wg9LWxYKbXWa_4r4VaEsg'
updater = Updater(TOKEN, use_context=True)

dispatcher = updater.dispatcher
print('Bot started. Press Ctrl+Z to exit')


def start(update, context):
    chat = update.effective_chat
    a = 'hello, welcome to calculator bot input/b and write an equation with spaces (like /b 1 + 1)' \
        'operators are: + - * /'
    context.bot.send_message(chat_id=chat.id, text=a)


def any_message(update, context):
    chat = update.effective_chat
    text = update.message.text
    if text.isdigit():
        number = float(text)
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    s = input("Enter s: ")

    def func(a, b, s):
        if s == "+":
            f = a + b
        elif s == "-":
            f = a - b
        elif s == "*":
            f = a * b
        elif s == "/":
            f = a / b
        else:
            return "error"
        return f


def start(update, context):
    chat = update.effective_chat
    t = update.message.text
    try:
        a, b, c, d = l.split()
    except ValueError:
        context.bot.send_message(chat_id=chat.id, text='invalid operation')
        return
    if b.isdigit():
        v = float(b)
    else:
        context.bot.send_message(chat_id=chat.id, text='invalid operation')
    if d.isdigit():
        n = float(d)
    else:
        context.bot.send_message(chat_id=chat.id, text='invalid operation')
    g = func(v, n, g)
    context.bot.send_message(chat_id=chat.id, text=g)
print([
    {
        "name": "Stepan",
        "currency": [
            "USD",
            "EUR",
            "CZK",
            "CHF"
        ]
    }
])


dispatcher.add_handler(CommandHandler('start', start))  # /start
dispatcher.add_handler(MessageHandler(Filters.all, any_message))

updater.start_polling()
updater.idle()
