from django.db import models


class TimestampMixin(models.Model):
    created_at = models.DateTimeField('Создан', auto_now_add=True)
    updated_at = models.DateTimeField('Последнее обновление', auto_now=True)

    class Meta:
        abstract = True


class BioMixin(models.Model):
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

    class Meta:
        abstract = True
