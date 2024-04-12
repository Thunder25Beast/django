from django.shortcuts import render, HttpResponse

from home.models import Contact

# Create your views here.
def index(request):
    context = {
        "variable": "this is sent"

    }
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
   return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contact(name=name,password=password,email=email,phone=phone,)
        contact.save()
    return render(request, 'contact.html')



