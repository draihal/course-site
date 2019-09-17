from django.db import models


class Review(models.Model):
    student = models.ForeignKey(
        'users.Student', on_delete=models.CASCADE, verbose_name='Студент')
    course = models.ForeignKey('pages.Course', on_delete=models.CASCADE, verbose_name='Курс')
    text = models.TextField('Отзыв', )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.course} {self.student}'
