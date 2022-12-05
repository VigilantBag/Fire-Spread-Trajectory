import overpy
import time
from Namedtuple import gridValues, dictPointer

api = overpy.Overpass(url="https://firespreadtrajectoryosm.loca.lt/api/interpreter/", max_retry_count=20) #Change url as needed, but keep subdirectory /api/interpreter/

radius = 0 #meters
lat = 34.167282045937164
long = -119.03844158095751

queryList = ["natural", "landuse"]
natural = "null"
landuse = "null"
searchtype = "natural"
indexer = 0
incradius = False

def osm(lat, long, dictPointer):
    api = overpy.Overpass(url="http://bore.pub:40841/api/interpreter/", max_retry_count=20) #Change url as needed, but keep subdirectory /api/interpreter/
    queryList = ["natural", "landuse"]
    indexer = 0
    radius = 0 #meters
    try:
        gridValues.append({"groundCover": 'null', "natural":'null', "landuse": 'null', "ele": 0, "isRoad": "False", "isBuilding": False, "isHouse": False, "foliageType": 'null'})
        while gridValues[dictPointer]["natural"] == 'null' and radius <= 1000:
            result = api.query('[out:json];way[{3}](around:{0},{1},{2});relation[{3}](around:{0},{1},{2}); out;'.format(radius, lat, long, "natural"))
            wloop = 0
            try:
                way = result.relations[0]
                #print(way.tags)
                while wloop < len(queryList):
                    
                    try:
                        gridValues[dictPointer][queryList[indexer]] = way.tags[queryList[wloop]]
                        
                        wloop = wloop+1 #Inc to next data
                        
                    except(KeyError):
                        print("KE")
                        wloop = wloop+1
                indexer = indexer+1
                print("Finish filling dict")
                

            
            except(KeyError):
                radius = radius+10
                print("KEY new radius = {}".format(radius))
                
            except(IndexError):
                try:
                    way = result.ways[0]
                except(IndexError):
                    radius = radius+10
                    print("INDEX new radius = {}".format(radius))
            
    except(IndexError):
        print(gridValues[dictPointer])
