#Self Created-Shishir

from django.http import HttpResponse

def index(req):
    return HttpResponse("Hello World")


def about(req):
    return HttpResponse("About World")