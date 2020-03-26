import random

from django.db import models
from django.conf import settings
from django.core.validators import validate_image_file_extension

from rest_framework.reverse import reverse as api_reverse

from utils.mixins import TimestampMixin


class PartnerManager(models.Manager):
    def get_queryset(self):
        return super(PartnerManager, self).get_queryset().select_related('user').prefetch_related('courses')


def upload_logo_image_dir(instance, filename):
    return f'partners/logo/{filename.lower()}'


class Partner(TimestampMixin):
    objects = PartnerManager()
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        primary_key=True, related_name='partner')
    logo = models.ImageField(
        'Логотип компании',
        upload_to=upload_logo_image_dir,
        blank=True,
        validators=[validate_image_file_extension])  # TODO hash
    company = models.CharField('Название компании', max_length=255, blank=True)
    info = models.TextField('О компании', max_length=500, blank=True)
    courses = models.ManyToManyField(
        'pages.Course', verbose_name='Выпусники каких курсов интересуют', blank=True)

    class Meta:
        ordering = ['company']
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

    def __str__(self):
        return self.company

    def get_api_url(self, request=None):
        return api_reverse('users:partner-profile-detail', kwargs={'pk': self.user.pk}, request=request)

    @staticmethod
    def get_random_partners(number_of_partners):
        valid_id_list = Partner.objects.values_list('user__id', flat=True)  # QuerySet [1, 2, 3, ...] flat=True
        random_id_list = random.sample(
            list(valid_id_list),
            min(len(valid_id_list), number_of_partners)
        )
        query_set = Partner.objects.filter(user__id__in=random_id_list)
        return query_set
