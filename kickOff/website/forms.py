from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from .models import *


class AddPlayerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['club'].empty_label = "Not Selected"

    class Meta:
        model = Players
        fields = ['fullName', 'slug', 'about', 'photo', 'is_published', 'club']
        widgets = {
            'fullName':forms.TextInput(attrs={'class': 'form-control'}),
            'about':forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'form-control'})
        }

    def clean_fullName(self):
        fullName = self.cleaned_data['fullName']
        if len(fullName) > 200:
            raise ValidationError('Len of name over 200 symbols')

        return fullName


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='User name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='User name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ContactForm(forms.Form):
    name = forms.CharField(label='User name', max_length=255)#widget=forms.TextInput(attrs={'class': 'form-control'})
    email = forms.EmailField(label='Email')#, widget=forms.EmailInput(attrs={'class': 'form-control'})
    content = forms.CharField(label='Content', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10 ,'class': 'form-control'}))
