from django.urls import path
from product.views import ProductCategoryListAPIView

urlpatterns = [
    path("<str:category_slug>/", ProductCategoryListAPIView.as_view(), name="product-category-list"),
]
