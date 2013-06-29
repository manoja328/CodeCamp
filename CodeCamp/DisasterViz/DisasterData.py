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
    return a

def gendisasterdata(generatorfunction,filtertext='deaths',filtervalue='.*'):
    a = generatorfunction({filtertext:filtervalue})
    return generatecolor(a)

def generatecolor(disaster):
    tree = ET.parse('Nepal_Zones.svg')
    root = tree.getroot()
    values = disaster.values()
    maxval = values.max()
    minval = values.min()
    maxR,maxG,maxB = (70,20,20)
    minR,minG,minB = (255,170,170)
    for i in range(5,80):
        element = root[i]
        #elements.atrrib['fill'] = '#FF0000'
        a = element.attrib
        a['fill'] = '#FFAAAA'
    tree.write("Map.svg")
