from django.db import models
from django.core.validators import validate_image_file_extension

from rest_framework.reverse import reverse as api_reverse

from utils.mixins import TimestampMixin


def upload_image_dir(instance, filename):
    return f'site/pages/massmedia/{filename.lower()}'


class MassMediaPublication(TimestampMixin):
    name = models.CharField('Название публикации', max_length=150,)
    slug = models.SlugField('Slug для url', max_length=150, unique=True,)
    main_image = models.ImageField(
        'Изображения для публикации',
        upload_to=upload_image_dir,
        blank=True,
        validators=[validate_image_file_extension])  # TODO hash
    publication_url = models.URLField('Ссылка публикации', max_length=250)
    mass_media_name = models.CharField('Название сми', max_length=250)
    date_of_publish = models.DateField('Дата публикации',)

    class Meta:
        ordering = ['-date_of_publish']
        verbose_name = 'Публикация в сми'
        verbose_name_plural = 'Публикации в сми'

    def __str__(self):
        return self.name

    def get_api_url(self, request=None):
        return api_reverse('pages:publications-detail', kwargs={'slug': self.slug}, request=request)
