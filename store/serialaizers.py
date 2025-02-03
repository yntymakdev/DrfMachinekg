from rest_framework import serializers
from .models import Category, ProductPhotos

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# class ProductPhotosSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductPhotos
#         fields = '__all__'
