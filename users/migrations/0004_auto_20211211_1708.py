# Generated by Django 3.1.2 on 2021-12-11 11:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211211_1649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profileassociate',
            old_name='hsc_result',
            new_name='tenplus_result',
        ),
        migrations.AlterField(
            model_name='profileassociate',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 11, 17, 7, 54, 131251)),
        ),
    ]
