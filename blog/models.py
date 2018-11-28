from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    author_name = models.CharField(max_length=100)
    date_written = models.DateField(auto_now=True)
