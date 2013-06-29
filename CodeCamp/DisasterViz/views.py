# Create your views here.
from django.http import *
from DisasterData import *


def index(request):
    return HttpResponse('<img src="Nepal_Zones.svg"></img>')

def image(request):
    a = HttpResponse(open('Nepal_Zones.svg','r').read(),mimetype="image/svg+xml")
    return a

def genmap(request):
    a = gendisasterdata(genfunction_bydeaths)
    #return HttpResponse(a,mimetype='image/svg+xml')
    return HttpResponse(repr(a))



