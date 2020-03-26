from django.db import models

from rest_framework.reverse import reverse as api_reverse

from utils.mixins import TimestampMixin


class Event(TimestampMixin):
    name = models.CharField('Название мероприятия', max_length=150,)
    slug = models.SlugField('Slug для url', max_length=150, unique=True,)
    speaker = models.ForeignKey(
        'users.Teacher', on_delete=models.CASCADE, verbose_name='Ведущий')
    course = models.ForeignKey('pages.Course', on_delete=models.CASCADE, verbose_name='Курс')
    type_of_event = models.CharField('Тип мероприятия', help_text='День открытых дверей', max_length=350)
    datetime = models.DateTimeField('Время и дата проведения', )
    url_translation = models.URLField('Ссылка на запись')

    class Meta:
        ordering = ['-datetime']
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return f'{self.course} {self.speaker}'

    def get_api_url(self, request=None):
        return api_reverse('pages:events-detail', kwargs={'slug': self.slug}, request=request)
