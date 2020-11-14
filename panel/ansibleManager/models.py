from django.db import models


class PlayBook(models.Model):
    title = models.CharField(max_length=120)
    inventory = models.CharField(max_length=120)
    tags = models.CharField(max_length=120)
    description = models.TextField()
