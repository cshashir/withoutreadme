# Generated by Django 3.1.2 on 2021-01-27 19:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_auto_20210127_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileassociate',
            name='gender',
            field=models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Other', 'other')], default='Select', max_length=6),
        ),
        migrations.AlterField(
            model_name='profileassociate',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 0, 48, 24, 333856)),
        ),
    ]
