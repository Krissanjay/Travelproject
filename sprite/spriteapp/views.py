from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Role
# Create your views here.
def demo(request):
    x=Place.objects.all()
    return render(request, "index.html", {'result': x})
def demo1(request):
    y = Role.objects.all()
    return render(request,"index.html",{'resul': y})
#def addition(request):
    #x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
    #res=x+y
    #return render(request,"result.html",{'result':res})