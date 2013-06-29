__author__ = 'Pravesh'
import pickle
import re
import sys

from xml.etree import ElementTree as ET

disdata = pickle.load(open("data.txt","r"))
class ContinueError(Exception):
    pass


def genfunction_bydeaths(filters):
    a = {}
    sys.stdout = open("Output.txt","w")
    print "Hello world"
    for elements in disdata:
        try:

            for filtertext in filters:
                if not re.match(filters[filtertext],elements[filtertext]):
                    raise ContinueError
            if elements['district'] in a:
                a[elements['district']] += int(elements['deaths'])
            else:
                a[elements['district']] = int(elements['deaths'])
        except ContinueError:
            continue
    #print repr(a)
    return a

def gendisasterdata(generatorfunction,filtertext='deaths',filtervalue='.*'):
    a = generatorfunction({filtertext:filtervalue})
    return generatecolor(a)


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
    print maxvalue, minvalue
    maxR,maxG,maxB = (70.,20.,20.)
    minR,minG,minB = (255.,170.,170.)

    for i in range(5,80):
        element = root[i]
        a = element.attrib
        district = a['name'].title()
        if district in disaster:
            value = disaster[a['name'].title()]
            print a['name']
            print value
            col = constructcolor(minR-(minR-maxR)/(maxvalue-minvalue)*value,  minG-(minG-maxG)/(maxvalue-minvalue)*value,
                minB-(minB-maxB)/(maxvalue-minvalue)*value)
            print col
            a['fill'] = col
        else:
            a['fill'] = '#FFFFFF'

    return ET.tostring(root)
