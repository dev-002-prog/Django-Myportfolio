from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')

def intro(request):
    return render(request,'intro.html')

def service(request):
    return render(request,'service.html')

def media(request):
    return render(request,'media.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        enquiry=request.POST.get('enquiry')
        contact=Contact(name=name,email=email,phone=phone,enquiry=enquiry,date=datetime.today())
        contact.save()
    return render(request,'wcontact.html')

