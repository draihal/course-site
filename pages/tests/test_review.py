import pytest

from django.test import TestCase

from ..models.review import Review
from .. import factories


@pytest.mark.django_db
class ReviewTest(TestCase):
    def setUp(self):
        self.review = factories.ReviewFactory()

    def test_review_creation(self):
        assert isinstance(self.review, Review)

    def test___str__(self):
        assert self.review.__str__() == f'{self.review.course} {self.review.student}'
