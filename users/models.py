from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_imgs", default="default.jpg")

    class Meta:
        db_table = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return f"{self.user.username} Profile"

    