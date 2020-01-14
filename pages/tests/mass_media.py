from django.test import TestCase
from django.utils import timezone

from ..models.mass_media import MassMediaPublication


class MassMediaPublicationTest(TestCase):

    @staticmethod
    def create_mass_media():
        return MassMediaPublication.objects.create(
            name='only a test',
            slug='uniqslugformassmedia',
            publication_url='https://realpython.com/',
            mass_media_name='only a test',
            date_of_publish=timezone.now()
        )

    def setUp(self):
        self.mass_media = self.create_mass_media()

    def test_mass_media_creation(self):
        self.assertTrue(isinstance(self.mass_media, MassMediaPublication))

    def test___str__(self):
        self.assertEqual(self.mass_media.__str__(), self.mass_media.name)
