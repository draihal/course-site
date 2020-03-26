import random
from rest_framework.reverse import reverse as api_reverse

from django.db import models
from django.conf import settings
from django.core.validators import validate_image_file_extension

from .mixins import BioMixin
from utils.mixins import TimestampMixin


class TeacherManager(models.Manager):
    def get_queryset(self):
        return super(TeacherManager, self).get_queryset().select_related('user')


def upload_avatar_image_dir(instance, filename):
    return f'avatars/teachers/{filename.lower()}'


class Teacher(BioMixin, TimestampMixin):
    objects = TeacherManager()
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        primary_key=True, related_name='teacher')
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
        return f'{self.user.first_name} {self.user.last_name or ""}'

    def get_api_url(self, request=None):
        return api_reverse('users:teacher-profile-detail', kwargs={'pk': self.user.pk}, request=request)

    @staticmethod
    def get_number_of_teachers():
        return Teacher.objects.count()

    @staticmethod
    def get_random_teachers(number_of_teachers):
        valid_id_list = Teacher.objects.values_list('user__id', flat=True)  # QuerySet [1, 2, 3, ...] flat=True
        random_id_list = random.sample(
            list(valid_id_list),
            min(len(valid_id_list), number_of_teachers)
        )
        query_set = Teacher.objects.filter(user__id__in=random_id_list)
        return query_set
