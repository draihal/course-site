# Generated by Django 2.2.10 on 2020-03-05 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_indexpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutuspage',
            name='short_about_us',
            field=models.TextField(blank=True, verbose_name='Всё, что вы хотите узнать про нас'),
        ),
        migrations.AlterField(
            model_name='aboutuspage',
            name='short_description',
            field=models.TextField(blank=True, verbose_name='О КОМПАНИИ'),
        ),
        migrations.AlterField(
            model_name='aboutuspage',
            name='title',
            field=models.CharField(blank=True, help_text='Название вкладки для страницы', max_length=150),
        ),
    ]
