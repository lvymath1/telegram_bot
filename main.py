from typing import Final
from config import TOKEN

from bot.commands import start, help, custom
from telegram.ext import Application, CommandHandler, MessageHandler

from bot.error import error
from bot.filters import text_filter
from bot.responses import handle_message

TOKEN: Final = TOKEN
BOT_USERNAME: Final = '@Lisa'

if __name__ == '__main__':
    print('正在启动机器人...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('custom', custom))

    # Message
    app.add_handler(MessageHandler(text_filter, handle_message))

    # Error
    app.add_error_handler(error)

    # 轮询机器人
    print('轮询中...')
    app.run_polling(poll_interval=0.5)