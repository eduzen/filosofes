import pytest

from django.shortcuts import reverse
from django.contrib.auth.models import User

from hypothesis import given
from hypothesis.extra.django.models import models

from blog.models import Post

HTTP_200_OK = 200


@pytest.mark.django_db
def test_post_ok(client):
    response = client.get(reverse('post-list'))

    assert response.status_code == HTTP_200_OK
    assert response.context_data['view'].__class__.__name__ == 'PostListView'


@given(post=models(Post, author=models(User)))
@pytest.mark.django_db
def test_post_detail_ok(client, post):
    url = reverse('post-detail', kwargs={"slug": post.slug})
    response = client.get(url)

    assert response.status_code == HTTP_200_OK
