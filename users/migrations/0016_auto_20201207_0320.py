# Generated by Django 3.1.2 on 2020-12-06 21:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20201207_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileassociate',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 7, 3, 20, 12, 244415)),
        ),
    ]
