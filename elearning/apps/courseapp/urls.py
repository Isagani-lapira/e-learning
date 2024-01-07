from django.urls import path
from apps.courseapp import views

# Create your views here.
app_name = "courseapp"
urlpatterns = [
    path('',views.index, name="course_url"),
    path('delete_course/<int:course_id>/', views.DeleteCourse,name="delete_url"),
    path('course_info/',views.CourseInfo, name="courseInfo_url"),
]