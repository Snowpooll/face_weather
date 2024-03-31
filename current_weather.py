import requests
import json
from datetime import datetime, timedelta

import deepl

auth_key = "DeepL API key"  # Replace with your key
translator = deepl.Translator(auth_key)

# OpenWeather APIのURLとパラメータを設定
url = "https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=hourly,minutely&units=metric&lang=ja&appid={API_key}"
latitude = "緯度"  # 例としての緯度
longitude = "経度"  # 例としての経度
API_key = "OpenWeather API  key"  # あなたのAPIキーをここに入力

# APIリクエスト
url = url.format(lat=latitude, lon=longitude, API_key=API_key)
response = requests.get(url)
jsondata = response.json()

# 今日の日付を取得
today = datetime.now().date()

# # 今日の最高気温と最低気温を探す
# for daily in jsondata["daily"]:
#     date = datetime.fromtimestamp(daily["dt"]).date()
#     if date == today:
#         min_temp = daily["temp"]["min"]
#         max_temp = daily["temp"]["max"]
#         print("今日の最高気温：", max_temp, "度")
#         print("今日の最低気温：", min_temp, "度")
#         break
# 今日の天気予報を探す
for daily_forecast in jsondata["daily"]:
    date = datetime.fromtimestamp(daily_forecast["dt"]).date()
    if date == today:
        min_temp = daily_forecast["temp"]["min"]
        max_temp = daily_forecast["temp"]["max"]
        weather = daily_forecast["weather"][0]["main"]
        description = daily_forecast["weather"][0]["description"]
        break

#天気をdeeplで英語から日本語にする
weather_japanese = translator.translate_text(weather,target_lang="JA")
# 結果の表示
print(f"今日の最高気温: {max_temp}°C")
print(f"今日の最低気温: {min_temp}°C")
print(f"天気: {weather_japanese} ({description})")

# 今日の天気予報をまとめる
today_weather_repo = f"今日の天気は{weather_japanese}、予想最高気温は{max_temp}度、予想最低気温は{min_temp}度です"

# 結果の表示
print(today_weather_repo)
