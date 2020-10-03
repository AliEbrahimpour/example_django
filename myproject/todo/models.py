from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    date = models.DateTimeField()
