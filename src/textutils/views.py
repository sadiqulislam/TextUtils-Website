# Self Created-Shishir

from django.http import HttpResponse
from django.shortcuts import render
import string


def index(request):
    return render(request, 'index.html')


def analyze(request):
    #Get The Text:
    djtext = request.GET.get('text', 'default')
    removepunctuation = request.GET.get('removepunctuation', 'default')
    print(removepunctuation)
    print(djtext)

    # Analyze The Text"
    if removepunctuation== "on":
        punctuations = string.punctuation
        analyze = ""
        for char in djtext:
            if char not in punctuations:
                analyze = analyze + char

        params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyze}
        #return HttpResponse('rempunc')
        return render(request, 'analyzer.html', params)

    else:
        return HttpResponse("Error")

#
# def rempunc(request):
#     # print(request.GET.get('text','default')) #Not Working
#
#     # Get The Text:
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     # Analyze The Text"
#
#     return HttpResponse('rempunc')
#     #return render(request, 'removepunc.html')
#
#
# def capfirst(request):
#     return render(request, 'capitalfirst.html')
#
#
# def newlinerem(request):
#     return render(request, 'newlinere.html')
#
#
# def spacerem(request):
#     return render(request, 'spacerem.html')
#
#
# def charcount(request):
#     return render(request, 'charcout.html')
