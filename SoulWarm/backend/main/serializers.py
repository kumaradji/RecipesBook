from django.contrib.auth.models import User
from rest_framework import serializers

from backend.main.models import Category, EcoStaff, MasterMedia, MasterClass, Order, Cart


class MasterMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterMedia
        fields = ('id', 'image', 'video')


class MasterClassSerializer(serializers.ModelSerializer):
    media = MasterMediaSerializer(many=True, read_only=True)

    class Meta:
        model = MasterClass
        fields = ('id', 'title', 'content', 'media')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class EcoStaffSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = EcoStaff
        fields = ('id', 'title', 'content', 'price', 'category')


class CartSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    items = EcoStaffSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'user', 'items', 'total_cost')


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    items = EcoStaffSerializer(many=True, read_only=True)
    master_classes = MasterClassSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'items', 'total_cost', 'address', 'status', 'master_classes')
