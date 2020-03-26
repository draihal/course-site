from django.db import models

from rest_framework.reverse import reverse as api_reverse

from utils.mixins import TimestampMixin


class Module(TimestampMixin):
    name = models.CharField('Название модуля', max_length=150, help_text='1 месяц')
    group = models.ForeignKey('education.Group', on_delete=models.CASCADE, verbose_name='Группа')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'

    def __str__(self):
        return self.name

    def get_api_url(self, request=None):
        return api_reverse('education:modules-detail', kwargs={'pk': self.pk}, request=request)
