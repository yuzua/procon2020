# procon2020

## docekr-composeでコンテナ起動
```
$docker-compose up --build -d　#コンテナ起動
$docker-compose exec web python manage.py bash #コンテナ内に入る
python manage.py runserver 0.0.0.0:8000 #サーバー起動
python manage.py makemigrations 
python manage.py migrate
python manage.py createsuperuser
```

##　コンテナ操作
```
$docker-compose up -d ＃コンテナをバックグラウンドで起動
$docker-compose ps　＃コンテナの起動状態を確認
$docker-compose down #起動中のコンテナを停止
```
