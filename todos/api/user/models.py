from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.

class Test(models.Model):
    full_name = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name
    