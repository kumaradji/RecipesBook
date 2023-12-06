# myrecipes/serializers.py

from rest_framework import serializers
from .models import Category, Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Recipe.

    Поля:
    - title (CharField): Название рецепта.
    - content (TextField): Описание рецепта.
    - category (PrimaryKeyRelatedField): Категория, к которой относится рецепт.

    Примечание: Сериализатор автоматически включает все поля модели Recipe.
    """

    class Meta:
        model = Recipe
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Category.

    Поля:
    - name (CharField): Название категории.
    - recipes (RecipeSerializer, many=True, read_only=True): Список рецептов в категории.

    Примечание: Сериализатор автоматически включает все поля модели Category.
    """

    recipes = RecipeSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
