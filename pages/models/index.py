from django.db import models

from solo.models import SingletonModel


class IndexPage(SingletonModel):
    title = models.CharField(max_length=150, help_text='Основное название',)
    short_description = models.TextField('Краткое описание')
    description = models.TextField('Основное описание')
    updated_at = models.DateTimeField('Последнее обновление', auto_now=True)

    class Meta:
        verbose_name = 'Страница - Главная'

    def __str__(self):
        return 'Главная страница'
