from django.contrib import admin

from .models import Book, Author, BookFile


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookFile)
