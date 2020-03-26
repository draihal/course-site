from django.db import models
from django.core.validators import RegexValidator, validate_email

from solo.models import SingletonModel


class ContactsPage(SingletonModel):
    # + and 15 digits
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Телефон должен быть в формате: '+79259999999'")

    title = models.CharField(max_length=150, help_text='Название вкладки для страницы',)
    vk = models.URLField('VK', max_length=250)
    fb = models.URLField('Facebook', max_length=250)
    ok = models.URLField('ОК', max_length=250)
    youtube = models.URLField('Youtube', max_length=250)
    telegram = models.URLField('Telegram', max_length=250)
    address = models.CharField('Адрес', max_length=250)
    details = models.TextField('Реквизиты', max_length=500)
    phone_number = models.CharField(
        'Телефонный номер',
        validators=[phone_regex],
        max_length=17)
    email = models.EmailField(
        'Email', max_length=255, validators=[validate_email])
    updated_at = models.DateTimeField('Последнее обновление', auto_now=True)

    class Meta:
        verbose_name = 'Страница - Контакты'

    def __str__(self):
        return 'Страница контактов'
