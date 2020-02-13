#Self Created-Shishir

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    shishir={'Place':'Neptune','Age':'1000'}
    return render(request, 'index.html',shishir)

def rempunc(request):
    return render(request, 'removepunc.html')

def capfirst(request):
    return render(request, 'capitalfirst.html')

def newlinerem(request):
    return render(request, 'newlinere.html')

def spacerem(request):
    return render(request, 'spacerem.html')

def charcount(request):
    return render(request, 'charcout.html')

