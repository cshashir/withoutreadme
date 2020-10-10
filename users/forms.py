from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


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
        fields = ['first_name', 'last_name','company_name', 'company_profile', 'phone']


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
        fields = ['first_name', 'last_name','date_of_birth', 'max_qualification','ssc_score', 'phone', 'aadhaar', 'associate_bio', 'work_ex']


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
