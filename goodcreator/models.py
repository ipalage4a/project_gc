import uuid
from django.db import models
from django.db.models.fields import UUIDField

# Create your models here.

class ModelMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_archive = models.BooleanField("заархивировано", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.title if self.title is not None else super().__str__()
    

class Category(ModelMixin):
    title = models.CharField("Название", max_length=512, blank=True, null=True)

class Entry(ModelMixin):
    title = models.CharField("Название", max_length=256, blank=True, null=True)
    body = models.CharField("Текст", max_length=1000)
    category = models.ForeignKey(
        Category,
        verbose_name="категория",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="articles",
        )
    