# Generated by Django 3.1.2 on 2020-10-31 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201021_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=25)),
                ('email', models.EmailField(default='', max_length=30)),
                ('comment', models.TextField(default='')),
            ],
        ),
    ]
