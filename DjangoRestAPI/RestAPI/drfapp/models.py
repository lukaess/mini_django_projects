from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    descrtiption = models.TextField()
    date_enroled = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name