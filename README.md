# Fullstack приложение Recipe
## Проект "Рецепты"
Это веб-приложение с полным стеком для управления рецептами. Оно включает в себя бэкэнд на Django для обработки хранения и извлечения данных, а также фронтэнд на React для предоставления удобного пользовательского интерфейса.

### Функциональность
1. Категории: Управление различными категориями для рецептов.
2. Рецепты: Создание, чтение, обновление и удаление рецептов внутри категорий. 
3. Документация Swagger: Изучение и понимание конечных точек API с использованием документации Swagger.

### Отзывчивый дизайн: 
Фронтэнд разработан с учетом отзывчивого дизайна для лучшего пользовательского опыта на различных устройствах.
Используемые технологии
### Бэкэнд (Django)
Django REST Framework
Django ORM для операций с базой данных
Django Rest Swagger для документации API
### Фронтэнд (React)
React для создания пользовательских интерфейсов
React Router для обработки навигации
Axios для выполнения запросов API
Swagger UI React для визуализации документации Swagger
## Инструкции по установке
### Бэкэнд (Django)
1. Перейдите в каталог backend. 
2. Установите зависимости: pip install -r requirements.txt. 
3. Установите модуль: pip install drf-yasg
4. Выполните миграции: python manage.py migrate.
4. Запустите сервер разработки: python manage.py runserver.
### Фронтэнд (React)
1. Перейдите в каталог frontend.
2. Установите зависимости: npm install.
3. Запустите сервер разработки: npm start.

Конечные точки API
Категории: /api/categories/

GET: Получить список категорий.
POST: Создать новую категорию.
Детали категории: /api/categories/<int:pk>/

GET: Получить подробную информацию о конкретной категории.
Рецепты: /api/recipes/

GET: Получить список всех рецептов.
POST: Создать новый рецепт.
Детали рецепта: /api/recipes/<int:pk>/

GET: Получить подробную информацию о конкретном рецепте.
Рецепты по категории: /api/recipes/category/<int:categoryId>/

GET: Получить список рецептов для конкретной категории.
Документация Swagger
Чтобы изучить документацию API, посетите страницу документации Swagger:

## Swagger UI: http://localhost:8000/swagger/
### Использование
1. Запустите серверы как для бэкэнда Django, так и для фронтэнда React.
2. Откройте приложение в веб-браузере.
3. Переходите по категориям, просматривайте рецепты и управляйте своими кулинарными идеями.

Внесение вклада
Если вы хотите внести вклад в этот проект, следуйте этим шагам:

Сделайте форк репозитория.
Создайте новую ветку для вашей функции или исправления ошибок.
Реализуйте ваши изменения.
Тщательно протестируйте.
Предоставьте запрос на включение изменений.

## Лицензия
Этот проект лицензирован в соответствии с лицензией MIT.

