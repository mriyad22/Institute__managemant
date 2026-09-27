from django.db import models
from accounts.models import AuthUserModel
# Create your models here.


class BasicInfoModel(models.Model):
    name = models.CharField(max_length=255, null=True)
    address = models.TextField()
    phone = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.address}"


class TeacherModel(BasicInfoModel):
    image = models.ImageField(upload_to="media/teacher_img", null=True)
    teacher = models.OneToOneField(
        AuthUserModel,
        on_delete=models.CASCADE,
        related_name="teacher_profile",
        null=True
    )

    def __str__(self):
        return f"{self.name}"