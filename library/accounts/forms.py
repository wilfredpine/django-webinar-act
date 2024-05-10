from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
                attrs={'class': 'form-control form-control-sm'}
            )
        )
    last_name = forms.CharField(
        widget=forms.TextInput(
                attrs={'class': 'form-control form-control-sm'}
            )
        )
    email = forms.EmailField(
        widget=forms.EmailInput(
                attrs={'class': 'form-control form-control-sm'}
            )
    )
    username = forms.CharField(
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        min_length=1,
        max_length=25,
        widget=forms.TextInput(
                attrs={'class': 'form-control form-control-sm'}
            )
        )
    password1 = forms.CharField(
        help_text='Your password can’t be too similar to your other personal information. Must contain at least 8 characters. Can’t be a commonly used password. Can’t be entirely numeric.',
        label='Password',
        min_length=8,
        max_length=30,
        widget=forms.PasswordInput(
                attrs={ 'class': 'form-control form-control-sm'}
            )
        )
    password2 = forms.CharField(
        help_text='Enter the same password as before, for verification.',
        label='Confirm Password',
        min_length=8,
        max_length=30,
        widget=forms.PasswordInput(
                attrs={ 'class': 'form-control form-control-sm'}
            )
        )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        min_length=1,
        max_length=25,
        widget=forms.TextInput(
                attrs={'class': 'form-control form-control-sm'}
            )
        )
    password = forms.CharField(
        label='Password',
        min_length=8,
        max_length=30,
        widget=forms.PasswordInput(
                attrs={ 'class': 'form-control form-control-sm'}
            )
        )