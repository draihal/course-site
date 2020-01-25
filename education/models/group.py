from django.db import models

from rest_framework.reverse import reverse as api_reverse

from utils.mixins import TimestampMixin


class Group(TimestampMixin):
    name = models.CharField('Название группы', max_length=150, help_text='PyWeb-2019-09-16')
    slug = models.SlugField('Slug для url', max_length=150, unique=True,)
    category = models.ForeignKey('pages.Course', on_delete=models.CASCADE, verbose_name='Курс')
    price = models.DecimalField('Стоимость', max_digits=10, decimal_places=2)
    date_start = models.DateField('Дата начала обучения', )
    date_end = models.DateField('Дата окончания обучения', )
    teachers = models.ManyToManyField('users.Teacher', verbose_name='Преподаватели', blank=True)
    students = models.ManyToManyField('users.Student', verbose_name='Студенты', blank=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return f'Группа {self.name}'

    def get_api_url(self, request=None):
        return api_reverse('education:groups-detail', kwargs={'slug': self.slug}, request=request)

    @staticmethod
    def get_number_of_groups():
        return Group.objects.count()
