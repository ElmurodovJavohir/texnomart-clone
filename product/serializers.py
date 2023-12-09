from rest_framework import serializers
from product.models import Product


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "description",
            "price",
            "price_discount",
            "category",
            "image",
            "rating",
            "is_available",
        )
