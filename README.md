# hw_python_oop - Калькулятор денег и колорий спринт 2 в Яндекс.Практикум
## Спринт 2 - Калькулятор денег и колорий

### hw_python_oop -  Калькулятор денег и колорий Яндекс.Практикум

Что реализовано в сообществе. Создано и зарегистрировано приложение Posts. Подключена база данных. Десять последних записей выводятся на главную страницу. В админ-зоне доступно управление объектами модели Post: 
можно публиковать новые записи или редактировать/удалять существующие. 

Пользователь может перейти на страницу любого сообщества, где отображаются десять последних публикаций из этой группы.

### Настройка и запуск на ПК

Клонируем проект:

```bash
git clone https://github.com/themasterid/hw02_community.git
```

или

```bash
git clone git@github.com:themasterid/hw02_community.git
```

Переходим в папку с проектом:

```bash
cd hw02_community
```

Устанавливаем виртуальное окружение:

```bash
python -m venv venv
```

Активируем виртуальное окружение:

```bash
source venv/Scripts/activate
```

> Для деактивации виртуального окружения выполним (после работы):
> ```bash
> deactivate
> ```

Устанавливаем зависимости:

```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Применяем миграции:

```bash
python yatube/manage.py makemigrations
```
```bash
python yatube/manage.py migrate
```

Создаем супер пользователя:

```bash
python yatube/manage.py createsuperuser
```

При желании делаем коллекцию статики:

```bash
python yatube/manage.py collectstatic
```

Предварительно сняв комментарий с:
```bash
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

И закомментировав: 
```bash
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

Иначе получим ошибку: You're using the staticfiles app without having set the STATIC_ROOT setting to a filesystem path.

В папку с проектом, где файл settings.py добавляем файл .env куда прописываем наши параметры:

```bash
SECRET_KEY='Ваш секретный ключ'
ALLOWED_HOSTS='127.0.0.1, localhost'
DEBUG=True
```

Не забываем добавить в .gitingore файлы:

```bash
.env
.venv
```

Запускаем проект:

```bash
python yatube/manage.py runserver localhost:80
```

После чего проект будет доступен по адресу http://localhost/

Заходим в http://localhost/admin и создаем группы и записи.
После чего записи и группы появятся на главной странице.

Автор: [Дмитрий Клепиков](https://github.com/themasterid) :+1:
