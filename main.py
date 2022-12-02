from grid import coordinateGrid
from osmCheckNearbyForData import osm
startLat = 34.167282045937164
startLon = -119.03844158095751

latFt = startLat*111.1111111111111*3280.34
lonFt = startLon*111.1111111111111*3280.4

#Fill coordinateGrid with 100ft away from start location
coordinateGrid[0][0] = (latFt, lonFt)
lat = 0
lon = 0
inc = 0
counter = 0
while coordinateGrid[3][3] == 16:
    wlat = lat
    while lat < 5:
        coordinateGrid[lat][lon] = (latFt+inc, lonFt)
        coordinatePairs = coordinateGrid[lat][lon]
        (latitude, longitude) = coordinatePairs
        latfttoCoord = latitude/3280.34/111.1111111111111
        lonfttoCoord = longitude/3280.34/111.1111111111111
        osm(latfttoCoord, lonfttoCoord)
        wlat = wlat+1
        coordinateGrid[lat][lon] = (latFt, lonFt-inc)
        coordinatePairs = coordinateGrid[lat][lon]
        (latitude, longitude) = coordinatePairs
        latfttoCoord = latitude/3280.34/(10,000/90)
        lonfttoCoord = longitude/3280.34/(10,000/90)
        osm(latfttoCoord, lonfttoCoord)
        lon = lon+1
        inc = inc+100

    lat = 0
    #infinite loop as lat and lon keep being set to 0 everytime while runs again. Need to fix
    """while lon < 5:
        coordinateGrid[lat][lon] = (latFt, lonFt-inc)
        coordinatePairs = coordinateGrid[lat][lon]
        (latitude, longitude) = coordinatePairs
        latfttoCoord = latitude/3280.34/(10,000/90)
        lonfttoCoord = longitude/3280.34/(10,000/90)
        osm(latfttoCoord, lonfttoCoord)
        lon = lon+1
        inc = inc+100
        
    lon = 0
    counter += 1
    """
    if (counter == 15):
        break

        
