from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    fullName = models.CharField(max_length=50, default='Anonymous')
    email = models.CharField(max_length=150)


    REQUIRED_FIELDS = []

    userName = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # def __str__(self):
    #     return self.email