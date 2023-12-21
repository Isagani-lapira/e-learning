from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path
from apps.accountapp import urls as account_url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: render(request, 'base.html'), name='empty_url'),
    path("__reload__/", include("django_browser_reload.urls")),
    path('account/', include(account_url)),
]
