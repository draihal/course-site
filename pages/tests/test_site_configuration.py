from django.test import TestCase

from ..models.site_configuration import SiteConfiguration


class SiteConfigurationTest(TestCase):

    # first() because SiteConfiguration django singleton
    def test__str__(self):
        siteconf = SiteConfiguration.objects.first()
        self.assertEqual(SiteConfiguration.objects.first().__str__(), siteconf.short_description)
