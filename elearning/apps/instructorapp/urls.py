from django.urls import path
from apps.instructorapp import views

app_name = "instructorapp"
urlpatterns = [
    path('',views.dashboard, name="instructor_dashboard")
]