import uuid
from django.db import models
from django.db.models.fields import UUIDField

# Create your models here.

class Entry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.CharField("Текст", max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)
