# Generated by Django 2.2.6 on 2019-11-09 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20191109_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(default='', max_length=80, unique=True),
        ),
    ]
