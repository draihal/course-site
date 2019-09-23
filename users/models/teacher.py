from django.db import models
from django.conf import settings
from django.core.validators import validate_image_file_extension

from rest_framework.reverse import reverse as api_reverse

from .mixins import BioMixin, TimestampMixin


class TeacherManager(models.Manager):
    def get_queryset(self):
        return super(TeacherManager, self).get_queryset().select_related('user')


class Teacher(BioMixin, TimestampMixin):
    objects = TeacherManager()
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        primary_key=True, related_name='teacher')

    def upload_avatar_image_dir(self, filename):
        return f'avatars/teachers/{filename.lower()}'

    avatar = models.ImageField(
        'Фотография',
        upload_to=upload_avatar_image_dir,
        blank=True,
        validators=[validate_image_file_extension])  # TODO hash
    bio = models.TextField('О себе', max_length=500, blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name if self.user.last_name else ""}'

    def get_api_url(self, request=None):
        return api_reverse('users:teacher-profile-detail', kwargs={'pk': self.user.pk}, request=request)
