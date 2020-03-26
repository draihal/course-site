import pytest

from django.test import TestCase

from .. import factories


@pytest.mark.django_db
class SiteConfigurationTest(TestCase):

    def setUp(self):
        self.site_configuration = factories.SiteConfigurationFactory()

    def test__str__(self):
        assert self.site_configuration.__str__() == self.site_configuration.short_description
