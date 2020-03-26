from django.db import models

from rest_framework.reverse import reverse as api_reverse

from utils.mixins import TimestampMixin


class Payment(TimestampMixin):
    datetime = models.DateTimeField('Дата оплаты', )
    invoice = models.URLField('Ссылка на чек', max_length=250)
    module = models.ForeignKey('education.Module', on_delete=models.DO_NOTHING, verbose_name='Модуль')
    student = models.ForeignKey('users.Student', on_delete=models.DO_NOTHING, verbose_name='Студент')

    class Meta:
        ordering = ['-datetime']
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплата'

    def __str__(self):
        return f'{self.student} {self.module} {self.module.group}'

    def get_api_url(self, request=None):
        return api_reverse('education:payments-detail', kwargs={'pk': self.pk}, request=request)
