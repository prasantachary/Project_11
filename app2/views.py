from django.shortcuts import render

# Create your views here.

def mylife(request):
    return render(request,'my life.html')

def kanha(request):
    return render(request,'kanha.html')