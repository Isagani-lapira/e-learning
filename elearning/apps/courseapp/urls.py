from django.urls import path
from apps.courseapp import views

# Create your views here.
app_name = "courseapp"
urlpatterns = [
    path('',views.index, name="course_url")
]