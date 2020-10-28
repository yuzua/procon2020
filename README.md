# procon2020

## docekr-composeでコンテナ起動
```
$docker-compose up --build -d #コンテナ起動
$docker-compose exec web bash #コンテナ内に入る
pipenv install --system #Pipfileをコンテナ内に適用
python manage.py makemigrations 
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000 #サーバー起動
```

## コンテナ操作
```
$docker-compose up -d ＃コンテナをバックグラウンドで起動
$docker-compose ps ＃コンテナの起動状態を確認
$docker-compose down #起動中のコンテナを停止
```


## Gitコマンド
自分のリポジトリをローカルにクローン
```
$ git clone 自分のリポURL　
```
リモートの追加(フェッチ元の変更を自分のリポジトリに反映させるため)
```
$ git remote add リモート名　リモートURL
```
ブランチを指定してpull
```
$ git pull origin ブランチ名
```
リモートの内容をpull
```
$ git pull リモート名　ブランチ名
```
カレントディレクトリの変更をステージング
```
$ git add .
```
変更をコミット(-mオプションでコメントを入力)
```
$ git commit -m '変更メッセージ入力'
```
変更を自分のリモートリポジトリにpush
```
$ git push origin ブランチ名
```

## psycopg2-binary(djangoでpostgresを使えるようにするやつ)をpipenvでインストール
```
$ pipenv install psycopg2-binary
```
