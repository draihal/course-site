# Generated by Django 2.2.5 on 2019-09-16 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('undone', 'Не сдано'), ('check', 'На проверке'), ('rework', 'На доработке'), ('hot', 'Сроки сдачи прошли'), ('done', 'Сдано')], max_length=6, verbose_name='Статус домашнего задания')),
                ('grade', models.TextField(verbose_name='Оценка преподавателя')),
            ],
            options={
                'verbose_name': 'Оценка',
                'verbose_name_plural': 'Оценки',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='PyWeb-2019-09-16', max_length=150, verbose_name='Название группы')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='Slug для url')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость')),
                ('date_start', models.DateField(verbose_name='Дата начала обучения')),
                ('date_end', models.DateField(verbose_name='Дата окончания обучения')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название урока')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='Slug для url')),
                ('number', models.PositiveSmallIntegerField(verbose_name='Номер урока')),
                ('description', models.TextField(verbose_name='Описание урока')),
                ('poll_url', models.URLField(verbose_name='Ссылка для опроса')),
                ('datetime', models.DateTimeField(verbose_name='Дата и время проведения')),
                ('url', models.URLField(verbose_name='Сылка на урок')),
                ('homework_title', models.CharField(max_length=250, verbose_name='Название домашнего задания')),
                ('homework_description', models.TextField(verbose_name='Описание домашнего задания')),
                ('homework_date', models.DateField(verbose_name='Дата сдачи до')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='1 месяц', max_length=150, verbose_name='Название модуля')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='Slug для url')),
            ],
            options={
                'verbose_name': 'Модуль',
                'verbose_name_plural': 'Модули',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='Дата оплаты')),
                ('invoice', models.URLField(max_length=250, verbose_name='Ссылка на чек')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='education.Module', verbose_name='Модуль')),
            ],
            options={
                'verbose_name': 'Оплата',
                'verbose_name_plural': 'Оплата',
            },
        ),
    ]
