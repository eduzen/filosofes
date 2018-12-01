from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

from ckeditor_uploader.fields import RichTextUploadingField


class Book(models.Model):
    """Model representing a book"""

    title = models.CharField(max_length=200)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True, blank=True)
    summary = RichTextUploadingField(null=True, blank=True, help_text="Enter a brief description of the book")
    isbn = models.CharField(
        "ISBN",
        null=True,
        blank=True,
        max_length=13,
        help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>',
    )
    cover = models.ImageField(upload_to="covers", default="covers/no_cover.jpg")
    # genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    slug = models.SlugField(max_length=70, blank=True, null=True)
    published_data = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title[:49])
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse("book-detail", args=[str(self.id)])


class Author(models.Model):
    """Model representing an author."""

    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField("Died", null=True, blank=True)
    slug = models.SlugField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name} {self.last_name}")
        super(Author, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse("author-detail", args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.last_name}, {self.first_name}"
