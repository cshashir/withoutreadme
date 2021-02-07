# Generated by Django 3.1.2 on 2021-01-27 19:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_auto_20210128_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileassociate',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Select', max_length=6),
        ),
        migrations.AlterField(
            model_name='profileassociate',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 0, 50, 11, 104564)),
        ),
    ]