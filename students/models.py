from django.db import models
from teachers.models import BasicInfoModel
from accounts.models import AuthUserModel

# Create your models here.

class StudentModel(BasicInfoModel):
    roll = models.PositiveIntegerField(null=True)
    image = models.ImageField(upload_to="media/student_img")
    student = models.OneToOneField(
        AuthUserModel,
        on_delete=models.CASCADE,
        related_name="student_profile",
        null=True
    )

    def __str__(self):
        return f"{self.name}, --{self.roll}"