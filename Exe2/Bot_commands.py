from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, CallbackContext
from telegram import Update
import datetime
import logging
from spy1 import log_1



logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
	log_1(update, context)
	await update.message.reply_text(f'Привет! {update.effective_user.first_name}, привет привет привет... Доделываю бота! ;)')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
	    # """Send a message when the command /help is issued."""
	log_1(update, context)
	await update.message.reply_text("Набери '/hello', /help, /time, /summ {ЧИСЛО} и {ЧИСЛО} или просто что-нибудь )")
	await update.message.reply_text("/mult {ЧИСЛО} и {ЧИСЛО}, /div {ЧИСЛО} и {ЧИСЛО}, /diff {ЧИСЛО} и {ЧИСЛО}  )")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
	log_1(update, context)
	    # """Echo the user message."""
	await update.message.reply_text(update.message.text)
	await update.message.reply_text((f'{update.effective_user.first_name}, это просто повторялка :)'
	                                 f' И я пока ничего не умею, но научусь!'))


async def bot_time(update: Update, context: ContextTypes.DEFAULT_TYPE):
	log_1(update, context)
	await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def start(update, context):
	log_1(update, context)
	await context.bot.send_message(chat_id=update.effective_chat.id,
		text="I'm a bot, please talk to me!")

async def summ(update, context):
	log_1(update, context)
	msg = update.message.text
	print(msg)

	items = msg.split()
	x = int(items[1])
	y = int(items[2])
	print(f'{x} + {y} = {x + y}')
	await update.message.reply_text(f'{x} + {y} = {x + y}')


async def diff(update, context):
	log_1(update, context)
	msg = update.message.text
	print(msg)

	items = msg.split()
	x = int(items[1])
	y = int(items[2])
	print(f'{x} - {y} = {x - y}')
	await update.message.reply_text(f'{x} - {y} = {x - y}')


async def mult(update, context):
	log_1(update, context)
	msg = update.message.text
	print(msg)

	items = msg.split()
	x = int(items[1])
	y = int(items[2])
	print(f'{x} * {y} = {x * y}')
	await update.message.reply_text(f'{x} * {y} = {x * y}')


async def div(update, context):
	log_1(update, context)
	msg = update.message.text
	print(msg)

	items = msg.split()
	x = int(items[1])
	y = int(items[2])
	print(f'{x} / {y} = {x / y}')
	await update.message.reply_text(f'{x} / {y} = {x / y}')