# coding=utf-8
import factory
import faker
from django.core.files.uploadedfile import SimpleUploadedFile

from website.misc.factories import UserFactory
from .. import models

fake = faker.Faker()


class SharedFileFactory(factory.DjangoModelFactory):
    author = factory.SubFactory(UserFactory)
    email = factory.Faker('niepodam_email')
    secret = factory.Faker('text', max_nb_chars=20)
    file = factory.Sequence(
        lambda x: SimpleUploadedFile(
            '{}.txt'.format(x),
            'The {} file!'.format(x).encode('ascii')
        )
    )

    class Meta:
        model = models.SharedFile


class SharedUrlFactory(factory.DjangoModelFactory):
    author = factory.SubFactory(UserFactory)
    email = factory.Faker('niepodam_email')
    secret = factory.Faker('text', max_nb_chars=20)
    url = factory.Faker('uri')

    class Meta:
        model = models.SharedUrl


class UserAgentFactory(factory.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    agent = factory.Faker('user_agent')

    class Meta:
        model = models.UserAgent
