# Generated by Django 3.1.2 on 2021-02-04 17:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0040_auto_20210204_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileassociate',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 4, 23, 22, 53, 273808)),
        ),
    ]