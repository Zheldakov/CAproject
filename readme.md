# Система контроля и учета

### Проект предназначен для учета и контроля выполненных сервисных работ на технике.

### Разрабатывается под конкретные нужды и задачи инженерного подразделения сельскохозяйственной компании.

## Технологии

- Python
- Django
- MSSQL
- API

## Запуск проекта

### 1. Клонировать репозиторий:

```shell
git clone https://github.com/Zheldakov/CAproject
````

### 2. Создать и активировать виртуальное окружение:

```shell
python -m venv venv
# Для Linux/macOS:
source venv/bin/activate
# Для Windows:
.\venv\Scripts\activate
```

### 3. Установка библиотек

Библиотеки в проект устанавливаются из файла requirements.txt

```shell
pip install - r requirements.txt
```

### Настройте окружение:

Создайте файл .env в корне проекта с содержимым (пример в .env_sample)

```
MS_SQL_SERVER='ваш_MSSQL_сервер'
MS_SQL_DATABASE='ваша_база_проекта'
MS_SQL_PAD_DATABASE='master' # БД-прокладка для создания БД проекта
MS_SQL_DRIVER='ODBC Driver 18 for SQL Server'
MS_SQL_USER='пользователь_БД'
MS_SQL_KEY='пароль_пользователя_БД'

SU_DJANGO_PASSWORD='пароль_администратора_проекта'
MODERATOR_PASSWORD='пароль_модератора_проекта'
USER_PASSWORD='пароль_пользователя'

SECRET_KEY='ваш_секретный_ключ_прокта_django'

GLONASSSOFT_LOGIN='пользователь_ГлонассСофт'
GLONASSSOFT_PASSWORD='пароль_ГлонассСофт'
```

### 4. Создание базы данных

Для создания базы данных, используйте следующую команду:

```shell
pythone manage.py ccdb
```

### 5. Миграции

Для создания миграций необходима выполнить команду:

```shell
pythone manage.py makemigrations
```

Для проведения миграций в базу данных следует выполнить команду:

```shell
pythone manage.py migrate
```

Команды для создания БД и пользователей в \users\management\commands

### 6. Создание пользователей

Для первоначального создания пользователей требуется использовать команду:

```shell
pythone manage.py ccsu
```

Команда создаст администратора, модератора и обычного пользователя по умолчанию.

### 7. Заполнение БД данными для примера (не обязательно)

```shell
# загрузка примера данных по технике
python loaddata fixtures/all_technic_data_is_base.json 
# загрузка примера новостей
python loaddata fixtures/all_news_data_is_base.json 
```

### 8. Запуск сервера

```shell
python manage.py runserver 
```

## Использование

После запуска сервера перейдите по адресам:

Основное приложение: http://localhost:8000/

Админ-панель: http://localhost:8000/admin_panel/

___

## Структура проекта

```
CAproject/
├── technic/        # Приложение по работе с техникой
├── news/           # Приложение по работе с новостями
├── users/          # Приложение по работе с пользователями
├── config/         # Настройки проекта
├── fixtures/       # fixtures для заполнения БД
├── static/         # Статические файлы
├── .env            # Переменные окружения
├── manage.py
└── requirements.txt
```
### В проекте используются запросы к сторонним продуктам:

- [ГлонассSoft](https://glonasssoft.ru/)
- [Cropwise](https://www.cropwise.com/)

___

## Модели приложения Users

### Модель пользователя User:

    email - почта (соответственно login для входа)
    role - роль пользователя
    first_name - имя
    last_name - фамилия
    phone - телефон
    telegram - телеграмм
    avatar - аватарка
    is_active - активный / не активный пользователь

### Модель ролей пользователя UserRoles:

    ADMIN - администратор
    MODERATOR - модератор
    USER - пользователь

___

## Модели приложения News

### Модель новостной статьи Article

    title - название статьи
    description - описание статьи
    date - дата создания статьи
    text - текст статьи

___

## Модели приложения Technic

### Модель типа техники TypeTechnic

    name - наименования типа техники
    description - описание типа техники

### Модель подразделения/отделения Department

    name - наименования подразделения/отделения
    description - описание подразделения/отделения

### Модель техники Technic

    name - наименование техники
    type - тип техники
    photo - фотография техники
    number - государственный номер
    invnumber - инвентарный номер
    imei - номер IMEI
    department -  подразделение/отделение

### Модель технического обслуживания

    technic - техника на которой проведен сервис
    work - проведенная работа
    date - дата проведения работы
    description - описание работы

___

## Автор

- [Желдаков Андрей](https://github.com/Zheldakov/)