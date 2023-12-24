from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Модель Django для категорий товаров.

    Атрибуты:
    - name (CharField): Название категории.

    Методы:
    - __str__: Возвращает строковое представление категории.
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class EcoStaff(models.Model):
    """
    Модель Django для платков, палантинов и пр.

    Атрибуты:
    - title (CharField): Название.
    - content (TextField): Описание.
    - category (ForeignKey): Внешний ключ, связывающий продукт с категорией.
    - images (ManyToManyField): Внешний ключ, связывающий продукт с категорией изображений.
    - videos (ManyToManyField): Внешний ключ, связывающий продукт с категорией видео-файлов.

    Методы:
    - __str__: Возвращает строковое представление продукта.
    """

    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    images = models.ManyToManyField('EcoImage')
    videos = models.ManyToManyField('EcoVideo')

    def __str__(self):
        return f'{self.title}'


class MasterClass(models.Model):
    """
    Модель Django для мастер-классов прочих видео-уроков.

    Атрибуты:
    - title (CharField): Название.
    - content (TextField): Описание.
    - category (ForeignKey): Внешний ключ, связывающий продукт с категорией.
    - media (ManyToManyField): Внешний ключ, связывающий продукт с медиа-файлами.

    Методы:
    - __str__: Возвращает строковое представление продукта.
    """

    title = models.CharField(max_length=255)
    content = models.TextField()
    media = models.ManyToManyField('MasterMedia')

    def __str__(self):
        return f'{self.title}'


class Cart(models.Model):
    """
    Модель Django для корзины покупок.

    Атрибуты:
    - user (ForeignKey): Внешний ключ, связывающий корзину с пользователем.
    - items (ManyToManyField): Внешний ключ, связывающий корзину с товарами (EcoStaff).
    - total_cost (DecimalField): Общая стоимость товаров в корзине.

    Методы:
    - None
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(EcoStaff)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class Order(models.Model):
    """
    Модель Django для заказов.

    Атрибуты:
    - user (ForeignKey): Внешний ключ, связывающий заказ с пользователем.
    - master_classes (ManyToManyField): Внешний ключ, связывающий заказ с мастер-классами (MasterClass).
    - items (ManyToManyField): Внешний ключ, связывающий заказ с товарами (EcoStaff).
    - total_cost (DecimalField): Общая стоимость товаров в заказе.
    - address (CharField): Адрес доставки заказа.
    - status (CharField): Статус заказа, выбирается из предопределенных вариантов.

    Методы:
    - None
    """

    CART_STATUS_CHOICES = (
        ('P', 'Pending'),  # just added to cart
        ('C', 'Confirmed'),  # confirmed order
        ('S', 'Shipped'),
        ('D', 'Delivered')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    master_classes = models.ManyToManyField('MasterClass')
    items = models.ManyToManyField(EcoStaff)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=1, choices=CART_STATUS_CHOICES)


class MasterMedia(models.Model):
    """
    Модель Django для медиа-файлов мастер-классов.

    Атрибуты:
    - image (ImageField): Изображение медиа-файла.
    - video (FileField): Видео-файл медиа-файла.

    Методы:
    - None
    """

    image = models.ImageField(upload_to='masterclasses')
    video = models.FileField(upload_to='masterclasses')


class EcoImage(models.Model):
    """
    Модель Django для изображений товаров (EcoStaff).

    Атрибуты:
    - image (ImageField): Изображение товара.

    Методы:
    - None
    """

    image = models.ImageField(upload_to='products')


class EcoVideo(models.Model):
    """
    Модель Django для видео-файлов товаров (EcoStaff).

    Атрибуты:
    - video (FileField): Видео-файл товара.

    Методы:
    - None
    """

    video = models.FileField(upload_to='products')

