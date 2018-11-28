from django.db import models
from django.utils import timezone

from ckeditor_uploader.fields import RichTextUploadingField


class PublishedPost(models.QuerySet):
    def published(self):
        # -- only active records
        return self.filter(published_date__isnull=False)


class Post(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    headline = models.CharField(max_length=800, null=True)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to="post-img/%Y/%m/%d", null=True)
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateField(null=True)

    objects = PublishedPost.as_manager()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def published(self):
        return True if self.published_date else False

    def __str__(self):
        return f"Post: {self.title}"
