from django.shortcuts import redirect, render, HttpResponse

def index(request):
    return HttpResponse("Course apps")