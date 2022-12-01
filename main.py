from grid import coordinateGrid
startLat = 34.167282045937164
startLon = -119.03844158095751

latFt = startLat*3280.34
lonFt = startLon*3280.4

#Fill coordinateGrid with 100ft away from start location
coordinateGrid[0][0] = (latFt, lonFt)
lat = 0
lon = 0
inc = 0
while coordinateGrid[4][4] == 16:
    while lat < 5:
        coordinateGrid[lat][lon] = (latFt+inc, lonFt)
        lat = lat+1
        inc = inc+100
    lat = 0
    while lon < 5:
        coordinateGrid[lat][lon] = (latFt, lonFt+inc)
        lon = lon+1
        inc = inc+100
    lon = 0
        