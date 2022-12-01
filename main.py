from grid import coordinateGrid
startLat = 34.167282045937164
startLon = -119.03844158095751

latFt = startLat*3280.34
lonFt = startLon*3280.4

#Fill coordinateGrid with 100ft away from start location
coordinateGrid[0][0] = (latFt, lonFt)