# Create your views here.
from django.shortcuts import render

def about(request):
    return render(request, 'portfolio/about.html')
def home(request):
    return render(request, 'portfolio/home.html')
def services(request):
    return render(request, 'portfolio/services.html')