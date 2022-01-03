from django.shortcuts import render
from .models import About, Contact

# Create your views here.

def home(request):
    return render(request, 'core/index.html')

def about(request):
    obj = About.objects.first()
    return render(request, 'core/about.html', {'obj': obj})


def contact(request):
    obj = Contact.objects.first()
    return render(request, 'core/contact.html',  {'obj': obj})