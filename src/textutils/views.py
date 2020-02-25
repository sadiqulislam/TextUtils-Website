# Self Created-Shishir

from django.http import HttpResponse
from django.shortcuts import render
import string


def index(request):
    return render(request, 'index.html')


def analyze(request):
    #  Get The Text:
    djtext = request.GET.get('text', 'default')

    # CheckBox Values:
    removepunctuation = request.GET.get('removepunctuation', 'off')
    caps = request.GET.get('caps','off')
    newlineremover = request.GET.get('newlineremover', 'off')
    # print(removepunctuation)
    # print(djtext)

    # Analyze The Text"
    if removepunctuation== "on":
        punctuations = string.punctuation
        analyze = ""
        for char in djtext:
            if char not in punctuations:
                analyze = analyze + char

        params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyze}
        # return HttpResponse('rempunc')
        return render(request, 'analyzer.html', params)

    elif(caps== "on"):
        analyze= ""

        for char in djtext:
            analyze = analyze + char.upper()

        params = {'purpose': 'All Uppercase', 'analyzed_text': analyze}
        # return HttpResponse('rempunc')
        return render(request, 'analyzer.html', params)

    elif(newlineremover == "on"):

        analyze=""

        for char in djtext:
            if char != "\n":
                analyze = analyze + char

        params = {'purpose':"New Line Removed",'analyzed_text':analyze}
        return render(request,'analyzer.html', params)

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
#   def capfirst(request):
#
#       if capfirst == 'on':
#
#           djtext=request.GET.get('text','default')
#
#           capitfirst = ""
#
#           for char in djtext:
#               if
#
#           pms = {'purpose2':"Capital First Letter","cap-first":capfirst}
#
#           return render(request, 'capitalfirst.html',pms)
#
#       else:
#             return HttpResponse("Error")
# #
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
