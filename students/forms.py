from django import forms
from .models import *


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = "__all__"
        exclude = ["student"]