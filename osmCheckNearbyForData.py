import overpy
import time

api = overpy.Overpass(url="https://7be2-209-129-115-56.ngrok.io/api/interpreter/") #Change url as needed, but keep subdirectory /api/interpreter/

radius = 100 #meters
lat = 34.167282045937164
long = -119.03844158095751

natural = "null"

while(natural == "null"):
    result = api.query('[out:json];way[natural](around:{},{},{}); out;'.format(radius, lat, long))
    try:
        way = result.ways[1]
        natural = way.tags["natural"]
    except(IndexError):
        radius = radius+10
        print("new radius = {}".format(radius))
    except(overpy.exception.OverpassTooManyRequests):
        time.sleep(1000)
    
print(natural)