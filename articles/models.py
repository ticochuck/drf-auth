from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f'{self.title}, by {self.author}'