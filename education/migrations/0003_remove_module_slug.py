# Generated by Django 2.2.5 on 2019-09-17 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_auto_20190917_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='slug',
        ),
    ]