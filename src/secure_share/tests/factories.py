# coding=utf-8
import factory
import faker

from website.misc.factories import UserFactory
from . import models

fake = faker.Faker()


class SharedFileFactory(factory.DjangoModelFactory):
    email = factory.Faker('email')
    secret = factory.Faker('catch_phrase')

    class Meta:
        model = models.SharedFile

class SharedUrlFactory(factory.DjangoModelFactory):
    email = factory.Faker('email')
    secret = factory.Faker('catch_phrase')
    url = factory.Faker('uri')

    class Meta:
        model = models.SharedUrl
