# Generated by Django 2.2.6 on 2019-11-10 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_auto_20191109_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_description',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
