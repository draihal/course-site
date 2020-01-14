from django.test import TestCase

from ..models.course import Course
from ..models.course_category import CourseCategory


class CourseTest(TestCase):

    @staticmethod
    def create_course():
        return Course.objects.create(
            name='only a test',
            slug='uniqslugforcoursey',
            category=CourseCategory.objects.first(),
            description='only a test',
            necessary_knowledge='only a test',
            study_process='only a test',
            graduation_project='only a test',
            after_training='only a test',
            )

    @staticmethod
    def create_course_category():
        return CourseCategory.objects.create(
            name='only a test',
            slug='uniqslugforcoursecategory',
        )

    def setUp(self):
        self.course_category = self.create_course_category()
        self.create_course = self.create_course()

    def test_course_creation(self):
        self.assertTrue(isinstance(self.create_course, Course))

    def test___str__(self):
        self.assertEqual(self.create_course.__str__(), self.create_course.name)
