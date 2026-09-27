from django import forms
from .models import TeacherModel

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherModel
        fields = "__all__"
        exclude = ["teacher"]