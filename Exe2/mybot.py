from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, MessageHandler, filters
from Bot_commands import *
import logging

app = ApplicationBuilder().token("5652573054:AAG4tHNldZsSp893bC9s_NW3FEJYzcOovmA").build()


app.add_handler(CommandHandler("hello", hello))


app.add_handler(CommandHandler("start", start))


app.add_handler(CommandHandler("help", help_command))


# on non command i.e message - echo the message on Telegram
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))


app.add_handler(CommandHandler('time', bot_time))


app.add_handler(CommandHandler('summ', summ))

app.add_handler(CommandHandler('diff', diff))

app.add_handler(CommandHandler('mult', mult))

app.add_handler(CommandHandler('div', div))



print('connect')


app.run_polling()
