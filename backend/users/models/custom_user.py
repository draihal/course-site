from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.core.validators import validate_email, RegexValidator

from rest_framework.reverse import reverse as api_reverse

from utils.mixins import TimestampMixin


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(
            self, first_name, email, phone_number,
            last_name='', is_student=False, is_teacher=False,
            is_partner=False, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Email обязателен!')
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            is_student=is_student,
            is_teacher=is_teacher,
            is_partner=is_partner,
            phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, email, phone_number, password):
        """
        Creates and saves a superuser with the given email and
        password.
        """
        user = self.create_user(
            first_name, email, phone_number, password=password,
            last_name='', is_student=False,
            is_teacher=False, is_partner=False
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# TODO: add post signal to create student or teacher or partner model if need
class CustomUser(AbstractBaseUser, PermissionsMixin, TimestampMixin):
    # + and 15 digits
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Телефон должен быть в формате: '+79259999999'")

    # Fields
    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255, blank=True)
    email = models.EmailField(
        'Email', max_length=255, unique=True, validators=[validate_email])
    phone_number = models.CharField(
        'Телефонный номер',
        validators=[phone_regex],
        max_length=17,
        unique=True)
    is_student = models.BooleanField('Студент', default=False)
    is_teacher = models.BooleanField('Преподаватель', default=False)
    is_partner = models.BooleanField('Партнер', default=False)
    is_active = models.BooleanField('Активный', default=True)
    is_staff = models.BooleanField('Сотрудник', default=False)
    is_superuser = models.BooleanField('Админ', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'phone_number']

    class Meta:
        ordering = ['is_staff']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Все пользователи'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name or ""}'

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.get_full_name()

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_api_url(self, request=None):
        return api_reverse('users:user-detail', kwargs={'pk': self.pk}, request=request)
