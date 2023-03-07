from django import forms

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control mb-3"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control mb-3"}))

    class Meta:
        model = User

