# myrecipes/views.py

from rest_framework import generics
from .models import Category, Recipe
from .serializers import CategorySerializer, RecipeSerializer


class CategoryList(generics.ListCreateAPIView):
    """
    View for listing and creating categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RecipeDetail(generics.RetrieveAPIView):
    """
    View for retrieving details of a specific recipe.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipesList(generics.ListAPIView):
    """
    View for listing all recipes.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class YourCategoryDetailView(generics.RetrieveAPIView):
    """
    View for retrieving details of a specific category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RecipesByCategoryList(generics.ListAPIView):
    """
    View for listing recipes by a specific category.
    """
    serializer_class = RecipeSerializer

    def get_queryset(self):
        """
        Retrieve the list of recipes based on the provided category ID.
        """
        category_id = self.kwargs['categoryId']
        return Recipe.objects.filter(category=category_id)
