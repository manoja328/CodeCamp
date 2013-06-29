# Create your views here.
from django.http import *
from DisasterData import *
from django.shortcuts import render,render_to_response
from DisasterData import disaster_set, district_set, year_set

def index(request):
    Response_string = ""
    error = ""
    success = ""
    if request.method == 'POST':
        Input_type = request.POST.get('input_type')
        print Input_type
        if Input_type == 'graph' or Input_type == "map":
            Year = request.POST.get('year')
            Response_string += "Year : " + Year + " "
            Disaster = request.POST.get('disaster')
            Response_string += "Disaster : " + Disaster+ " "
            District =  request.POST.get('district')
            Response_string += "District : " + District + " "
            Type = request.POST.get('type')
            Response_string += "CasualtyType : " + Type + " "
            if Input_type == "map":
                gendisasterdata(Year,Disaster,Type)
            elif Input_type == "graph":
                gendisastergraph(District,Disaster,Type)

        elif Input_type == 'entry':
            Disaster = request.POST.get('disaster')
            if not Disaster:
                error = True
            District = request.POST.get('district')
            if not District:
                error = True
            Source = request.POST.get('source')
            if not Source:
                error = True
            Date = request.POST.get('date')
            if not Date:
                error = True
            Deaths = request.POST.get('deaths')
            if not Deaths:
                error = True
            Injured = request.POST.get('injured')
            if not Injured:
                error = True
            Missing = request.POST.get('missing')
            if not Missing:
                error = True

            if error == True:
                error = "One or more values not present"
            else:
                success = "Value added successfully"

    #return render(request,'index.html',{'yearset':[],'disasterset':[],'typeset':("ALL","Deaths","Injured","Missing"),
    #                                    'districtset':[]})
    return render(request,'index.html',{'yearset':tuple(year_set),'disasterset':(disaster_set),'typeset':("Deaths","Injured","Missing"),
                                        'districtset':(district_set), "response_string":Response_string,"error_string":error,"success_string":success})

def image(request):
    a = HttpResponse(open('Nepal_Zones.svg','r').read(),mimetype="image/svg+xml")
    return a

def genmap(request):
    a = HttpResponse(open('NepalMap.svg','r').read(),mimetype="image/svg+xml")
    return a


def trend(request):
    return HttpResponse(open("fig.png","rb"),mimetype="image/png")

