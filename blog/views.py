from django.http import HttpResponse
from django.views.generic.list import ListView

from .models import Post


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class PostListView(ListView):
    model = Post
    paginate_by = 10
