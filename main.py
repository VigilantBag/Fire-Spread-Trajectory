from grid import coordinateGrid
from osmCheckNearbyForData import osm
from WeightCalculation import calcWeight
from Namedtuple import gridValues
startLat = 34.167282045937164
startLon = -119.03844158095751

latFt = startLat*111.1111111111111*3280.34
lonFt = startLon*111.1111111111111*3280.4

#Fill coordinateGrid with 100ft away from start location
coordinateGrid[0][0] = (latFt, lonFt)
lat = 0
lon = 0
inc = 0
dictPointer = 0
counter = 0
while lon <= 3:
    coordinateGrid[0][lon] = (latFt, lonFt-inc)
    coordinatePairs = coordinateGrid[lat][lon]
    latitude, longitude = coordinatePairs
    latfttoCoord = latitude/3280.34/111.1111111111111
    lonfttoCoord = longitude/3280.34/111.1111111111111
    osm(latfttoCoord, lonfttoCoord, dictPointer)
    dictPointer = dictPointer + 1
    lon = lon+1
    inc = inc+1000
inc = 0
lon = 0
while lon <= 3:
    coordinateGrid[1][lon] = (latFt+inc, lonFt-inc)
    coordinatePairs = coordinateGrid[lat][lon]
    latitude, longitude = coordinatePairs
    latfttoCoord = latitude/3280.34/111.1111111111111
    lonfttoCoord = longitude/3280.34/111.1111111111111
    osm(latfttoCoord, lonfttoCoord, dictPointer)
    dictPointer = dictPointer + 1
    lon = lon+1
    inc = inc+1000
lon = 0
inc = 0
while lon <= 3:
    coordinateGrid[2][lon] = (latFt+inc, lonFt-inc)
    coordinatePairs = coordinateGrid[lat][lon]
    latitude, longitude = coordinatePairs
    latfttoCoord = latitude/3280.34/111.1111111111111
    lonfttoCoord = longitude/3280.34/111.1111111111111
    osm(latfttoCoord, lonfttoCoord, dictPointer)
    dictPointer = dictPointer + 1
    lon = lon+1
    inc = inc+1000
lon = 0
inc = 0
while lon <= 3:
    coordinateGrid[3][lon] = (latFt+inc, lonFt-inc)
    coordinatePairs = coordinateGrid[lat][lon]
    latitude, longitude = coordinatePairs
    latfttoCoord = latitude/3280.34/111.1111111111111
    lonfttoCoord = longitude/3280.34/111.1111111111111
    osm(latfttoCoord, lonfttoCoord, dictPointer)
    dictPointer = dictPointer + 1
    lon = lon+1
    inc = inc+1000
lon = 0
inc = 0
lat = 0
calcWeight()
    #infinite loop as lat and lon keep being set to 0 everytime while runs again. Need to fix
"""while lon < 5:
    coordinateGrid[lat][lon] = (latFt, lonFt-inc)
    coordinatePairs = coordinateGrid[lat][lon]
    latitude, longitude = coordinatePairs
    latfttoCoord = latitude/3280.34/111.1111111111111
    lonfttoCoord = longitude/3280.34/111.1111111111111
    osm(latfttoCoord, lonfttoCoord)
    lon = lon+1
    inc = inc+1000
    
lon = 0
counter += 1
"""
print(coordinateGrid)
print(gridValues)

        
