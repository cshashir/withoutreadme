# Generated by Django 3.1.2 on 2020-10-31 22:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20201101_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileassociate',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 1, 4, 24, 5, 192248)),
        ),
    ]
