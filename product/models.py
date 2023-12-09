from django.db import models
from utils.models import BaseModel
from django.template.defaultfilters import slugify
from product.managers import ProductManager


class Category(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    parent = models.ForeignKey("self", related_name="children", on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Brand(BaseModel):
    title = models.CharField(max_length=255)


class Product(BaseModel):
    title = models.CharField(max_length=255)

    price = models.PositiveIntegerField(default=0)
    price_discount = models.PositiveIntegerField(default=0)

    count = models.PositiveBigIntegerField(default=0)

    _image = models.ImageField(upload_to="product_images", null=True, blank=True, editable=False)

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    description = models.TextField(null=True, blank=True)

    rating = models.DecimalField(default=0, max_digits=2, decimal_places=1)

    is_active = models.BooleanField(default=True)

    objects = ProductManager()

    @property
    def image(self):
        return self._image.url if self._image else None

    @property
    def is_available(self):
        return self.count > 0 and self.is_active


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_images")
    is_main = models.BooleanField(default=False)
