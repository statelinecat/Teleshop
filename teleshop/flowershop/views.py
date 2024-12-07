from django.shortcuts import render
from django.http import HttpResponse
#from .models import Flower


# Create your views here.

def index(request):
    return render(request, 'flowershop/index.html')


def contact(request):
    return render(request, 'flowershop/contact.html')


def catalog(request):
    #flowers = Flower.objects.all()
    return render(request, 'flowershop/catalog.html') #, {'flowers': flowers})




# Create your views here.
