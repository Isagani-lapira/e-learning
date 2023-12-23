from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #additional fields for user
    is_instructor = models.BooleanField(default=False)
    
    
class Instructor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    instructor_description = models.TextField(blank=True, default='')
    profile_img = models.ImageField(null=True, blank=True, upload_to="images/") #default image location