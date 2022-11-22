import overpy
import time
import Namedtuple
from collections import namedtuple

api = overpy.Overpass(url="https://4d0e-209-129-115-55.ngrok.io/api/interpreter/", max_retry_count=20) #Change url as needed, but keep subdirectory /api/interpreter/

radius = 100 #meters
lat = 34.167282045937164
long = -119.03844158095751

ways = []

natural = "null"
landuse = "null"
searchtype = "natural"

wayData = namedtuple("wayData", ["natural", "landuse", "isBuilding"])

i = 1

while(i <= 2):
    result = api.query('[out:json];way["natural"](around:{0},{1},{2});way["landuse"](around:{0},{1},{2}); out;'.format(radius, lat, long))
    try:
        way = result.ways[0]
        #print(way.tags)
        try:
            natural = way.tags["natural"]
            ways[i] = Namedtuple.gridValues("null", way.tags["natural"], "null", "null", "null", "null", "null", "null")
        except(KeyError):
            try:
                landuse = way.tags["landuse"]
                ways[i] = Namedtuple.gridValues("null", "null", way.tags["landuse"], "null", "null", "null", "null", "null")
            except(KeyError):
                print(ways[i])
                i = i+1
    except(KeyError):
        radius = radius+100
        print("new radius = {}".format(radius))
        continue
    except(IndexError):
        radius = radius+100
        print("INDEX new radius = {}".format(radius))

    
print(natural)
print(landuse)