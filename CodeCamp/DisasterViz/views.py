# Create your views here.
from django.http import *
from DisasterData import *
from django.shortcuts import render,render_to_response

def index(request):
    return render(request,'index.html',{})

def image(request):
    a = HttpResponse(open('Nepal_Zones.svg','r').read(),mimetype="image/svg+xml")
    return a

def genmap(request):
    a = gendisasterdata(genfunction_bydeaths)
    return HttpResponse(a,mimetype='image/svg+xml')




