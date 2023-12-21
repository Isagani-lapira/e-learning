from django.urls import path
from apps.accountapp import views


urlpatterns = [
    path('fullname',views.index)
]