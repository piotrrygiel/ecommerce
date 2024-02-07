from rest_framework import serializers
from .models import Category, Product, Size


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = (
            "size",
            "quantity",
        )


class ProductSerializer(serializers.ModelSerializer):
    sizes = SizeSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail",
            "get_category_name",
            "sizes",
        )


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )
