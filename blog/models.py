from django.db import models
from django.utils import timezone
from datetime import date, datetime
from django.core.validators import MaxValueValidator
from django.conf import settings
from django.urls import reverse


User = settings.AUTH_USER_MODEL


class Post(models.Model):
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    skills_reqd = models.TextField(default='Skills expected')
    post_date = models.DateField(default=timezone.now)
    start_date = models.DateField("Start date: (yyyy-mm-dd)", auto_now_add=False, auto_now=False, blank=False,default=timezone.now)
    end_date = models.DateField("End date: (yyyy-mm-dd)", auto_now_add=False, auto_now=False, blank=False,default=timezone.now)
    start_time = models.TimeField("Start time: (HH:MM)", blank=False, null=True)
    end_time = models.TimeField("End time: (HH:MM)", blank=False, null=True)
    fellow = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=15, default='')
    vacancy = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(50)])
    address = models.TextField(default='Reporting Address')
    stipend = models.IntegerField(default=0, blank=True)
    filled = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.job_title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'id': self.id})


class ContactUs(models.Model):
    name  = models.CharField(default='',max_length=25, blank=False)
    email = models.EmailField(default='', max_length=30, blank=False)
    subject = models.TextField(default='', blank=False)
    comment = models.TextField(default='', blank=False)

    def __str__(self):
        return self.name