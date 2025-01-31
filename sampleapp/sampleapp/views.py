# I have created this file 
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Home")
    # params = {'name':'Anish', 'place':'Mars'}
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    # check with checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')


    # print(djtext)
    # print(removepunc)
    # print(fullcaps)
    
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:    
                analyzed = analyzed + char
        params = {'purpose':'Remove Punctuation', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    elif fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Change to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char.upper()
        params = {'purpose':'Remove New Line', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char.upper()
        params = {'purpose':'Remove New Line', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")


# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("capitalize first")


# def spaceremove(request):
#     return HttpResponse("space remover")

# def charcount(request):
#     return HttpResponse("charcount ")
