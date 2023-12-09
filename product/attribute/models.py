from django.db import models
from utils.models import BaseModel


ATTRIBUTE_CHOICES = (
    ("text", "Text"),
    ("number", "Number"),
)


class Attribute(BaseModel):  # Дисплей
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=ATTRIBUTE_CHOICES)


class AttributeValue(BaseModel):  # Мавжуд
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)


class ProductAttribute(BaseModel):
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE)
    value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)
