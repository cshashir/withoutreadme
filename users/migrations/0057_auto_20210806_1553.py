# Generated by Django 3.1.2 on 2021-08-06 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0056_auto_20210806_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileassociate',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='profilefellow',
            name='phone',
        ),
        migrations.AlterField(
            model_name='profileassociate',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 6, 15, 53, 38, 21501)),
        ),
    ]