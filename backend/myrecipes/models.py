# myrecipes/models.py

from django.db import models

class Category(models.Model):
    """
    Модель Django для категорий блюд.

    Атрибуты:
    - name (CharField): Название категории.
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Recipe(models.Model):
    """
    Модель Django для рецептов блюд.

    Атрибуты:
    - title (CharField): Название рецепта.
    - content (TextField): Описание рецепта.
    - category (ForeignKey): Внешний ключ, связывающий рецепт с категорией.

    Методы:
    - __str__: Возвращает строковое представление рецепта.
    """

    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'
