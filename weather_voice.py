import subprocess
import pygame
import time
from weather_forecast import get_weather_forecast

def generate_and_play_weather_report(latitude, longitude, API_key, deepl_auth_key):
    # 天気予報を取得してファイルに保存
    weather_report = get_weather_forecast(latitude, longitude, API_key, deepl_auth_key)
    with open('weather.txt', 'w') as file:
        file.write(weather_report)

    # JSONファイルを作成するためのcurlコマンド
    command_json = [
        "curl", "-s", "-X", "POST",
        "192.168.1.69:50021/audio_query?speaker=1",
        "--get", "--data-urlencode", "text@weather.txt"
    ]

    # 音声ファイルを作成するためのcurlコマンド
    command_audio = [
        "curl", "-s", "-H", "Content-Type: application/json", "-X", "POST",
        "-d", "@query.json", "192.168.1.69:50021/synthesis?speaker=1"
    ]

    # JSONファイルと音声ファイルを作成
    with open('query.json', 'w') as file:
        subprocess.run(command_json, stdout=file)
    with open('test_audio.wav', 'wb') as file:
        subprocess.run(command_audio, stdout=file)

    # Pygameで音声ファイルを再生
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound("test_audio.wav")
    sound.play()
    while pygame.mixer.get_busy():
        time.sleep(0.1)

