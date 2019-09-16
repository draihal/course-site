# Generated by Django 2.2.5 on 2019-09-16 20:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import pages.models.about_us
import pages.models.course
import pages.models.course_category
import pages.models.mass_media
import pages.models.site_configuration


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Название вкладки для страницы', max_length=150)),
                ('slug', models.SlugField(help_text='Короткое название латиницей для url', max_length=150)),
                ('main_image', models.ImageField(blank=True, upload_to=pages.models.about_us.AboutUsPage.upload_image_dir, validators=[django.core.validators.validate_image_file_extension], verbose_name='Главное изображение страницы')),
                ('short_description', models.CharField(max_length=250, verbose_name='О КОМПАНИИ')),
                ('short_about_us', models.TextField(max_length=750, verbose_name='Всё, что вы хотите узнать про нас')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Страница - О нас',
                'verbose_name_plural': 'Страница - О нас',
            },
        ),
        migrations.CreateModel(
            name='ContactsPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vk', models.URLField(max_length=250, verbose_name='VK')),
                ('fb', models.URLField(max_length=250, verbose_name='Facebook')),
                ('ok', models.URLField(max_length=250, verbose_name='ОК')),
                ('youtube', models.URLField(max_length=250, verbose_name='Youtube')),
                ('telegram', models.URLField(max_length=250, verbose_name='Telegram')),
                ('address', models.CharField(max_length=250, verbose_name='Адрес')),
                ('details', models.TextField(max_length=500, verbose_name='Реквизиты')),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Телефон должен быть в формате: '+79259999999'", regex='^\\+?1?\\d{9,15}$')], verbose_name='Телефонный номер')),
                ('email', models.EmailField(max_length=255, validators=[django.core.validators.EmailValidator()], verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='Slug для url')),
                ('image', models.ImageField(blank=True, upload_to=pages.models.course_category.CourseCategory.upload_image_dir, validators=[django.core.validators.validate_image_file_extension], verbose_name='Изображение для категории')),
            ],
            options={
                'verbose_name': 'Категория курса',
                'verbose_name_plural': 'Категории курсов',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='MassMediaPublication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(blank=True, upload_to=pages.models.mass_media.MassMediaPublication.upload_image_dir, validators=[django.core.validators.validate_image_file_extension], verbose_name='Изображения для публикации')),
                ('publication_url', models.URLField(max_length=250, verbose_name='url публикации')),
                ('mass_media_name', models.CharField(max_length=250, verbose_name='Название сми')),
                ('short_description', models.CharField(max_length=250, verbose_name='Название публикации')),
                ('date_of_publish', models.DateField(verbose_name='Дата публикации')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Публикация в сми',
                'verbose_name_plural': 'Публикации в сми',
            },
        ),
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название страницы')),
                ('logo', models.ImageField(blank=True, upload_to=pages.models.site_configuration.SiteConfiguration.upload_logo_image_dir, validators=[django.core.validators.validate_image_file_extension], verbose_name='Логотип сайта курсов')),
                ('short_description', models.CharField(max_length=250, verbose_name='Слоган сайта курсов')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Основная информация',
                'verbose_name_plural': 'Основная информация',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название курса')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='Slug для url')),
                ('image', models.ImageField(blank=True, upload_to=pages.models.course.Course.upload_image_dir, validators=[django.core.validators.validate_image_file_extension], verbose_name='Изображение для курса')),
                ('description', models.TextField(verbose_name='Что даст этот курс')),
                ('necessary_knowledge', models.TextField(verbose_name='Необходимые знания')),
                ('study_process', models.TextField(verbose_name='Процесс обучения')),
                ('graduation_project', models.TextField(verbose_name='Выпускной проект')),
                ('after_training', models.TextField(verbose_name='После обучения')),
                ('certificate_sample', models.ImageField(blank=True, upload_to=pages.models.course.Course.upload_image_dir, validators=[django.core.validators.validate_image_file_extension], verbose_name='Образец сертификата')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.CourseCategory', verbose_name='Категория курса')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
                'ordering': ('name',),
            },
        ),
    ]
