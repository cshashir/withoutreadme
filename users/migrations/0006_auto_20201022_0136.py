# Generated by Django 3.1.2 on 2020-10-21 20:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20201021_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='associate_comment',
            field=models.TextField(default='', max_length=300, verbose_name='Comment here'),
        ),
        migrations.AddField(
            model_name='application',
            name='fellow_comment',
            field=models.TextField(default='', max_length=300, verbose_name='Comment here'),
        ),
        migrations.AlterField(
            model_name='profileassociate',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 22, 1, 36, 20, 699329)),
        ),
    ]
