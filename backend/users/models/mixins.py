from django.db import models


class BioMixin(models.Model):
    COUNTRY_CHOICES = (('NA', 'Не указано'), ('RU', 'Россия'),
                       ('BY', 'Республика Беларусь'), ('KZ', 'Казахстан'),
                       ('UA', 'Украина'))
    SEX_CHOICES = (('0', 'Не указано'), ('m', 'Мужской'), ('f', 'Женский'))

    # Fields
    first_name_lat = models.CharField(
        'Имя (латиницей)', max_length=127, blank=True)
    last_name_lat = models.CharField(
        'Фамилия (латиницей)', max_length=127, blank=True)
    username = models.CharField('Имя (в блоге)', max_length=127, blank=True)
    birth_date = models.DateField('Дата рождения', blank=True, null=True)
    country = models.CharField('Страна', max_length=2, choices=COUNTRY_CHOICES, default='NA')
    city = models.CharField('Город', max_length=127, blank=True)
    sex = models.CharField('Пол', max_length=1, choices=SEX_CHOICES, default='0')
    company = models.CharField('Компания', max_length=127, blank=True)
    position = models.CharField('Должность', max_length=127, blank=True)

    class Meta:
        abstract = True
