from django.shortcuts import render
from My_web.models import Contact
from datetime import datetime

# Create your views here.

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        desc = request.POST.get('desc')
        contact =  Contact(name=name, email= email, subject= subject, desc=desc, pub_date= datetime.today())
        contact.save()

    return render(request, 'index.html')

def projects(request):
    return render(request, 'Projects.html')

def base(request):
    return render(request, 'base.html')

