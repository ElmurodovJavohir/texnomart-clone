from django.shortcuts import render
from rest_framework import generics
from product.models import Product
from product.serializers import ProductCategorySerializer


# Create your views here.
class ProductCategoryListAPIView(generics.ListAPIView):
    queryset = Product.objects.active()
    serializer_class = ProductCategorySerializer

    def filter_queryset(self, queryset):
        queryset = super(ProductCategoryListAPIView, self).filter_queryset(queryset)
        return queryset.filter(category__slug=self.kwargs["category_slug"])
