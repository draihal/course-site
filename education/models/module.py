from django.db import models

from rest_framework.reverse import reverse as api_reverse


class Module(models.Model):
    name = models.CharField('Название модуля', max_length=150, help_text='1 месяц')
    group = models.ForeignKey('education.Group', on_delete=models.CASCADE, verbose_name='Группа')
    created_at = models.DateTimeField('Создан', auto_now_add=True)
    updated_at = models.DateTimeField('Последнее обновление', auto_now=True)

    class Meta:
        ordering = ('group',)
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'

    def __str__(self):
        return f'{self.name}'

    def get_api_url(self, request=None):
        return api_reverse('education:modules-detail', kwargs={'pk': self.pk}, request=request)
