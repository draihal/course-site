from django.contrib.auth import get_user_model
from django.core import mail
from django.test import TestCase
from django.test.utils import override_settings


class UsersManagersTests(TestCase):

    def setUp(self):
        self.user = get_user_model()
        self.default_user = self.user.objects.create(
            first_name='Name',
            phone_number='+79999999999',
            email='email@user.com',
            password='foo')
        self.admin_user = self.user.objects.create_superuser(
            first_name='TestingName',
            phone_number='+77999999999',
            email='super@user.com',
            password='foo')

    def test_create_user(self):
        self.assertEqual(self.default_user.email, 'email@user.com')
        self.assertTrue(self.default_user.is_active)
        self.assertFalse(self.default_user.is_staff)
        self.assertFalse(self.default_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(self.default_user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            self.user.objects.create_user()
        with self.assertRaises(TypeError):
            self.user.objects.create_user(email='')
        with self.assertRaises(ValueError):
            self.user.objects.create_user(
                first_name='Name',
                phone_number='+79999999999',
                email='', password="foo")

    def test_create_superuser(self):
        self.assertEqual(self.admin_user.email, 'super@user.com')
        self.assertTrue(self.admin_user.is_active)
        self.assertTrue(self.admin_user.is_staff)
        self.assertTrue(self.admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(self.admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            self.user.objects.create_superuser(
                first_name='TestingName',
                phone_number='+79999999999',
                email='', password='foo')


@override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
@override_settings(DEFAULT_FROM_EMAIL='from@example.com')
@override_settings(SERVER_EMAIL='from@example.com')
class CustomUserTest(TestCase):

    def setUp(self):
        self.user = get_user_model()
        self.customuser = self.user.objects.create(
            first_name='Name',
            phone_number='+79999999999',
            email='email@user.com',
            password='foo')

    def test_create_user(self):
        self.assertTrue(isinstance(self.customuser, self.user))

    def test_get_full_name(self):
        self.assertEqual(self.customuser.get_full_name(), f'{self.customuser.first_name} {self.customuser.last_name or ""}')

    def test_get_short_name(self):
        self.assertEqual(self.customuser.get_short_name(), self.customuser.first_name)

    def test___str__(self):
        self.assertEqual(self.customuser.__str__(), self.customuser.get_full_name())

    def test_send_mail_to_user(self):
        self.customuser.email_user(
                'Subject here',
                'Here is the message.',
                'from@example.com',
                fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')
        self.assertEqual(mail.outbox[0].body, 'Here is the message.')
        self.assertEqual(mail.outbox[0].from_email, 'from@example.com')
        self.assertEqual(mail.outbox[0].to, [self.customuser.email])
