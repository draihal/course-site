from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email and
        password.
        """
        user = self.create_user(
            username,
            email,
            password=password,
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _('username'),
        max_length=127, null=False,
        blank=False, unique=True,)
    email = models.EmailField(
        _('email address'),
        max_length=255, unique=True,
        validators=[validate_email],
    )
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    is_superuser = models.BooleanField(_('is_superuser'), default=False)
    date_joined = models.DateTimeField(
        _('date joined'),
        auto_now_add=True,
        editable=False,
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        ordering = ['is_staff']
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
