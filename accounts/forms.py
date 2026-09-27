from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = AuthUserModel
        fields = [
            "username",
            "email",
            "user_type",
            "password1",
            "password2"
        ]