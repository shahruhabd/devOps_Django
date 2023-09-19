from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    gender = models.CharField(max_length=20)

    def __str__(self):
        return f"#{self.id} {self.email}"