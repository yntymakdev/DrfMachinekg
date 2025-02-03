from rest_framework import serializers
from .models import Category, ProductPhotos, Comment, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhotos
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):  # Исправлено здесь
    class Meta:
        model = Comment
        fields = '__all__'
