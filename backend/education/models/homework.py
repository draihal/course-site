from django.db import models

from rest_framework.reverse import reverse as api_reverse

from utils.mixins import TimestampMixin


class Homework(TimestampMixin):
    lesson = models.ForeignKey('education.Lesson', on_delete=models.CASCADE, verbose_name='Урок')
    student = models.ForeignKey('users.Student', on_delete=models.CASCADE, verbose_name='Студент')
    # chat = models.ForeignKey()  # TODO: add chat
    student_homework = models.TextField('Поле для домашнего задания', )

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Домашние задания'

    def __str__(self):
        return f'{self.lesson} {self.student}'

    def get_api_url(self, request=None):
        return api_reverse('education:homework-detail', kwargs={'pk': self.pk}, request=request)
