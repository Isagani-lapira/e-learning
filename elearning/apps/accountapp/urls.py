from django.urls import path
from apps.accountapp import views

app_name = "accountapp"
urlpatterns = [
    path('',views.login,name="login_url")
]