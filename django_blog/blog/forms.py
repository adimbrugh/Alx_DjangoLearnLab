

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms


class CustomUserCreationForm(UserChangeForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']