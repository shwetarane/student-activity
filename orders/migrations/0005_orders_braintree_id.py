# Generated by Django 2.2.6 on 2019-11-23 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20191122_0150'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='braintree_id',
            field=models.CharField(blank=True, max_length=160),
        ),
    ]
