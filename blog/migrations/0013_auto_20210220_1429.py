# Generated by Django 3.1.2 on 2021-02-20 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_post_rejection_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='contacted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contactus',
            name='resolved',
            field=models.BooleanField(default=False),
        ),
    ]
