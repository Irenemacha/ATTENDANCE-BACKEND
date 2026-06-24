from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    ROLE_CHOICES = (
        ('Student', 'Student'),
        ('Lecturer', 'Lecturer'),
        ('HOD', 'HOD'),
        ('Admin', 'Admin'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='Student'
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    is_verified = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.username
