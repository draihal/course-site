from django.db import models

from .group import Group


class Module(models.Model):
    name = models.CharField('Название модуля', max_length=150, help_text='1 месяц')
    slug = models.SlugField('Slug для url', max_length=150, unique=True,)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, verbose_name='Группа')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'

    def __str__(self):
        return self.name
