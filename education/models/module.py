from django.db import models


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
