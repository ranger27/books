from django.shortcuts import render
from django.http import HttpResponse
from .models import Author,Book

# Create your views here.
def  index(request):
    b = Book.objects.all()
    context = {"list": b}
    return render(request,'books/index.html',context)

def detail(request,id):
    b = Book.objects.filter(pk=id)
    context = {"book":[]}
    if b:
        b = b[0]
        context = {"book":b}  
    return render(request,'books/detail.html',context)
        