import requests
from .utils.const_value import API_LOCATION_KEY, API, KEY1, KEY2, METRIC, LANGUAGE


def get_weather_info(city):
    # 第一步：根据城市名称获取城市的 API Key
    location_data, location_key = get_city_location_key(city)

    if location_key:
        # 第二步：使用获取的 API Key 查询天气信息
        weather_info = fetch_weather(location_data, location_key)
        return weather_info
    else:
        return "无法获取该城市温度"

def get_city_location_key(city):
    api_keys = [KEY1, KEY2]
    for key in api_keys:
        response = requests.get(API_LOCATION_KEY, params={
            'apikey': key,
            'q': city,
            'language': LANGUAGE,
        }, timeout=1)
        location_data = response.json()
        if location_data and 'Code' in location_data and location_data['Code'] == 'ServiceUnavailable':
            continue
        # 提取城市的 API Key
        if location_data and len(location_data) > 0:
            return location_data[0], location_data[0]['Key']
    return None, None

def fetch_weather(location_data, location_key):
    print(location_data)
    api_keys = [KEY1, KEY2]
    for KEY in api_keys:
        response = requests.get(API + location_key, params={
            'apikey': KEY,
            'language': LANGUAGE,
            'details': True,
            'metric': METRIC,
        }, timeout=1)
        weather_data = response.json()  # 将 JSON 响应转换为 Python 字典
        if weather_data and 'Code' in weather_data and weather_data['Code'] == 'ServiceUnavailable':
            continue
        # 提取关键信息并转换为字符串
        country_localized_name = location_data['Country']['LocalizedName']
        city_localized_name = location_data['AdministrativeArea']['LocalizedName']
        localized_name = location_data['LocalizedName']
        icon_phrase = weather_data['DailyForecasts'][0]['Day']['IconPhrase']
        min_temp = weather_data['DailyForecasts'][0]['Temperature']['Minimum']['Value']
        max_temp = weather_data['DailyForecasts'][0]['Temperature']['Maximum']['Value']
        feel_temperature = weather_data['DailyForecasts'][0]['RealFeelTemperature']['Minimum']['Phrase']
        air_pollen = weather_data['DailyForecasts'][0]['AirAndPollen'][0]['Value']


        weather_str = f"{city_localized_name}{localized_name}明天的天气为{icon_phrase}，最高温度{max_temp}℃，" \
                      f"最低温度{min_temp}℃, 体感温度{feel_temperature}, 空气质量为{air_pollen}。"
        return weather_str
    return "无法获取该城市温度"