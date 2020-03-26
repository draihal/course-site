# import factory
import factory.fuzzy
from faker import Faker

from django.conf import settings

from . import models


fake = Faker(locale='ru_RU')  # TODO: need to add other locale?

COUNTRY_CHOICES = ('NA', 'RU', 'BY', 'KZ', 'UA')
SEX_CHOICES = ('0', 'm', 'f')


class CustomUserFactory(factory.DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL
        # django_get_or_create = ('email',)

    first_name = factory.lazy_attribute(lambda o: fake.first_name())
    last_name = factory.lazy_attribute(lambda o: fake.last_name())
    email = factory.lazy_attribute(lambda o: fake.safe_email())
    phone_number = factory.lazy_attribute(lambda o: fake.phone_number())
    is_student = factory.lazy_attribute(lambda o: fake.pybool())
    is_teacher = factory.lazy_attribute(lambda o: fake.pybool())
    is_partner = factory.lazy_attribute(lambda o: fake.pybool())


class StudentFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Student

    user = factory.SubFactory(CustomUserFactory)
    can_relocate = factory.lazy_attribute(lambda o: fake.pybool())
    can_full_time = factory.lazy_attribute(lambda o: fake.pybool())
    can_part_time = factory.lazy_attribute(lambda o: fake.pybool())
    can_remote = factory.lazy_attribute(lambda o: fake.pybool())
    birth_date = factory.lazy_attribute(lambda o: fake.date_between(start_date='-30y', end_date='today'))
    country = factory.fuzzy.FuzzyChoice(COUNTRY_CHOICES)
    city = factory.lazy_attribute(lambda o: fake.city_name())
    sex = factory.fuzzy.FuzzyChoice(SEX_CHOICES)


class TeacherFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Teacher

    user = factory.SubFactory(CustomUserFactory)
    birth_date = factory.lazy_attribute(lambda o: fake.date_between(start_date='-30y', end_date='today'))
    country = factory.fuzzy.FuzzyChoice(COUNTRY_CHOICES)
    city = factory.lazy_attribute(lambda o: fake.city_name())
    sex = factory.fuzzy.FuzzyChoice(SEX_CHOICES)


class PartnerFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Partner

    user = factory.SubFactory(CustomUserFactory)
    company = factory.lazy_attribute(lambda o: fake.company())
