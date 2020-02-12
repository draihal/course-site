from django.db import models

from rest_framework.reverse import reverse as api_reverse

from utils.mixins import TimestampMixin


class Grade(TimestampMixin):
    STATUS_CHOICES = (
        ('undone', 'Не сдано'),
        ('check', 'На проверке'),
        ('rework', 'На доработке'),
        ('hot', 'Сроки сдачи прошли'),
        ('done', 'Сдано'),
    )
    status = models.CharField('Статус домашнего задания', max_length=16, choices=STATUS_CHOICES)
    grade = models.TextField('Оценка преподавателя', )
    lesson = models.ForeignKey('education.Lesson', on_delete=models.CASCADE, verbose_name='Урок')
    homework = models.OneToOneField('education.Homework', on_delete=models.CASCADE, verbose_name='Домашняя работа')
    teacher = models.ForeignKey('users.Teacher', on_delete=models.CASCADE, verbose_name='Преподаватель')
    student = models.ForeignKey('users.Student', on_delete=models.CASCADE, verbose_name='Студент')
    # chat = models.ForeignKey()  # TODO: add chat
    # student_homework = models.TextField('Поле для домашннего задания', )

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __str__(self):
        return f'{self.status} {self.lesson} {self.student}'

    def get_api_url(self, request=None):
        return api_reverse('education:grades-detail', kwargs={'pk': self.pk}, request=request)
