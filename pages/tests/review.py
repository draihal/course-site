from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model

from ..models.course import Course
from ..models.course_category import CourseCategory
from ..models.review import Review
from users.models.student import Student


class ReviewTest(TestCase):

    @staticmethod
    def create_course_category():
        return CourseCategory.objects.create(
            name='only a test',
            slug='uniqslugforcoursecategory',
        )

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
    def create_review():
        return Review.objects.create(
            student=Student.objects.first(),
            course=Course.objects.first(),
            text='only a test',
        )

    def setUp(self):
        self.user = get_user_model()
        self.customuser = self.user.objects.create(
            first_name='Name',
            phone_number='+79999999999',
            email='email@user.com',
            password='foo')
        self.student = Student.objects.create(
            user=self.user.objects.first(),
            can_relocate=True,
            can_full_time=True,
            can_part_time=True,
            can_remote=True,
            birth_date=timezone.now(),
            country='NA',
            city='only a test',
            sex=0
        )

        self.course_category = self.create_course_category()
        self.create_course = self.create_course()
        self.review = self.create_review()

    def test_review_creation(self):
        self.assertTrue(isinstance(self.review, Review))

    def test___str__(self):
        self.assertEqual(self.review.__str__(), f'{self.review.course} {self.review.student}')
