from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

