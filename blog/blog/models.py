from django.db import models

class Post(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, blank=True)
    text = models.TextField()
