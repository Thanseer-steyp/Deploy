# api/v1/user/serializers.py
from rest_framework import serializers
from user.models import ClothProduct, JewelleryProduct


class ClothProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothProduct
        fields = ['id', 'name', 'price', 'image']


class JewelleryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = JewelleryProduct
        fields = ['id', 'name', 'price', 'image']
