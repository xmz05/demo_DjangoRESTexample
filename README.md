# Простой интернет-магазин на Django и Django REST Framework

## Описание проекта

Этот проект представляет собой простой интернет-магазин, реализованный с использованием Django и Django REST Framework. Проект позволяет управлять товарами, выполняя CRUD-операции, а также предоставляет дополнительные возможности, такие как фильтрация и поиск товаров.

## Установка и запуск проекта

### 1. Установка необходимых зависимостей

Убедитесь, что у вас установлен Python и pip. Затем установите Django и Django REST Framework:

*linux/mac bash & windows cmd*
```
pip install django djangorestframework
```

### 2. Создание и активация виртуального окружения
Рекомендуется использовать виртуальное окружение:

*linux/mac bash*
```
python -m venv venv
source venv/bin/activate 
```
*windows cmd*
```
python -m venv venv
`venv\Scripts\activate`
```

### 3. Клонирование репозитория (если необходимо)
Для клонирования репозитория необходимо выполнить следующую команду:
(перед этим убедитесь, что у вас установлен [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))

*linux/mac bash & windows cmd*
```
git clone https://github.com/???/shop.git
cd shop
```

### 4. Применение миграций
Перейдите в директорию проекта и примените миграции для создания базы данных:

*linux/mac bash & windows cmd*
```
cd shop
python manage.py migrate
```

### 5. Создание суперпользователя
Для доступа к админ. панели django создайте суперпользователя:

*linux/mac bash & windows cmd*
```
python manage.py createsuperuser
```

### 6. Запуск сервера разработки
Запустите сервер разработки для проверки работы проекта:

*linux/mac bash & windows cmd*
```
python manage.py runserver
```

### 7. Проверка работы API
Откройте браузер и перейдите по следующим адресам для проверки доступных эндпоинтов:

- Список всех товаров: <http://127.0.0.1:8000/api/products/>
- Создание нового товара: Используйте метод *POST* на <http://127.0.0.1:8000/api/products/>
- Детальная информация о товаре: <http://127.0.0.1:8000/api/products/{id}/>
- Обновление информации о товаре: Используйте методы *PUT* или *PATCH* на <http://127.0.0.1:8000/api/products/{id}/>
- Удаление товара: Используйте метод *DELETE* на <http://127.0.0.1:8000/api/products/{id}/>
- Поиск товаров по названию: <http://127.0.0.1:8000/api/products/?search={query}>
- Сортировка товаров по цене: <http://127.0.0.1:8000/api/products/?ordering=price>
- Список из 5 самых дорогих товаров: <http://127.0.0.1:8000/api/top-expensive/>

### Доступные эндпоинты

- GET /api/products/ - Получить список всех товаров
- POST /api/products/ - Создать новый товар
- GET /api/products/{id}/ - Получить детальную информацию о товаре
- PUT /api/products/{id}/ - Обновить информацию о товаре
- PATCH /api/products/{id}/ - Частично обновить информацию о товаре
- DELETE /api/products/{id}/ - Удалить товар
- GET /api/products/?search={query} - Поиск товаров по названию
- GET /api/products/?ordering=price - Сортировка товаров по цене
- GET /api/top-expensive/ - Получить список из 5 самых дорогих товаров

## Дополнительная информация
#### Административная панель Django: <http://127.0.0.1:8000/admin/>
#### Документация Django REST Framework: <https://www.django-rest-framework.org/>