# Generated by Django 2.2.6 on 2019-11-10 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0015_auto_20191110_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_description',
            field=models.CharField(max_length=300),
        ),
    ]
