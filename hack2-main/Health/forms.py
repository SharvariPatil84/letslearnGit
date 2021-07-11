
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
 password1 = forms.CharField(label='Password')
 password2 = forms.CharField(label='Confirm Password(again)')
 class meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
