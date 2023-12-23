import random
import string
from arrow import now
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #additional fields for user
    is_instructor = models.BooleanField(default=False)
    
    
class Instructor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    instructor_description = models.TextField(blank=True, default='')
    profile_img = models.ImageField(null=True, blank=True, upload_to="images/") #default image location
    
    
class Course(models.Model):
    instructor = models.ForeignKey(Instructor,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    certificate = models.ImageField(null=True,blank=True,upload_to="images/")
    date_created = models.DateTimeField(auto_now=True) #get current date time once it created
    
class Student(models.Model):
    #get random characters
    def RandomStudentNo():
        CHARACTER_LENGTH = 25
        letters = string.ascii_uppercase
        result_str = ''.join(random.choice(letters) for i in range(CHARACTER_LENGTH))
        return result_str
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    #set up new primary key
    student_no_value = f"{RandomStudentNo()}{random.randint(0,1000)}"
    student_no = models.CharField(max_length = 30, primary_key=True, default=student_no_value)
    
    