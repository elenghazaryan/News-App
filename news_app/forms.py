from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserForm(UserCreationForm):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Your email', max_length=100)

    class Meta:
        model = User
        fields = ("name", "email")
