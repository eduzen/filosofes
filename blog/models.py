from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.utils import timezone

from ckeditor_uploader.fields import RichTextUploadingField


class PublishedPost(models.QuerySet):
    def published(self):
        # -- only active records
        return self.filter(published_date__isnull=False)


class Post(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    headline = models.CharField(max_length=800, null=True, blank=True)
    content = RichTextUploadingField(null=True, blank=True)
    image = models.ImageField(upload_to="post-img/%Y/%m/%d", null=True, blank=True)
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateField(null=True, blank=True)
    slug = models.SlugField(max_length=50, blank=True, null=True)

    objects = PublishedPost.as_manager()

    def generate_slug(self):
        if self.slug:
            return

        slug = slugify(self.title[:49])
        if Post.objects.filter(slug=slug).exists():
            self.slug = f"{self.pk}-{slug}"
        self.save()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def published(self):
        return True if self.published_date else False

    def __str__(self):
        return f"Post: {self.title}"


def post_post_save(sender, instance, created, **kwargs):
    instance.generate_slug()


signals.post_save.connect(post_post_save, Post)
