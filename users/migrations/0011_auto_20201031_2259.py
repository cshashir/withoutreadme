# Generated by Django 3.1.2 on 2020-10-31 17:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20201031_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilefellow',
            name='address',
            field=models.TextField(default='Reporting Address'),
        ),
        migrations.AddField(
            model_name='profilefellow',
            name='city',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='profileassociate',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 31, 22, 59, 11, 626391)),
        ),
    ]
