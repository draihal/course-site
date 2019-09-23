from django.db import models
from django.conf import settings
from django.core.validators import validate_image_file_extension

from rest_framework.reverse import reverse as api_reverse


class Teacher(models.Model):
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
    first_name_lat = models.CharField(
        'Имя (латиницей)', max_length=127, blank=True)
    last_name_lat = models.CharField(
        'Фамилия (латиницей)', max_length=127, blank=True)
    username = models.CharField('Имя (в блоге)', max_length=127, blank=True)
    birth_date = models.DateField('Дата рождения', blank=True)
    COUNTRY_CHOICES = (('NA', 'Не указано'), ('RU', 'Россия'),
                       ('BY', 'Республика Беларусь'), ('KZ', 'Казахстан'),
                       ('UA', 'Украина'))
    country = models.CharField('Страна', max_length=2, choices=COUNTRY_CHOICES)
    city = models.CharField('Город', max_length=127)
    SEX_CHOICES = (('0', 'Не указано'), ('m', 'Мужской'), ('f', 'Женский'))
    sex = models.CharField('Пол', max_length=1, choices=SEX_CHOICES)
    company = models.CharField('Компания', max_length=127, blank=True)
    position = models.CharField('Должность', max_length=127, blank=True)
    created_at = models.DateTimeField('Создан', auto_now_add=True)
    updated_at = models.DateTimeField('Последнее обновление', auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name if self.user.last_name else ""}'

    def get_api_url(self, request=None):
        return api_reverse('users:teacher-profile-detail', kwargs={'pk': self.user.pk}, request=request)
