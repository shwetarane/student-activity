# Generated by Django 2.2.6 on 2019-11-11 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0020_auto_20191111_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='available_in_library',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_store',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='book',
            name='library_shelf',
            field=models.CharField(blank=True, max_length=4),
        ),
    ]