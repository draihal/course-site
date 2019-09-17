from django.db import models


class Event(models.Model):
    name = models.CharField('Название мероприятия', max_length=150,)
    slug = models.SlugField('Slug для url', max_length=150, unique=True,)
    speaker = models.ForeignKey(
        'users.Teacher', on_delete=models.CASCADE, verbose_name='Ведущий')
    course = models.ForeignKey('pages.Course', on_delete=models.CASCADE, verbose_name='Курс')
    type_of_event = models.CharField('Тип мероприятия', help_text='День открытых дверей', max_length=350)
    datetime = models.DateTimeField('Время и дата проведения', )
    url = models.URLField('Ссылка на запись')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return f'{self.course} {self.student}'
