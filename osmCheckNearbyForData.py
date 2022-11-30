import overpy
import time
from Namedtuple import gridValues, dictPointer

api = overpy.Overpass(url="https://e789-209-129-115-55.ngrok.io/api/interpreter/", max_retry_count=20) #Change url as needed, but keep subdirectory /api/interpreter/

radius = 100 #meters
lat = 34.167282045937164
long = -119.03844158095751


queryList = ["natural", "landuse", "ele"]
natural = "null"
landuse = "null"
searchtype = "natural"


while(gridValues[dictPointer]["natural"] == "none") | (gridValues[dictPointer]["landuse"] == "none") | (gridValues[dictPointer]["ele"] == 0):
    result = api.query('[out:json];way["natural"](around:{0},{1},{2}); way["landuse"](around: {0},{1},{2}); way["ele"](around: {0},{1},{2});out;'.format(radius, lat, long))
    try:
        way = result.ways[0]
        gridValues.append({"groundCover": 'null', "natural":'null', "landuse": 'null', "ele": 0, "isRoad": "False", "isBuilding": False, "isHouse": False, "foliageType": 'null'})
        #print(way.tags)
        for j in range(len(queryList)):
            
            try:
                natural = way.tags[j]
                gridValues[dictPointer][j]
            except(KeyError):
                print("KE")

    except(KeyError):
        radius = radius+100
        print("new radius = {}".format(radius))
        continue
    except(IndexError):
        radius = radius+100
        print("INDEX new radius = {}".format(radius))

print(gridValues)
    
print(natural)
print(landuse)