import cv2
import time

import configparser
import weather_voice

# 天気予報を取得してファイルに保存
latitude = "緯度"
longitude = "経度"

# 設定ファイルを読み込む
config = configparser.ConfigParser()
config.read('config.ini')


# APIキーを取得
API_key = config['API_KEYS']['OPENWEATHER_API_KEY']
deepl_auth_key = config['API_KEYS']['DEEPL_AUTH_KEY']

# Haar Cascade分類器の読み込み
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Webカメラの設定
cap = cv2.VideoCapture(0)  # 0番目のカメラを使用する場合

# 最後の顔検出時刻
lastTime = None

# メインループ
while True:


    # カメラからのフレームの取得
    ret, frame = cap.read()
    
    # フレームのグレースケール化
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 顔の検出
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # 検出された顔に対する処理
    for (x, y, w, h) in faces:
        # 検出自の処理（検出から１分たったら再度イベント動かす
        if lastTime is None or time.perf_counter() - lastTime > 60:
            # 検出時刻更新
            lastTime = time.perf_counter()
            print("今日の天気を顔認識したのでお知らせ")
            weather_voice.generate_and_play_weather_report(latitude, longitude, API_key, deepl_auth_key)
        

# 後処理
cap.release()
cv2.destroyAllWindows()
