
## Зависимости

Для запуска проекта установить python версии 3.7 и выше и pip и postgres 12 и выше

## Локальный запуск проекта

### После клонирования проекта
```bash
git clone ssh https://github.com/Dancher-man/landAccounting
```
### Выполните все следующие команды

### Извините через докер не смог настроить postgres(postgis)

### Склонируйте проект, после установите виртуальное окружение командой
```bash
python -m venv venv
```

### Активируйте виртуальное окружение командой
```bash
source venv/bin/activate
venv\Scripts\activate
```

### Установите зависимости командой
```bash 
pip install -r requirements.txt
```

### Перейдите в папку LandAccounting командой
```bash
cd LandAccounting
```
### Пропишите данные БД postgres в файле settings.py
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'landaccounting',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```

### Затем в терминале выполните команды
```bash
sudo -i -u postgres
psql
CREATE DATABASE your_db;
\c your_db
CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;
\q
logout
```

### Примените миграцию командой
```bash
python manage.py migrate
```

### Затем создайте суперюзера с помощью команды
```bash
docker-compose run web python manage.py createsuperuser
```
### Запустите проект командой
```bash
python manage.py runserver 8000
```


