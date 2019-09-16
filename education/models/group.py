from django.db import models

from pages.models.course import Course


class Group(models.Model):
    name = models.CharField('Название группы', max_length=150, help_text='PyWeb-2019-09-16')
    slug = models.SlugField('Slug для url', max_length=150, unique=True,)
    category = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name='Курс')
    price = models.DecimalField('Стоимость', max_digits=10, decimal_places=2)
    date_start = models.DateField('Дата начала обучения', )
    date_end = models.DateField('Дата окончания обучения', )
    teachers = models.ManyToManyField('users.Teacher', verbose_name='Преподаватели', blank=True)
    students = models.ManyToManyField('users.Student', verbose_name='Студенты', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name
