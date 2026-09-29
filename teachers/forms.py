from django import forms
from .models import TeacherModel
from accounts.models import AuthUserModel
from django.db import transaction

class TeacherProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=200)
    email = forms.EmailField()

    class Meta:
        model = TeacherModel
        fields = [
            "username",
            "email",
            "name",
            "address",
            "image",
            "phone" 
        ]
        exclude = ["teacher"]

    @transaction.atomic
    def save(self, commit = True):
        user = AuthUserModel.objects.create_user(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["email"],
            password='123456',
            user_type = "Teacher"
        )
        
        teacher = super().save(commit = False)
        teacher.teacher = user
        if commit:
            teacher.save()
        return teacher




class TeacherProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = TeacherModel
        fields = [
            "name",
            "address",
            "image",
            "phone" 
        ]


    