# Generated by Django 2.2.5 on 2019-11-22 01:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191029_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='from_date',
            field=models.DateField(default=datetime.date(2019, 11, 22)),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(default='FEMALE', max_length=10),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='to_date',
            field=models.DateField(default=datetime.date(2019, 11, 22)),
        ),
    ]