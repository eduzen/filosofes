import pytest

from django.contrib.auth.models import User
from hypothesis.extra.django.models import models

from blog.models import Post


@pytest.mark.django_db
def test_post_creation():
    post = models(Post, author=models(User)).example()
    assert post
