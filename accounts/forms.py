from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import EmailValidator
from django.forms import ModelForm, fields
from django.contrib.auth import get_user_model
from django.forms.forms import Form
from django.http import request


from .models import Profile


class UserRegisterForm(UserCreationForm):
    class Meta:
        fields = ['first_name', 'last_name', 'username', 'email', 'password1']
        exclude = ['password2']
        model = User
    validators = [],
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'f-v-lc1',
            'placeholder': 'Firstname',
            'id': 'fullname'}),
        max_length=100, label='', required=False
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'f-v-lc1',
            'placeholder': 'Lastname',
            'id': 'fullname'}),
        max_length=100, label='', required=False
    )

    username = forms.CharField(
        validators=[],
        widget=forms.TextInput(attrs={
            'class': 'f-v-lc1',
            'placeholder': 'Username',
            'id': 'username'}), max_length=200, label='', required=False
    )

    email = forms.EmailField(
        validators=[],
        widget=forms.EmailInput(attrs={
            'class': 'f-v-lc1',
            'placeholder': 'Email',
            'id': 'email1'}), label='', required=False
    )

    password1 = forms.CharField(
        validators=[],
        widget=forms.PasswordInput(attrs={
            'class': 'f-v-lc1',
            'placeholder': 'Password',
            'id': 'password1',
            'name': 'password',
            'maxlength': '20'}), label='', required=False
    )

    password2 = forms.CharField(
        validators=[],
        widget=forms.PasswordInput(attrs={
            'class': 'f-v-lc1',
            'placeholder': 'Password',
            'id': 'password1',
            'name': 'password',
            'maxlength': '20'}), label='', required=False
    )


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]


class Profileform(forms.ModelForm):
    class Meta:
        fields = ['profileimg', 'bio', 'country', 'website',
                  'istagram', 'facebook', 'linkedin', 'twitter']
        model = Profile

    profileimg = forms.ImageField(
        validators=[],
        widget=forms.ClearableFileInput(attrs={
            'onchange': 'loadFile(event)',
            'name': 'profileimg'
        }), required=False
    )

    bio = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'imo-pan',
            'style': 'resize:none;',
            'rows': '15',
            'name': 'bio'
        }), required=False
    )

    country = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'imo-pan',
            'name': 'country',
        }), required=False
    )

    website = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'imo-pan',
            'name': 'website',
        }), required=False
    )

    istagram = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'imo-pan',
            'name': 'istagram',
        }), required=False
    )

    facebook = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'imo-pan',
            'name': 'facebook',
        }), required=False
    )

    linkedin = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'imo-pan',
            'name': 'linkedin',
        }), required=False
    )

    twitter = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'imo-pan',
            'name': 'twitter',
        }), required=False
    )
