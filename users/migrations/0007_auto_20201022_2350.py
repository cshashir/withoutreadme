# Generated by Django 3.1.2 on 2020-10-22 18:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20201022_0136'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='associate_rating_status',
            field=models.CharField(choices=[('New', 'New'), ('True', 'True'), ('False', 'False')], default='New', max_length=5),
        ),
        migrations.AddField(
            model_name='application',
            name='fellow_rating_status',
            field=models.CharField(choices=[('New', 'New'), ('True', 'True'), ('False', 'False')], default='New', max_length=5),
        ),
        migrations.AlterField(
            model_name='application',
            name='associate_comment',
            field=models.CharField(blank=True, default='', max_length=300, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='application',
            name='fellow_comment',
            field=models.CharField(blank=True, default='', max_length=300, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='profileassociate',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 22, 23, 50, 1, 57343)),
        ),
    ]
