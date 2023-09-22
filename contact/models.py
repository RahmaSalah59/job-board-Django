from django.db import models

# Create your models here.
class info(models.Model):
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
