import factory
import factory.fuzzy
from faker import Faker

from users.factories import StudentFactory
from . import models


fake = Faker(locale='ru_RU')  # TODO: need to add other locale?


class AboutUsPageFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.AboutUsPage
        django_get_or_create = ('title', )

    title = factory.lazy_attribute(lambda o: fake.sentence(
        nb_words=2, variable_nb_words=True, ext_word_list=None))
    short_description = factory.lazy_attribute(lambda o: fake.sentence(
        nb_words=6, variable_nb_words=True, ext_word_list=None))
    short_about_us = factory.lazy_attribute(lambda o: fake.sentence(
        nb_words=10, variable_nb_words=True, ext_word_list=None))


class ContactsPageFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.ContactsPage
        django_get_or_create = ('title', )

    title = factory.lazy_attribute(lambda o: fake.sentence(
        nb_words=2, variable_nb_words=True, ext_word_list=None))
    vk = factory.lazy_attribute(lambda o: fake.url())
    fb = factory.lazy_attribute(lambda o: fake.url())
    ok = factory.lazy_attribute(lambda o: fake.url())
    youtube = factory.lazy_attribute(lambda o: fake.url())
    telegram = factory.lazy_attribute(lambda o: fake.url())
    address = factory.lazy_attribute(lambda o: fake.address())
    details = factory.lazy_attribute(lambda o: fake.sentence(
        nb_words=8, variable_nb_words=True, ext_word_list=None))
    phone_number = factory.lazy_attribute(lambda o: fake.phone_number())


class CourseCategoryFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.CourseCategory

    name = factory.lazy_attribute(lambda o: fake.sentence(
        nb_words=2, variable_nb_words=True, ext_word_list=None))
    slug = factory.lazy_attribute(lambda o: fake.user_name())


class CourseFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Course

    name = factory.lazy_attribute(lambda o: fake.sentence(
        nb_words=2, variable_nb_words=True, ext_word_list=None))
    slug = factory.lazy_attribute(lambda o: fake.user_name())
    category = factory.SubFactory(CourseCategoryFactory)
    description = factory.lazy_attribute(lambda o: fake.sentence(
        nb_words=15, variable_nb_words=True, ext_word_list=None))
    necessary_knowledge = factory.lazy_attribute(lambda o: fake.sentence(
        nb_words=15, variable_nb_words=True, ext_word_list=None))
    study_process = factory.lazy_attribute(lambda o: fake.sentence(
        nb_words=15, variable_nb_words=True, ext_word_list=None))
    graduation_project = factory.lazy_attribute(lambda o: fake.sentence(
        nb_words=15, variable_nb_words=True, ext_word_list=None))
    after_training = factory.lazy_attribute(lambda o: fake.sentence(
        nb_words=15, variable_nb_words=True, ext_word_list=None))


class ReviewFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Review

    student = factory.SubFactory(StudentFactory)
    course = factory.SubFactory(CourseFactory)
    text = factory.lazy_attribute(lambda o: fake.sentence(
        nb_words=12, variable_nb_words=True, ext_word_list=None))


class MassMediaPublicationFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.MassMediaPublication

    name = factory.lazy_attribute(lambda o: fake.sentence(
        nb_words=2, variable_nb_words=True, ext_word_list=None))
    slug = factory.lazy_attribute(lambda o: fake.user_name())
    publication_url = factory.lazy_attribute(lambda o: fake.url())
    mass_media_name = factory.lazy_attribute(lambda o: fake.sentence(
        nb_words=3, variable_nb_words=True, ext_word_list=None))
    date_of_publish = factory.lazy_attribute(lambda o: fake.date())


class SiteConfigurationFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.SiteConfiguration
        django_get_or_create = ('title', )

    title = factory.lazy_attribute(lambda o: fake.sentence(
        nb_words=2, variable_nb_words=True, ext_word_list=None))
    short_description = factory.lazy_attribute(lambda o: fake.sentence(
        nb_words=2, variable_nb_words=True, ext_word_list=None))
