from django.db import models
from django.conf import settings
from django.core.validators import validate_image_file_extension


class Partner(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        primary_key=True)

    def upload_logo_image_dir(self, filename):
        url = f'/partners/logo/{filename.lower()}'
        return url

    logo = models.ImageField(
        'Логотип компании',
        upload_to=upload_logo_image_dir,
        blank=True,
        validators=[validate_image_file_extension])  # TODO hash
    company = models.CharField('Название компании', max_length=127)
    info = models.TextField('О компании', max_length=500, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    courses = models.ManyToManyField(
        'pages.Course', verbose_name='Выпусники каких курсов интересуют', blank=True)

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

    def __str__(self):
        return f'{self.company} {self.user.first_name}'
