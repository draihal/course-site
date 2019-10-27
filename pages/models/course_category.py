from django.db import models
from django.core.validators import validate_image_file_extension

from rest_framework.reverse import reverse as api_reverse


def upload_image_dir(instance, filename):
    return f'site/categories/{filename.lower()}'


class CourseCategory(models.Model):
    name = models.CharField('Название категории', max_length=150,)
    slug = models.SlugField('Slug для url', max_length=150, unique=True,)
    image = models.ImageField(
        'Изображение для категории',
        upload_to=upload_image_dir,
        blank=True,
        validators=[validate_image_file_extension])  # TODO hash
    updated_at = models.DateTimeField('Последнее обновление', auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория курса'
        verbose_name_plural = 'Категории курсов'

    def __str__(self):
        return self.name

    def get_api_url(self, request=None):
        return api_reverse('pages:categories-detail', kwargs={'slug': self.slug}, request=request)
