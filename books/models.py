from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.TextField(max_length=128)
    author = models.TextField(max_length=128,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Chapter(models.Model):
    book = models.ForeignKey(to=Book,on_delete=models.CASCADE)
    title = models.TextField(max_length=128)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
