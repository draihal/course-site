from django.db import models
from django.conf import settings
from django.core.validators import validate_image_file_extension


class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        primary_key=True)

    def upload_avatar_image_dir(self, filename):
        url = f'avatars/students/{filename.lower()}'
        return url

    avatar = models.ImageField(
        'Фотография',
        upload_to=upload_avatar_image_dir,
        blank=True,
        validators=[validate_image_file_extension])  # TODO hash
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
    relocate = models.BooleanField('Готовность к переезду', )
    full_time = models.BooleanField('Полный день', )
    part_time = models.BooleanField('Гибкий график', )
    remote = models.BooleanField('Удаленно', )
    SEX_CHOICES = (('0', 'Не указано'), ('m', 'Мужской'), ('f', 'Женский'))
    sex = models.CharField('Пол', max_length=1, choices=SEX_CHOICES)
    company = models.CharField('Компания', max_length=127, blank=True)
    position = models.CharField('Должность', max_length=127, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name if self.user.last_name else ""}'
