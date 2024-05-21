import os
import re

from bot.bing_daily.bing_daily import bing_daily
from bot.dog_dairy.dog_dairy import dog_dairy
from bot.openai_gpt.gpt import gpt_answer_questions
from bot.weather.weather_api import get_weather_info


async def handle_message(update, context):
    message_type = update.message.chat.type
    text = update.message.text

    print(f'User ({update.message.chat.id}) said in {message_type}: "{text}"')

    response = handle_response(text)

    # Check if the response is a text or an image
    if isinstance(response, tuple):
        image_path, image_title = response
        if os.path.exists(image_path):
            print('Bot: Sent an image response')
            with open(image_path, 'rb') as image_file:
                await context.bot.send_photo(chat_id=update.message.chat.id, photo=image_file, caption=image_title)
        else:
            print('Bot: Image file not found')
            await update.message.reply_text("抱歉，Lisa找不到壁纸了，请稍后再试")
    else:
        print('Bot:', response)
        await update.message.reply_text(response)


def handle_response(text):
    processed = text.lower()

    if processed in ('hello', 'hi'):
        return '嗨，你好！'

    if 'How are you' in processed:
        return '我很好，谢谢你。'

    if 'I love python' in processed:
        return '记得订阅！'

    if '壁纸' in processed:
        return bing_daily()

    # 服务器无法加入此功能
    # if '舔狗日记' in processed:
    #     dog_dairy_answer = dog_dairy()
    #     if dog_dairy_answer:
    #         return dog_dairy_answer
    #     else:
    #         return '抱歉，我无法返回添狗日记。'

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

    if text:
        return gpt_answer_questions(text)
    return '抱歉，我无法识别你提供的语言。'

def extract_gpt_msg(text):
    match = re.search(r'(?<=gpt)\s*[\u4e00-\u9fa5]+', text)
    if match:
        return match.group(0).strip()  # 去除可能的前后空格
    return None

def extract_city_name(text):
    match = re.search(r'[\u4e00-\u9fa5]+(?=天气)', text)
    if match:
        return match.group(0)
    return None

