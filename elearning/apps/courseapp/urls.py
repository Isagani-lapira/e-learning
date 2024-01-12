from django.urls import path
from apps.courseapp import views

# Create your views here.
app_name = "courseapp"
urlpatterns = [
    path('',views.index, name="course_url"),
    path('delete_course/<int:course_id>/', views.DeleteCourse,name="delete_url"),
    path('addmodule/<int:id>/',views.AddModule,name="AddModule_url"),
    path('deletemodule/<int:id>/',views.deleteModule, name="DelModule_url"),
    path('deletelesson/<int:id>/',views.deleteLesson, name="DelLesson_url"),
]