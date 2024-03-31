# face_weather

顔認識すると現在の天気を音声でお知らせします。

動作させるにはAPIキーが必要になります

天気情報取得のため  
OpenWeather API  
https://home.openweathermap.org/users/sign_up  
での登録

天気を日本語に訳すため  
DeepL API   
https://www.deepl.com/ja/translator  
での登録

音声の作成に voicevox の docker が必要になります  
`docker pull voicevox/voicevox_engine:cpu-ubuntu20.04-latest`  
で取得しています

動作させるには

バックグランドでの起動で
-d オプションをつけて  
`docker run -d  -p '192.168.1.69:50021:50021' voicevox/voicevox_engine:cpu-ubuntu20.04-latest`  
というように起動させます  
IPアドレス部分はご自身のマシンのIPに変えてください

current_weather.pyで  
DeepL とOpenWeather API  を使ったテストができます  

weather_forecast.pyの中の  
```
# 関数を使用して天気予報を取得
latitude = "緯度"
longitude = "経度"
API_key = "OpenWeather API key"
deepl_auth_key = "DeepL API key"
```
に値を設定してください

 weather_voice.pyの中の
curlコマンドのIPアドレスを
dokerマシンのIPアドレスに変更してください


kao.py の中の
```
# 天気予報を取得してファイルに保存
latitude = "緯度"
longitude = "経度"
```
の緯度経度を変更してください

