# I have created this file 
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Home")
    # params = {'name':'Anish', 'place':'Mars'}
    return render(request, 'index.html')

def removepunc(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    print(djtext)
    # Analyze the text
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("capitalize first")


def spaceremove(request):
    return HttpResponse("space remover")

def charcount(request):
    return HttpResponse("charcount ")
