from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from product.models import Product, Brand, Category, ProductImage


class ProductTests(APITestCase):
    def setUp(self):
        brand = Brand.objects.create(title="BrandName")
        category = Category.objects.create(
            title="CategoryName",
        )
        product = Product.objects.create(
            title="Product Name", price=1000, price_discount=900, count=10, category=category, brand=brand
        )
        product_image = ProductImage.objects.create(image="product_image.jpg", product=product, is_main=True)
        self.category = category
        self.brand = brand
        self.product = product
        self.product_image = product_image

    def test_active_product(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse("product-category-list", kwargs={"category_slug": self.category.slug})

        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()

        self.assertTrue(
            any([True for obj in data if obj["id"] == self.product.id]),
        )

    def test_count(self):
        """
        Ensure we can create a new account object.
        """
        self.product.count = 0
        self.product.save()

        url = reverse("product-category-list", kwargs={"category_slug": self.category.slug})

        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()

        self.assertFalse(
            any([True for obj in data if obj["id"] == self.product.id]),
        )
        self.product.count = 10
        self.product.save()

    def test_active(self):
        """
        Ensure we can create a new account object.
        """
        self.product.is_active = False
        self.product.save()

        url = reverse("product-category-list", kwargs={"category_slug": self.category.slug})

        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()

        self.assertFalse(
            any([True for obj in data if obj["id"] == self.product.id]),
        )

        self.product.is_active = True
        self.product.save()

    def test_image(self):
        """
        Ensure we can create a new account object.
        """

        url = reverse("product-category-list", kwargs={"category_slug": self.category.slug})

        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        print(self.product_image.image.url)
        self.assertTrue(
            any([True for obj in data if obj["image"] == self.product_image.image.url]),
        )
