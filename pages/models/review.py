from django.db import models

from rest_framework.reverse import reverse as api_reverse


class Review(models.Model):
    student = models.ForeignKey(
        'users.Student', on_delete=models.CASCADE, verbose_name='Студент')
    course = models.ForeignKey('pages.Course', on_delete=models.CASCADE, verbose_name='Курс')
    text = models.TextField('Отзыв', )
    created_at = models.DateTimeField('Создан', auto_now_add=True)
    updated_at = models.DateTimeField('Последнее обновление', auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.course} {self.student}'

    def get_api_url(self, request=None):
        return api_reverse('pages:reviews-detail', kwargs={'pk': self.pk}, request=request)
