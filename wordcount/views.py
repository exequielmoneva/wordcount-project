from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return render(request,"home.html")

def count(request):
    fulltext=request.GET["fulltext"]
    wordList=fulltext.split()
    return render(request,"count.html",{"fulltext":fulltext,"count":len(wordList)})
def about(request):
    return render(request,"about.html")
