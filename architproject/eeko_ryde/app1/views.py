from django.shortcuts import render

# Create your views here.

from .models import *
from app1.form import *

def index(request):
    return render(request,'index.html')

def service(request):
    return render(request,'service.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
