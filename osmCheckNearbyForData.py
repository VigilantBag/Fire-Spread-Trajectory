import overpy
import time
import Namedtuple

api = overpy.Overpass(url="https://e789-209-129-115-55.ngrok.io/api/interpreter/", max_retry_count=20) #Change url as needed, but keep subdirectory /api/interpreter/

radius = 100 #meters
lat = 34.167282045937164
long = -119.03844158095751

ways = []

natural = "null"
landuse = "null"
searchtype = "natural"


i = 1

while(i <= 2):
    result = api.query('[out:json];way["natural"](around:900,34.167282045937164,-119.03844158095751); out;')
    try:
        way = result.ways[0]
        #print(way.tags)
        try:
            natural = way.tags["natural"]
            ways.append(Namedtuple.gridValues("null", way.tags["natural"], "null", "null", "null", "null", "null", "null")) 
        except(KeyError):
            try:
                landuse = way.tags["landuse"]
                ways.append(Namedtuple.gridValues("null", "null", way.tags["landuse"], "null", "null", "null", "null", "null"))
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
for i in range(len(ways)):
    print(ways[i])
    
print(natural)
print(landuse)