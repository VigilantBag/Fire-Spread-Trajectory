import overpy
import time
import Namedtuple
from collections import namedtuple

api = overpy.Overpass(url="https://fc77-209-129-115-56.ngrok.io/api/interpreter/", max_retry_count=20) #Change url as needed, but keep subdirectory /api/interpreter/

radius = 100 #meters
lat = 34.167282045937164
long = -119.03844158095751

ways = []

natural = "null"

searchtype = "natural"

wayData = namedtuple("wayData", ["natural", "landuse", "isBuilding"])

i = 0

while(i <= 20):
    result = api.query('[out:json];way[natural](around:{},{},{}); out;'.format(radius, lat, long))
    try:
        way = result.ways[i]
        #print(way.tags)
        natural = way.tags["natural"]
        ways[i] = Namedtuple.gridValues(way.tags["landcover"], way.tags["natural"], way.tags["landuse"], null, way.tags["*road*"], way.tags["building"], null, null )
        print(ways[i])
        i = i+1
    except(KeyError):
        radius = radius+100
        print("new radius = {}".format(radius))
        continue
    except(IndexError):
        radius = radius+100
        print("new radius = {}".format(radius))

    
print(natural)