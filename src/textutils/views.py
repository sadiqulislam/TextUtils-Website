#Self Created-Shishir

from django.http import HttpResponse

def index(request):
    return HttpResponse("Home")

def rempunc(request):
    return HttpResponse("Remove Punctuation")

def capfirst(request):
    return HttpResponse("Capitalize First")

def newlinerem(request):
    return HttpResponse("New LIne Remover")

def spacerem(request):
    return HttpResponse("Space Remover")

def charcount(request):
    return HttpResponse("Char Counter")
