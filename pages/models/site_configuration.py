from django.db import models
from django.core.validators import validate_image_file_extension

from solo.models import SingletonModel


def upload_logo_image_dir(instance, filename):
    return f'site/logo/{filename.lower()}'


class SiteConfiguration(SingletonModel):
    title = models.CharField('Название вкладки с сайтом', max_length=250)
    logo = models.ImageField(
        'Логотип сайта курсов',
        upload_to=upload_logo_image_dir,
        blank=True,
        validators=[validate_image_file_extension])  # TODO hash
    short_description = models.CharField('Слоган сайта курсов', max_length=250)
    updated_at = models.DateTimeField('Последнее обновление', auto_now=True)

    class Meta:
        verbose_name = 'Основная информация'

    def __str__(self):
        return self.short_description
