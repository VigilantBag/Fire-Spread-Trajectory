import ast
import overpy
api = overpy.Overpass()

radius = 100
lat = 34.167282045937164
long = -119.03844158095751

natural = "null"

while(natural == "null"):
    result = api.query('[out:json];way[natural](around:{},{},{}); out;'.format(radius, lat, long))
    try:
        way = result.ways[1]
        natural = way.tags["natural"]
    except(IndexError):
        radius = radius+100
        print("new radius = {}".format(radius))
    
print(natural)