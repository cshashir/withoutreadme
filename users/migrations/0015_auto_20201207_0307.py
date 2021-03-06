# Generated by Django 3.1.2 on 2020-12-06 21:37

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20201101_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileassociate',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date of birth: (yyyy-mm-dd)'),
        ),
        migrations.AlterField(
            model_name='profileassociate',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 7, 3, 7, 17, 134029)),
        ),
    ]
