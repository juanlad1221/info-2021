from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.category


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    created = models.DateTimeField()
    active = models.BooleanField(default=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
