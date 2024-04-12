from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib.messages import constants as messages
# Create your views here.
def index(request):
    return render(request , 'index.html')

def about(request):
     return render(request , 'about.html')

def contact(request):
     if request.method == "POST":
          name=request.POST.get('name')
          password=request.POST.get('password')
          email=request.POST.get('email')
          phone=request.POST.get('phone')
          contact= Contact(name=name,password=password,email=email,phone=phone,date= datetime.today())
          contact.save()
          
     return render(request , 'contact.html')