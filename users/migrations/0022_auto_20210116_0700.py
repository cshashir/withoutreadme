# Generated by Django 3.1.2 on 2021-01-16 01:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20210116_0523'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='associates_complaint_updating',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='fellows_complaint_updating',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profileassociate',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 16, 7, 0, 52, 180419)),
        ),
    ]