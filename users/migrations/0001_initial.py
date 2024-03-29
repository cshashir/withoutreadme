# Generated by Django 3.1.2 on 2021-12-11 11:07

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=75, unique=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(default='8888888888', max_length=128, region=None, unique=True, verbose_name='Phone number: +9188xxx xxx88')),
                ('is_fellow', models.BooleanField(default=False)),
                ('is_associate', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ProfileFellow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='', max_length=100)),
                ('first_name', models.CharField(default='', max_length=15)),
                ('last_name', models.CharField(default='', max_length=15)),
                ('company_profile', models.TextField(default='')),
                ('image', models.ImageField(default='default_fellow.png', upload_to='profile_pics_fellow')),
                ('estd', models.PositiveIntegerField(default='1998', validators=[django.core.validators.MaxValueValidator(9999)], verbose_name='Establishment year')),
                ('is_fellow', models.BooleanField(default=True)),
                ('city', models.CharField(default='', max_length=15)),
                ('address', models.TextField(default='Reporting Address')),
                ('fellow_avg_rating', models.DecimalField(decimal_places=1, default=3, max_digits=2)),
                ('is_verified', models.BooleanField(default=False)),
                ('note_by_partshala', models.TextField(default='')),
                ('fellow', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileAssociate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=15)),
                ('last_name', models.CharField(default='', max_length=15)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Select', max_length=6)),
                ('aadhaar', models.PositiveIntegerField(default='9', validators=[django.core.validators.MaxValueValidator(999999999999)], verbose_name='UIDAI (Aadhaar) number: (will be used for verification purpose)')),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now, verbose_name='Date of birth: (yyyy-mm-dd)')),
                ('image', models.ImageField(default='default_associate.png', upload_to='profile_pics_associate', verbose_name='Profile picture:')),
                ('max_qualification', models.CharField(default='', max_length=25)),
                ('ssc_score', models.FloatField(default='100', verbose_name='10th score (%):')),
                ('hsc_score', models.FloatField(default='100', verbose_name='12th score (%):')),
                ('ssc_result', models.FileField(default='', upload_to='associate_documents', verbose_name='10th Marksheet:')),
                ('hsc_result', models.FileField(blank=True, default='Not Applicable', upload_to='associate_documents', verbose_name='12th Marksheet:')),
                ('have_dl', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Select', max_length=3, verbose_name='Do you have driving license?')),
                ('dl_copy', models.FileField(blank=True, default='Not Applicable', upload_to='associate_documents', verbose_name='Driving License:')),
                ('associate_bio', models.TextField(default='', max_length=300, verbose_name='About you:')),
                ('work_ex', models.TextField(default='Fresher', max_length=300, verbose_name='Work Experience:')),
                ('last_updated', models.DateTimeField(default=datetime.datetime(2021, 12, 11, 16, 37, 14, 774364))),
                ('associate_avg_rating', models.DecimalField(decimal_places=1, default=3, max_digits=2)),
                ('is_verified', models.BooleanField(default=False)),
                ('note_by_partshala', models.TextField(default='')),
                ('associate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('sent_to_employer', models.BooleanField(default=False)),
                ('rejected', models.BooleanField(default=False)),
                ('is_hired', models.BooleanField(default=False)),
                ('associate_rating', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5)])),
                ('fellow_rating', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5)])),
                ('associate_comment', models.CharField(blank=True, default='', max_length=300)),
                ('fellow_comment', models.CharField(blank=True, default='', max_length=300)),
                ('associate_is_rated', models.BooleanField(default=False)),
                ('fellow_is_rated', models.BooleanField(default=False)),
                ('associate_rating_status', models.CharField(choices=[('New', 'New'), ('True', 'True'), ('False', 'False')], default='New', max_length=5)),
                ('fellow_rating_status', models.CharField(choices=[('New', 'New'), ('True', 'True'), ('False', 'False')], default='New', max_length=5)),
                ('fellows_complaint_subject', models.CharField(blank=True, default='', max_length=100)),
                ('fellows_complaint', models.CharField(blank=True, default='', max_length=300)),
                ('fellow_complained', models.BooleanField(default=False)),
                ('fellows_complaint_resolved', models.BooleanField(default=False)),
                ('fellows_complaint_updating', models.BooleanField(default=False)),
                ('associates_complaint_subject', models.CharField(blank=True, default='', max_length=100)),
                ('associates_complaint', models.CharField(blank=True, default='', max_length=300)),
                ('associate_complained', models.BooleanField(default=False)),
                ('associates_complaint_resolved', models.BooleanField(default=False)),
                ('associates_complaint_updating', models.BooleanField(default=False)),
                ('recall', models.BooleanField(default=False)),
                ('note_by_partshala', models.TextField(default='')),
                ('associate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicants', to='blog.post')),
            ],
            options={
                'unique_together': {('associate', 'post')},
            },
        ),
    ]
