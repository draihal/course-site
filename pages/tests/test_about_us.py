import pytest

from django.test import TestCase

from .. import factories


@pytest.mark.django_db
class AboutUsPageTest(TestCase):
    def setUp(self):
        self.about_us_page = factories.AboutUsPageFactory()

    def test__str__(self):
        assert self.about_us_page.__str__() == 'Страница о нас'
