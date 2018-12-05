import factory

from django.contrib.auth.models import User

from blog import models


class UserFactory(factory.Factory):
    class Meta:
        model = User

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.Faker("user_name")


class PostFactory(factory.Factory):
    class Meta:
        model = models.Post

    author = factory.SubFactory(UserFactory)
    title = factory.Faker('sentence', nb_words=4)
    content = factory.Faker("text")
    slug = "some-slug"
