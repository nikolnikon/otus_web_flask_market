# otus_web_flask_market

Интернет-магазин, сделанный с использованием фреймворка Flask.

## Установка

С использованием git и установкой зависимостей из requirements.txt (для разработки):
```bash
1. Скачать исходный код веб-приложения
$ git clone https://github.com/nikolnikon/otus_web_flask_market.git

2. Установить необходимые зависимости
$ cd otus_web_flask_market
$ pip install -r requirements.txt

3. Создать базу данных
$ docker-compose up -d

4. Выполнить миграции
$ flask db upgrade

5. Загрузить данные в БД
$ flask fixtures load

Для загрузки даных в Window пришлось поменять кодироку файлов на cp-1251. Предполагаю, что если делать то же
самое под Linux, то нужно будет кодировать их в utf-8.
```

## Запуск приложения
Данная иструкция распространяется на запуск приложения с помощью предоставляемого Flask веб-сервера. Такой вариант не 
подходит для развертывания в "боевом" окружении. Подходы к развертыванию в "боевом" окружении описаны в документации.  
```bash
1. Создать в корневой директории (otus_web_flask_market) файл .env

2. Прописать в нем переменные окружения, соответствующие натсройкам веб-приложения. По умолчанию значения настроек 
берутся из файла config.py

3. В файле .flaskenv указать необходимую конфигурацию, задав соответствующее значение переменной окружения FLASK_ENV.
Возможные значения: development, production.

3. Выполнить команду
$ flask run
```

## Работа приложения
Страница со списком продуктов

![Список продуктов](https://i.gyazo.com/0425318a7bf7152c4f2e74ec1df49129.png)

Страница конкретного продукта

![Конкретный продукт. Описание](https://i.gyazo.com/906b0c6da0435ee0ad9304e9eea70c78.png)

![Конкретный продукт. Характеристики](https://i.gyazo.com/a2d8eb22b43794ad113d31bd65ac7ad6.png)

## Лицензия
Проект распространяентся под лицензией MIT. Подробная информация в файле
[LICENSE](https://github.com/nikolnikon/otus_web_django_market/blob/master/LICENSE)
