from django.db import models
from django.conf import settings


class BaseModel(models.Model):
    """
    Abstract model class that provides self-updating
    'created' and 'modified' fields.
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @property
    def image_url(self):
        return settings.HOST + self.image
