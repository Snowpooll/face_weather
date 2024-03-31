import requests
import json
from datetime import datetime
import deepl

def get_weather_forecast(latitude, longitude, API_key, deepl_auth_key):
    # DeepL Translatorのインスタンスを生成
    translator = deepl.Translator(deepl_auth_key)

    # OpenWeather APIのURL
    url = "https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=hourly,minutely&units=metric&lang=ja&appid={API_key}"
    url = url.format(lat=latitude, lon=longitude, API_key=API_key)

    # APIリクエスト
    response = requests.get(url)
    jsondata = response.json()

    # 今日の日付を取得
    today = datetime.now().date()

    # 今日の天気予報を探す
    for daily_forecast in jsondata["daily"]:
        date = datetime.fromtimestamp(daily_forecast["dt"]).date()
        if date == today:
            min_temp = daily_forecast["temp"]["min"]
            max_temp = daily_forecast["temp"]["max"]
            weather = daily_forecast["weather"][0]["main"]
            description = daily_forecast["weather"][0]["description"]
            break

    # 天気をdeeplで日本語に翻訳
    weather_japanese = translator.translate_text(weather, target_lang="JA").text

    # 今日の天気予報をまとめる
    today_weather_repo = f"今日の天気は{weather_japanese}、予想最高気温は{max_temp}度、予想最低気温は{min_temp}度です"
    return today_weather_repo

# 関数を使用して天気予報を取得
latitude = "緯度"
longitude = "経度"
API_key = "OpenWeather API key"
deepl_auth_key = "DeepL API key"

weather_report = get_weather_forecast(latitude, longitude, API_key, deepl_auth_key)

# 天気予報をテキストファイルに保存
with open('weather.txt', 'w') as file:
    file.write(weather_report)
