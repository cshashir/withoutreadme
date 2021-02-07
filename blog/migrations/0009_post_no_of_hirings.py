# Generated by Django 3.1.2 on 2021-02-04 17:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_rejection_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='no_of_hirings',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]