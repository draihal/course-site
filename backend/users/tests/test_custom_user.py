import pytest

from django.contrib.auth import get_user_model
from django.core import mail
from django.test import TestCase

from .. import factories


@pytest.mark.django_db
class UsersManagersTests(TestCase):

    def setUp(self):
        self.user = get_user_model()
        self.admin_user = self.user.objects.create_superuser(
            first_name='TestingName',
            phone_number='+77999999999',
            email='super@user.com',
            password='foo')
        self.default_user = factories.CustomUserFactory.create(email='email@user.com')
        # TODO: factory boy add createsuperuserfactory
        # self.admin_user = factories.CustomUserFactory.create_superuser(email='super@user.com')

    def test_create_user(self):
        assert self.default_user.email == 'email@user.com'
        assert self.default_user.is_active
        assert self.default_user.is_staff == False
        assert self.default_user.is_superuser == False
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            assert None == self.default_user.username
        except AttributeError:
            pass
        with pytest.raises(TypeError):
            self.user.objects.create_user()
        with pytest.raises(TypeError):
            self.user.objects.create_user(email='')
        with pytest.raises(ValueError):
            self.user.objects.create_user(
                first_name='Name',
                phone_number='+79999999999',
                email='', password="foo")

    def test_create_superuser(self):
        assert self.admin_user.email == 'super@user.com'
        assert self.admin_user.is_active
        assert self.admin_user.is_staff
        assert self.admin_user.is_superuser
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            assert self.admin_user.username is None
        except AttributeError:
            pass
        with pytest.raises(ValueError):
            self.user.objects.create_superuser(
                first_name='TestingName',
                phone_number='+79999999999',
                email='', password='foo')


@pytest.mark.django_db
class CustomUserTest(TestCase):

    def setUp(self):
        self.user = get_user_model()
        self.customuser = factories.CustomUserFactory.create(email='email@user.com')

    def test_create_user(self):
        assert isinstance(self.customuser, self.user) == True

    def test_get_full_name(self):
        assert self.customuser.get_full_name() == f'{self.customuser.first_name} {self.customuser.last_name or ""}'

    def test_get_short_name(self):
        assert self.customuser.get_short_name() == self.customuser.first_name

    def test___str__(self):
        assert self.customuser.__str__() == self.customuser.get_full_name()

    def test_send_mail_to_user(self):
        self.customuser.email_user(
                'Subject here',
                'Here is the message.',
                'from@example.com',
                fail_silently=False)
        assert len(mail.outbox) == 1
        assert mail.outbox[0].subject == 'Subject here'
        assert mail.outbox[0].body == 'Here is the message.'
        assert mail.outbox[0].from_email == 'from@example.com'
        assert mail.outbox[0].to == [self.customuser.email]
