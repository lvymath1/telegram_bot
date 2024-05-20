async def handle_message(update, context):
    message_type = update.message.chat.type
    text = update.message.text

    print(f'User ({update.message.chat.id}) said in {message_type}: "{text}"')

    if message_type == 'group':
        if '@Lisa' in text:
            new_text = text.replace('@Lisa', '').strip()
            response = handle_response(new_text)
        else:
            return
    else:
        response = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

def handle_response(text):
    processed = text.lower()

    if processed in ('hello', 'hi'):
        return '嗨，你好！'

    if 'how are you' in processed:
        return '我很好，谢谢你。'

    if 'i love python' in processed:
        return '记得订阅！'

    return '抱歉，我不理解你说的是什么...'
