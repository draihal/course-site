from django.db import models

from .lesson import Lesson


class Grade(models.Model):
    STATUS_CHOICES = (
        ('undone', 'Не сдано'),
        ('check', 'На проверке'),
        ('rework', 'На доработке'),
        ('hot', 'Сроки сдачи прошли'),
        ('done', 'Сдано'),
    )
    status = models.CharField('Статус домашнего задания', max_length=6, choices=STATUS_CHOICES)
    grade = models.TextField('Оценка преподавателя', )
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок')
    teacher = models.ForeignKey('users.Teacher', on_delete=models.DO_NOTHING, verbose_name='Преподаватель')
    student = models.ForeignKey('users.Student', on_delete=models.DO_NOTHING, verbose_name='Студент')
    # chat = models.ForeignKey()  # TODO

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __str__(self):
        return f'{self.status} {self.lesson} {self.student}'
