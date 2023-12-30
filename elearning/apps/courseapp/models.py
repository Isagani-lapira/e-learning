from django.db import models
from apps.accountapp.models import *

# Create your models here.
class Course(models.Model):
    instructor = models.ForeignKey(Instructor,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    certificate = models.ImageField(null=False,blank=False,default='',upload_to="images/")
    date_created = models.DateTimeField(auto_now=True) #get current date time once it created
    
    
class Enrollment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now = True)
    is_finish = models.BooleanField(default = False)
    

class Module(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    title = models.CharField(blank=False, null=False, max_length = 150)
    description = models.TextField(blank=False, null=False)
    cover_img = models.ImageField(null=True, blank=True,upload_to="images/")
    
    
class Lesson(models.Model):
    module = models.ForeignKey(Module,on_delete=models.CASCADE)
    title = models.CharField(blank=False, null=False, max_length = 150)
    content = models.TextField(blank=False, null=False)
    cover_img = models.ImageField(null=True, blank=True,upload_to="images/")
    

class LessonAssets(models.Model):
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    asset = models.ImageField(null=False, blank=False,upload_to="images/")
    
class AdditionalResource(models.Model):
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    resource_name = models.CharField(max_length=150,null=True ,blank=True, default='')
    link = models.TextField(null=False,blank=False)
    
    
class StudentProgress(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    module = models.ForeignKey(Module,on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)