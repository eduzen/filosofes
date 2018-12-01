from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from . import models


class BookListView(ListView):
    model = models.Book
    paginate_by = 10


class BookDetailView(DetailView):
    model = models.Book


class AuthorListView(ListView):
    model = models.Author
    paginate_by = 10


class AuthorDetailView(DetailView):
    model = models.Author
