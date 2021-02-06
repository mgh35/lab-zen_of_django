from django.db import models

class Post(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, blank=True)
    title = models.CharField(max_length=256, default="No Title")
    text = models.TextField()
