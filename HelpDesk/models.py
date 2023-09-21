from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    gender = models.CharField(max_length=20)

    def __str__(self):
        return f"#{self.id} {self.email}"
    
class Request(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    PRIORITY_CHOICES = [
        (LOW, 'Низкий'),
        (MEDIUM, 'Средний'),
        (HIGH, 'Высокий'),
    ]
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default=MEDIUM,
    )

    NEW = "NEW"
    INPROGRESS = "IN PROGRESS"
    RESOLVED = "RESOLVED"
    STATUS_CHOICES = [
        (NEW, 'new'),
        (INPROGRESS, 'in progress'),
        (RESOLVED, 'resolved'),
    ]
    status = models.CharField(
        max_length=11,
        choices=STATUS_CHOICES,
        default=NEW
    )

    def __str__(self):
        return f'{self.id}, {self.name}, {self.status}'



