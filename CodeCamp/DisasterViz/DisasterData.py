__author__ = 'Pravesh'
import pickle
import re
import sys
import matplotlib.pyplot as plot
from scipy.interpolate import interp1d
from numpy import linspace

from xml.etree import ElementTree as ET

disdata = pickle.load(open("data.txt","r"))
year_set = set()
disaster_set = set()
district_set = set()

for elements in disdata:
    if len(elements['date']) == 4:
        year_set.add(elements['date'][-4:])
    disaster_set.add(elements['disaster'])
    district_set.add(elements['district'])
year_set = sorted(tuple(year_set))
disaster_set = sorted(tuple(disaster_set))
district_set = sorted(tuple(district_set))


class ContinueError(Exception):
    pass


def genfunction_bycasualty(year,disaster,type):
    a = {}
    sys.stdout = open("Output.txt","w")
    #print "Hello world"
    #print year, disaster, type
    for elements in disdata:
        if elements['date'][-4:] == year or year == "ALL":
            if elements['disaster'] == disaster or disaster == 'ALL':
                if type.lower() =='deaths':
                    value = int(elements['deaths'])
                elif type.lower() == 'injured':
                    value = int(elements['injured'])
                elif type.lower() == 'missing':
                    value = int(elements['missing'])
                elif type == 'ALL':
                    value = int(elements['deaths']) + int(elements['injured']) + int(elements['missing'])

                if elements['district'] in a:
                    a[elements['district']] += value
                else:
                    a[elements['district']] = value
    return a

def genfunction_byyear(district,disaster,type):
    a = {}
    sys.stdout = open("Output.txt","w")
    print "Hello world"
    print disaster, disaster, type
    for elements in disdata:
        if elements['district'] == district or district == "ALL":
            if elements['disaster'] == disaster or disaster == 'ALL':
                if type.lower() =='deaths':
                    value = int(elements['deaths'])
                elif type.lower() == 'injured':
                    value = int(elements['injured'])
                elif type.lower() == 'missing':
                    value = int(elements['missing'])
                elif type == 'ALL':
                    value = int(elements['deaths']) + int(elements['injured']) + int(elements['missing'])
                if len(elements['date'][-4:]) ==4:
                    if elements['date'][-4:] in a:
                        a[elements['date'][-4:]] += value
                    else:
                        a[elements['date'][-4:]] = value
    return a

def gendisasterdata(year='ALL',disaster='ALL',type='ALL'):
    a = genfunction_bycasualty(year,disaster,type)
    generatecolor(a)


def constructcolor(r,g,b):
    print r,g,b
    r,g,b = int(r),int(g),int(b)
    print r,g,b
    r = hex(r)[2:]
    g = hex(g)[2:]
    b = hex(b)[2:]
    if len(r) == 1:
        r = "0"+r
    if len(g) == 1:
        g = "0"+g
    if len(b) == 1:
        b = "0"+b

    return '#%s%s%s'%(r,g,b)

def generatecolor(disaster):
    tree = ET.parse('Nepal_Zones.svg')
    root = tree.getroot()
    values = disaster.values()
    maxvalue = max(values)
    minvalue = min(values)
    #print maxvalue, minvalue
    maxR,maxG,maxB = (70.,20.,20.)
    minR,minG,minB = (255.,170.,170.)

    for i in range(5,80):
        element = root[i]
        a = element.attrib
        district = a['name'].title()
        if district in disaster:
            value = disaster[a['name'].title()]
            #print a['name']
            #print value
            col = constructcolor(minR-(minR-maxR)/(maxvalue-minvalue)*value,  minG-(minG-maxG)/(maxvalue-minvalue)*value,
                minB-(minB-maxB)/(maxvalue-minvalue)*value)
            print col
            a['fill'] = col
        else:
            a['fill'] = '#FFFFFF'

    open('NepalMap.svg',"w").write(ET.tostring(root))

def gendisastergraph(District="ALL",Disaster="ALL",Type="ALL"):
    a = genfunction_byyear(District,Disaster,Type)
    print a
    generatetrend(a)

def generatetrend(disaster):
    """
        This disaster is a dictionary consisting of years and the data
    """
    f = plot.figure()
    sp = f.add_subplot(111)
    items_count = len(disaster)

    keys = sorted(disaster.keys())
    values = [disaster[i] for i in keys]

    x = [i for i in range(items_count)]
    interpolate = interp1d(x,values,kind='linear')
    newx = linspace(0,len(disaster)-1,300)
    sp.set_xticks(x)
    sp.set_xticklabels(keys)
    sp.plot(newx,interpolate(newx))
    f.savefig("fig.png")
    pass
