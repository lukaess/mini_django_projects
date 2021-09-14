from django.contrib.admin.sites import DefaultAdminSite
from django.db import models

# Create your models here.
class  Feature(models.Model):
    name = models.CharField(max_length=100, default="")
    details = models.CharField(max_length=500, default="")