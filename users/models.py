from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_imgs", default="default.jpg")
    bio = models.CharField(max_length=2000, default="Bio")
    git_url = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return f"{self.user.username} Profile"

    