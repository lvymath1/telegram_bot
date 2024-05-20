from telegram.ext import CommandHandler
from telegram import Update

async def start(update: Update, context):
    await update.message.reply_text('你好，感谢你与我聊天，我是 Lisa 机器人。')

async def help(update: Update, context):
    await update.message.reply_text('我是 Lisa 机器人，请随意输入信息，我会进行回复。')

async def custom(update: Update, context):
    await update.message.reply_text('这是自定义命令')

start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
custom_handler = CommandHandler('custom', custom)
