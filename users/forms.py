from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from blog.models import ContactUs


class UserLoginForm(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}), required=True, max_length=30)
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}), required=True, max_length=30)


class FellowRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class FellowUpdateForm(forms.ModelForm):
    # email = forms.EmailField()

    class Meta:
        model = ProfileFellow
        fields = ['first_name', 'last_name','company_name', 'estd', 'company_profile', 'city', 'address', 'phone']


class FellowPicUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileFellow
        fields = ['image']


class AssociateRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']


class AssociateUpdateForm(forms.ModelForm):
    # email = forms.EmailField()

    class Meta:
        model = ProfileAssociate
        fields = ['first_name', 'last_name','date_of_birth', 'gender', 'max_qualification','ssc_score', 'phone', 'aadhaar', 'associate_bio', 'work_ex']


class AssociatePicUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileAssociate
        fields = ['image']


class SSCResultForm(forms.ModelForm):
    class Meta:
        model = ProfileAssociate
        fields = ['ssc_result']


class ApplyJobForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['post']


class AssociateRateForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ['associate_rating', 'associate_comment']


class FellowRateForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ['fellow_rating', 'fellow_comment']


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = ['name', 'email','subject', 'comment']



class FellowsComplaintForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ['fellows_complaint_subject', 'fellows_complaint']



class AssociatesComplaintForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ['associates_complaint_subject', 'associates_complaint']