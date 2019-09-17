from django.db import models
from django.core.validators import validate_image_file_extension


class MassMediaPublication(models.Model):

    def upload_image_dir(self, filename):
        return f'site/pages/massmedia/{filename.lower()}'

    main_image = models.ImageField(
        'Изображения для публикации',
        upload_to=upload_image_dir,
        blank=True,
        validators=[validate_image_file_extension])  # TODO hash
    publication_url = models.URLField('Ссылка публикации', max_length=250)
    mass_media_name = models.CharField('Название сми', max_length=250)
    short_description = models.CharField('Название публикации', max_length=250)
    date_of_publish = models.DateField('Дата публикации',)
    updated_at = models.DateTimeField(auto_now=True,)

    class Meta:
        verbose_name = 'Публикация в сми'
        verbose_name_plural = 'Публикации в сми'

    def __str__(self):
        return f'{self.short_description}'
