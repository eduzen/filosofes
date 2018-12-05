import pytest

from blog.tests.factories import PostFactory

from django.shortcuts import reverse


@pytest.mark.django_db
def test_post_ok(client):
    response = client.get(reverse('post-list'))

    assert response.status_code == 200
    assert response.context_data['view'].__class__.__name__ == 'PostListView'


@pytest.mark.django_db
def test_post_detail_ok(client):
    post = PostFactory.create()
    response = client.get(f'/post/{post.slug}')

    assert response.status_code == 301
