import re

from bot.weather.weather_api import get_weather_info


async def handle_message(update, context):
    message_type = update.message.chat.type
    text = update.message.text

    print(f'User ({update.message.chat.id}) said in {message_type}: "{text}"')

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

    if '天气' in processed:
        city = extract_city_name(text)
        if city:
            weather_info = get_weather_info(city)
            if weather_info:
                return weather_info
            else:
                return '抱歉，我找不到这个城市的天气信息。'
        else:
            return '抱歉，我无法识别你提供的城市名称。'

    return '抱歉，我不理解你说的是什么...'

def extract_city_name(text):
    match = re.search(r'天气\s*(\S+)', text)
    if match:
        return match.group(1)
    return None


