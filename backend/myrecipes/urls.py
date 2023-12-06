# myrecipes/urls.py

from django.urls import path
from .views import CategoryList, RecipeDetail, RecipesList, RecipesByCategoryList, YourCategoryDetailView

urlpatterns = [
    path('', CategoryList.as_view(), name='home'),
    path('api/recipes/', RecipesList.as_view(), name='recipe-list'),
    path('api/categories/<int:pk>/', YourCategoryDetailView.as_view(), name='category-detail'),
    path('api/recipes/category/<int:categoryId>/', RecipesByCategoryList.as_view(), name='recipes-by-category'),
    path('api/recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
    path('api/categories/', CategoryList.as_view(), name='category-list'),
]
