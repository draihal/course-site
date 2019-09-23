from django.db import models


class Lesson(models.Model):
    name = models.CharField('Название урока', max_length=150, )
    slug = models.SlugField('Slug для url', max_length=150, unique=True,)
    module = models.ForeignKey('education.Module', on_delete=models.CASCADE, verbose_name='Модуль')
    group = models.ForeignKey('education.Group', on_delete=models.CASCADE, verbose_name='Группа')
    number = models.PositiveSmallIntegerField('Номер урока')
    description = models.TextField('Описание урока', )
    poll_url = models.URLField('Ссылка для опроса', )
    datetime = models.DateTimeField('Дата и время проведения', )
    url = models.URLField('Ссылка на урок',)
    homework_title = models.CharField('Название домашнего задания', max_length=250)
    homework_description = models.TextField('Описание домашнего задания',)
    homework_date = models.DateField('Дата сдачи до', )
    # materials = models.ForeignKey()  # TODO polymorphic
    created_at = models.DateTimeField('Создан', auto_now_add=True)
    updated_at = models.DateTimeField('Последнее обновление', auto_now=True)

    class Meta:
        ordering = ('-datetime',)
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return f'Урок {self.name}'
