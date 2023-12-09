from django.db.models.signals import post_save
from django.dispatch import receiver
from product.models import ProductImage


@receiver(post_save, sender=ProductImage)
def save_image_to_product(sender, instance, **kwargs):
    if instance.is_main:
        instance.product._image = instance.image
        instance.product.save()
