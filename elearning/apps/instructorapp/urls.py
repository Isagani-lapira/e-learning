from django.urls import path
from apps.instructorapp import views

app_name = "instructorapp"
urlpatterns = [
    path('<str:username>/',views.dashboard, name="instructor_dashboard")
]