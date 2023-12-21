from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    template = "profile.html"
    context = {
        "name": "Isagani lapira Jr",
    }
    return render(request,template,context)