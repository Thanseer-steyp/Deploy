from rest_framework import serializers
from django.contrib.auth.models import User
from user.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'image']
