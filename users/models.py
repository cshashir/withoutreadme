from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.core.validators import MaxValueValidator

from blog.models import Post
from django.conf import settings


# User = settings.AUTH_USER_MODEL


class User(AbstractUser):
    is_fellow = models.BooleanField(default=False)
    is_associate = models.BooleanField(default=False)


class ProfileFellow(models.Model):
    company_name = models.CharField(default='', max_length=100)
    first_name = models.CharField(default='', max_length=15)
    last_name = models.CharField(default='', max_length=15)
    company_profile = models.TextField(default='')
    phone = models.CharField("Phone number (without +91 or 0): 88xxx xxx88", default='', max_length=10) 
    fellow = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_fellow.png', upload_to='profile_pics_fellow')
    is_fellow = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.fellow.username} ProfileFellow'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class ProfileAssociate(models.Model):
    associate = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(default='', max_length=15)
    last_name = models.CharField(default='', max_length=15)
    gender = models.CharField(default='Male/Female', max_length=6)
    phone = models.CharField("Phone number (without +91 or 0): 88xxx xxx88", default='', max_length=10, blank=False)
    aadhaar = models.PositiveIntegerField("UIDAI (Aadhaar) number: (will be used for verification purpose)", default='0', blank=False, validators=[MaxValueValidator(9999999999999999)])
    date_of_birth = models.DateField("Date of birth: (yyyy/mm/dd)", auto_now_add=False, auto_now=False, blank=False,default=timezone.now)
    image = models.ImageField(default='default_associate.png', upload_to='profile_pics_associate')
    max_qualification = models.CharField(default='', max_length=25)
    ssc_score = models.FloatField("10th score (%):", default='100')
    ssc_result = models.FileField(default='', upload_to='associate_documents', blank=False)
    associate_bio = models.TextField("About you", default='', max_length=300)
    work_ex = models.TextField(default='Enter your work experience if any', max_length=300)
    last_updated = models.DateTimeField(default=datetime.now())
    punctuality_score = models.PositiveIntegerField(default='0')

    def __str__(self):
        return f'{self.associate.username} ProfileAssociate'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Application(models.Model):
    associate = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='applicants')
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_hired = models.BooleanField(default=False)

    class Meta:
        unique_together = ['associate', 'post']

    # def __str__(self):
    #     return self.applicant.username
