# Generated by Django 3.1.2 on 2021-02-18 18:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0045_auto_20210219_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileassociate',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 19, 0, 1, 41, 942140)),
        ),
    ]