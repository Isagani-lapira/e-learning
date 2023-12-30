from django.db import models
from apps.accountapp.models import *

# Create your models here.
class Course(models.Model):
    instructor = models.ForeignKey(Instructor,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    certificate = models.ImageField(null=True,blank=True,upload_to="images/")
    date_created = models.DateTimeField(auto_now=True) #get current date time once it created