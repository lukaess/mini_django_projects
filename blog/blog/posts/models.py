from django.db import models
from datetime import datetime
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(max_length = 1000000)
    date_of_creation = models.DateTimeField(default=datetime.now, blank=True)
