from django.shortcuts import render
from .models import Projects

def home(request):
    projects = Projects.objects.all()

    return render(request,'home/index.html',{'projects':projects})
