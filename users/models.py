from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.core.validators import MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
# from phone_field import PhoneField


from blog.models import Post
from django.conf import settings


# User = settings.AUTH_USER_MODEL


class User(AbstractUser):
    username = models.CharField(unique=True,max_length=30)
    email = models.EmailField(unique=True,max_length=75)
    is_fellow = models.BooleanField(default=False)
    is_associate = models.BooleanField(default=False)


class ProfileFellow(models.Model):
    fellow = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(default='', max_length=100)
    first_name = models.CharField(default='', max_length=15)
    last_name = models.CharField(default='', max_length=15)
    company_profile = models.TextField(default='')
    phone = PhoneNumberField(unique=True,unique=False,null=False, blank=False)
    image = models.ImageField(default='default_fellow.png', upload_to='profile_pics_fellow')
    estd = models.PositiveIntegerField("Establishment year", default='1998', blank=False, validators=[MaxValueValidator(9999999999)])
    is_fellow = models.BooleanField(default=True)
    city = models.CharField(max_length=15, default='')
    address = models.TextField(default='Reporting Address')
    fellow_avg_rating = models.DecimalField(default=3, max_digits=2, decimal_places=1)
    is_verified = models.BooleanField(default=False)
    note_by_partshala = models.TextField(default='')

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

    Gender = (
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    )
    associate = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(default='', max_length=15)
    last_name = models.CharField(default='', max_length=15)
    gender = models.CharField(choices=Gender, max_length=6, default='Select')
    phone = PhoneNumberField( "Phone number: +9188xxx xxx88", unique=False,null=False, blank=False)
    aadhaar = models.PositiveIntegerField("UIDAI (Aadhaar) number: (will be used for verification purpose)", default='9', blank=False, validators=[MaxValueValidator(9999999999999999)])
    date_of_birth = models.DateField("Date of birth: (yyyy-mm-dd)", auto_now_add=False, auto_now=False, blank=False,default=timezone.now)
    image = models.ImageField(default='default_associate.png', upload_to='profile_pics_associate')
    max_qualification = models.CharField(default='', max_length=25)
    ssc_score = models.FloatField("10th score (%):", default='100')
    hsc_score = models.FloatField("12th score (%):", default='100')
    ssc_result = models.FileField(default='', upload_to='associate_documents', blank=False)
    hsc_result = models.FileField(default='Not Available', upload_to='associate_documents', blank=True)
    associate_bio = models.TextField("About you", default='', max_length=300)
    work_ex = models.TextField("Work Experience:",default='Fresher', max_length=300)
    last_updated = models.DateTimeField(default=datetime.now())
    associate_avg_rating = models.DecimalField(default=3, max_digits=2, decimal_places=1)
    is_verified = models.BooleanField(default=False)
    note_by_partshala = models.TextField(default='')


    def get_age(self):
        now = datetime.now()
        age = (now.date() - self.date_of_birth).days/365.25
        return int(age)

    age = property(get_age)


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
    AssociateRate = (
        ('New','New'),
        ('True','True'),
        ('False','False'),
    )
    FellowRate = (
        ('New','New'),
        ('True','True'),
        ('False','False'),
    )
    associate = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='applicants')
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    sent_to_employer = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    is_hired = models.BooleanField(default=False)
    associate_rating = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5)])
    fellow_rating = models.IntegerField(default=1, validators=[MaxValueValidator(5)])
    associate_comment = models.CharField(default='', max_length=300, blank=True)
    fellow_comment = models.CharField(default='', max_length=300, blank=True)
    associate_is_rated = models.BooleanField(default=False)
    fellow_is_rated = models.BooleanField(default=False)
    associate_rating_status = models.CharField(choices=AssociateRate, max_length=5, default='New')
    fellow_rating_status = models.CharField(choices=FellowRate, max_length=5, default='New')
    fellows_complaint_subject = models.CharField(default='', max_length=100, blank=True)
    fellows_complaint = models.CharField(default='', max_length=300, blank=True)
    fellow_complained = models.BooleanField(default=False)
    fellows_complaint_resolved = models.BooleanField(default=False)
    fellows_complaint_updating = models.BooleanField(default=False)
    associates_complaint_subject = models.CharField(default='', max_length=100, blank=True)
    associates_complaint = models.CharField(default='', max_length=300, blank=True)
    associate_complained = models.BooleanField(default=False)
    associates_complaint_resolved = models.BooleanField(default=False)
    associates_complaint_updating = models.BooleanField(default=False)
    recall = models.BooleanField(default=False)
    note_by_partshala = models.TextField(default='')


    class Meta:
        unique_together = ['associate', 'post']

    # def __str__(self):
    #     return self.applicant.username
