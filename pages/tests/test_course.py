import pytest

from django.test import TestCase

from ..models.course import Course
from .. import factories


@pytest.mark.django_db
class CourseTest(TestCase):

    def setUp(self):
        self.create_course = factories.CourseFactory()

    def test_course_creation(self):
        assert isinstance(self.create_course, Course)

    def test___str__(self):
        assert self.create_course.__str__() == self.create_course.name
