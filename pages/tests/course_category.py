from django.test import TestCase

from ..models.course_category import CourseCategory


class CourseCategoryTest(TestCase):

    @staticmethod
    def create_course_category():
        return CourseCategory.objects.create(
            name='only a test',
            slug='uniqslugforcoursecategory',
        )

    def setUp(self):
        self.course_category = self.create_course_category()

    def test_course_category_creation(self):
        self.assertTrue(isinstance(self.course_category, CourseCategory))

    def test___str__(self):
        self.assertEqual(self.course_category.__str__(), self.course_category.name)
