from django.db import models
from django.contrib.auth.models import User
from django.db import models

class AndroidApp(models.Model):
    name = models.CharField(max_length=255)
    package_name = models.CharField(max_length=255, unique=True)
    icon = models.ImageField(upload_to="app_icons/", blank=True, null=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Task(models.Model):
    app = models.ForeignKey(AndroidApp, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    screenshot = models.ImageField(upload_to='screenshots/', null=True, blank=True)

    def __str__(self):
        return f"Task for {self.user.username} on {self.app.name}"


def task():
    return None