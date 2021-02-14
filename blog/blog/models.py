from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=256, default="No Title")
    text = models.TextField()
    is_public = models.BooleanField(default=True)


class Comment(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
