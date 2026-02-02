# Create your views here.
from django.shortcuts import render

def about(request):
    return render(request, 'portfolio/about.html')
