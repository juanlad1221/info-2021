from django.db import models
from django.db.models.fields import EmailField
import post
from post.models import Post
from django.utils import timezone

# Create your models here.
class Comments(models.Model):
    comment = models.CharField(max_length=500)
    email = models.EmailField(max_length=200)
    created = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment