# coding=utf-8
# Copyright 2015 Brave Labs sp. z o.o.
# All rights reserved.
#
# This source code and all resulting intermediate files are CONFIDENTIAL and
# PROPRIETY TRADE SECRETS of Brave Labs sp. z o.o.
# Use is subject to license terms. See NOTICE file of this project for details.

import logging

import factory
import faker
from django.contrib.auth import get_user_model
from faker import providers

fake = faker.Faker()
log = logging.getLogger(__name__)


class TestEmailProvider(providers.BaseProvider):
    def niepodam_email(self):
        return '{}@niepodam.pl'.format(self.generator.user_name())


factory.Faker.add_provider(TestEmailProvider)


class UserFactory(factory.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('niepodam_email')
    username = factory.Sequence(lambda n: fake.user_name() + str(n))
    is_staff = False
    is_active = True

    class Meta:
        model = get_user_model()
