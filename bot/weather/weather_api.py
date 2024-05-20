import requests
from .utils.const_value import API, KEY, UNIT, LANGUAGE


def get_weather_info(city):
    # 调用你的天气 API 来获取天气信息
    # 替换这里的代码为实际的 API 调用和处理
    return fetchWeather(city)


def fetchWeather(location):
    response = requests.get(API, params={
        'key': KEY,
        'location': location,
        'language': LANGUAGE,
        'unit': UNIT
    }, timeout=1)

    data = response.json()  # 将 JSON 响应转换为 Python 字典

    # 提取所需的天气信息
    location_name = data['results'][0]['location']['name']
    temperature = data['results'][0]['now']['temperature']
    weather_text = data['results'][0]['now']['text']

    # 构建天气信息字符串
    weather_info = f"{location_name}的天气是{weather_text}天，当前气温为{temperature}摄氏度。"

    return weather_info

