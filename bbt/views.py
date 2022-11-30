from django.shortcuts import render, HttpResponse
from bbt.models import Contact
from datetime import datetime
from django.contrib import messages
from bbt.models import Register



# Create your views here.
def index(request):
    # context = {
    #     "variable1": "Harry is great",
    #     "variable2": "Rohan is great"
    # }
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")


def about(request):
    # return HttpResponse("this is homepage")
    return render(request, 'about.html')


def tournament(request):
    return render(request, 'tournament.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact= Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Form Submitted!')
    return render(request, 'contact.html')

def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        register = Register(email=email, password=password, address=address, address2=address2,city=city,state=state,zip=zip, date=datetime.today())
        register.save()
        messages.success(request, 'Registration Successfull!')
    return render(request,'register.html')
