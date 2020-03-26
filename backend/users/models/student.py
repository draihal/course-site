from django.db import models
from django.conf import settings
from django.core.validators import validate_image_file_extension

from rest_framework.reverse import reverse as api_reverse

from .mixins import BioMixin
from utils.mixins import TimestampMixin


class StudentManager(models.Manager):
    def get_queryset(self):
        return super(StudentManager, self).get_queryset().select_related('user')


def upload_avatar_image_dir(instance, filename):
    return f'avatars/students/{filename.lower()}'


class Student(BioMixin, TimestampMixin):
    objects = StudentManager()
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        primary_key=True, related_name='student')
    avatar = models.ImageField(
        'Фотография',
        upload_to=upload_avatar_image_dir,
        blank=True,
        validators=[validate_image_file_extension])  # TODO hash
    can_relocate = models.BooleanField('Готовность к переезду', default=False)
    can_full_time = models.BooleanField('Полный день', default=False)
    can_part_time = models.BooleanField('Гибкий график', default=False)
    can_remote = models.BooleanField('Удаленно', default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name or ""}'

    def get_api_url(self, request=None):
        return api_reverse('users:student-profile-detail', kwargs={'pk': self.user.pk}, request=request)

    @staticmethod
    def get_number_of_students():
        return Student.objects.count()
