from telegram import Update

async def error(update: Update, context):
    print(f'Update {update} caused error {context.error}')
