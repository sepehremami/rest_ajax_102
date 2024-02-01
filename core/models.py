
from django.db import models


class BaseModel(models.Model):
    """
    Common attributes of all models
    All models extend BaseModel
    """

    is_deleted = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()