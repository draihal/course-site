from django.db import models
from django.core.validators import validate_image_file_extension

from solo.models import SingletonModel


class AboutUsPage(SingletonModel):
    title = models.CharField(max_length=150, help_text='Название вкладки для страницы',)
    slug = models.SlugField(max_length=150, help_text='Короткое название латиницей для url')

    def upload_image_dir(self, filename):
        return f'site/pages/about_us/{filename.lower()}'

    main_image = models.ImageField(
        'Главное изображение страницы',
        upload_to=upload_image_dir,
        blank=True,
        validators=[validate_image_file_extension])  # TODO hash
    short_description = models.TextField('О КОМПАНИИ')
    short_about_us = models.TextField('Всё, что вы хотите узнать про нас', )
    updated_at = models.DateTimeField('Последнее обновление', auto_now=True)

    class Meta:
        verbose_name = 'Страница - О нас'

    def __str__(self):
        return f'Страница о нас'
