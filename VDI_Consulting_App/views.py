from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    context = {
    "time": strftime("%b %d, %Y  %H:%M %p", gmtime())
    }
    return render(request, "index.html", context)

def services(request):
    context = {
    "time": strftime("%b %d, %Y  %H:%M %p", gmtime())
    }
    return render(request, "services.html", context)

def aboutus(request):
    context = {
    "time": strftime("%b %d, %Y  %H:%M %p", gmtime())
    }
    return render(request, "aboutus.html", context)

def contactus(request):
    context = {
    "time": strftime("%b %d, %Y  %H:%M %p", gmtime())
    }
    return render(request, "contactus.html", context)


