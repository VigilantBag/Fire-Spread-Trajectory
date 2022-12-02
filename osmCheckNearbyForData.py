import overpy
import time
from Namedtuple import gridValues, dictPointer

api = overpy.Overpass(url="https://firespreadtrajectoryosm.loca.lt/api/interpreter/", max_retry_count=20) #Change url as needed, but keep subdirectory /api/interpreter/

radius = 100 #meters
lat = 34.167282045937164
long = -119.03844158095751


queryList = ["natural", "landuse"]
natural = "null"
landuse = "null"
searchtype = "natural"
indexer = 0
incradius = False

def osm(lat, long):
    api = overpy.Overpass(url="https://firespreadtrajectoryosm.loca.lt/api/interpreter/", max_retry_count=20) #Change url as needed, but keep subdirectory /api/interpreter/
    queryList = ["natural", "landuse"]
    indexer = 0
    radius = 100 #meters
    try:
        gridValues.append({"groundCover": 'null', "natural":'null', "landuse": 'null', "ele": 0, "isRoad": "False", "isBuilding": False, "isHouse": False, "foliageType": 'null'})
        while indexer <= len(queryList):
            result = api.query('[out:json];way[{3}](around:{0},{1},{2}); out;'.format(radius, lat, long, queryList[indexer]))
            wloop = 0
            try:
                way = result.ways[0]
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
                radius = radius+100
                print("KEY new radius = {}".format(radius))
                
            except(IndexError):
                radius = radius+100
                print("INDEX new radius = {}".format(radius))
            
    except(IndexError):
        print(gridValues[dictPointer])
osm(lat, long)