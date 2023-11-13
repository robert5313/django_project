from django.db import models

# Create your models here.
class Tutorial(models.Model):
    name = models.CharField(max_length=50)
    detail = models.CharField(max_length=225)
    created_at = models.DateTimeField()
