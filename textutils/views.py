# I have created this file - Hussnain
from django.http import HttpResponse
from django.shortcuts import render

def analyze(request):
    # Get the text entered by the user
    djtext = request.POST.get("text", "default")

    # Check if user check the "Remove Punctuations" checkbox
    removepunc = request.POST.get("removepunc", "off")

    # Check if user check the "Uppercase All Letters" checkbox
    fullcaps = request.POST.get("fullcaps", "off")

    # Check if user check the "LowerCase All Letters" checkbox
    fullLowercase = request.POST.get("fullLowercase", "off")
    
    # Check if user check the "New Line Remove" checkbox
    newlineremover = request.POST.get("newlineremover", "off")
    
    # Check if user check the "Remove Extra Space" checkbox
    extraspaceremove = request.POST.get("extraspaceremove", "off")

    # Check if user check the "Character Counter" checkbox
    charcounter = request.POST.get("charcounter", "off")

    # Returns ERROR if textbox is empty
    if(djtext==''):
        return HttpResponse("ERROR: Please Enter Text to Analyze")

    # Check which checkbox is on by the user
    if(removepunc=="on"):
        punctuations = '''!()-[]\{};:'",<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {"purpose":"Remove Punctuations","analyzed_text":analyzed}
        djtext = analyzed

    if(fullcaps=='on'):
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
            
        params = {"purpose":"Uppercase all Letters","analyzed_text":analyzed}
        djtext = analyzed

    if(fullLowercase=='on'):
        analyzed = ""
        for char in djtext:
            analyzed += char.casefold()
            
        params = {"purpose":"LowerCase All Letters","analyzed_text":analyzed}
        djtext = analyzed


    if(newlineremover=='on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed += char
                
        params = {"purpose":"Remove Line Remover","analyzed_text":analyzed}
        djtext = analyzed
    
    if(extraspaceremove=='on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed += char
    
        params = {"purpose":"Extra Space Remove","analyzed_text":analyzed}
        djtext = analyzed
    
    if(charcounter=='on'):
        analyzed = djtext.__len__()
    
        params = {"purpose":"Character Counter","charcounter":"Characters: "+str(analyzed)+" Characters in your text", "analyzed_text":djtext}
        djtext = analyzed

    if(removepunc!='on' and charcounter!='on' and extraspaceremove!='on' and newlineremover!="on" and fullLowercase!="on" and fullcaps!="on"):
        return HttpResponse("ERROR: No function is selected.")

    return render(request, "analyze.html", params)



def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")


