import pytest

from django.test import TestCase

from ..models.course_category import CourseCategory
from .. import factories


@pytest.mark.django_db
class CourseCategoryTest(TestCase):
    def setUp(self):
        self.course_category = factories.CourseCategoryFactory()

    def test_course_category_creation(self):
        assert isinstance(self.course_category, CourseCategory)

    def test___str__(self):
        assert self.course_category.__str__() == self.course_category.name
