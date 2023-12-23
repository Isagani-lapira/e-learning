from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #additional fields for user
    is_instructor = models.BooleanField(default=False)