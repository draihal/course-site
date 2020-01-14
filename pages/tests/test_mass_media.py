import pytest

from django.test import TestCase

from ..models.mass_media import MassMediaPublication
from .. import factories


@pytest.mark.django_db
class MassMediaPublicationTest(TestCase):

    def setUp(self):
        self.mass_media = factories.MassMediaPublicationFactory()

    def test_mass_media_creation(self):
        assert isinstance(self.mass_media, MassMediaPublication)

    def test___str__(self):
        assert self.mass_media.__str__() == self.mass_media.name
