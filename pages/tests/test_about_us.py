from django.test import TestCase

from ..models.about_us import AboutUsPage


class AboutUsPageTest(TestCase):

    # first() because AboutUsPage django singleton
    def test__str__(self):
        self.assertEqual(AboutUsPage.objects.first().__str__(), 'Страница о нас')
