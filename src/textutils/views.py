#Self Created-Shishir

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def rempunc(request):
    return render(request, 'index.html')

def capfirst(request):
    return HttpResponse("Capitalize First")

def newlinerem(request):
    return HttpResponse("New LIne Remover")

def spacerem(request):
    return HttpResponse("Space Remover")

def charcount(request):
    return HttpResponse("Char Counter")
