from django.db import models

# Create your models here.
from django.db import models


class Celebrity(models.Model):
    prefix = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
