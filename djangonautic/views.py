from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse('home')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('about2')
    return render(request, 'about.html')
