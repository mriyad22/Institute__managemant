from django import forms
from .models import *
from accounts.models import AuthUserModel
from django.db import transaction


class StudentProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=200)
    email = forms.EmailField()

    class Meta:
        model = StudentModel
        fields = [
            "username",
            "email",
            "name",
            "roll",
            "address",
            "image",
            "phone"
        ]
        exclude = ["student"]

    @transaction.atomic
    def save(self, commit = True):
        user = AuthUserModel.objects.create_user(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["email"],
            password='123456',
            user_type="Student"

        )
        student = super().save(commit = False)
        student.student = user
        if commit:
            student.save()
        return student



#Student update form
class StudentProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = [
            "name",
            "roll",
            "address",
            "image",
            "phone"
        ]
        