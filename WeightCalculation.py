from Namedtuple import gridValues,dictPointer
from grid import weightedGrid

dictPointer = 0


def calcWeight():
    if dictPointer < 4:
        gridRow = 0
    elif dictPointer > 4 < 8:
        gridRow = 1
    elif dictPointer > 8 < 12:
        gridRow = 2
    elif dictPointer > 12:
        gridRow = 3


    i = 0
    while i < len(gridValues[dictPointer]) - 4:
        print("i = ", i)
        match gridValues[dictPointer]["natural"]:
            case "wetland":
                weightedGrid[gridRow][i] = 0.10
                print("wet")
                
            case "grassland":
                weightedGrid[gridRow][i] = 0.98
                
            case "moor":
                weightedGrid[gridRow][i] = 0.95
                
            case "scrub":
                weightedGrid[gridRow][i] = 0.87
                
            case "tree":
                weightedGrid[gridRow][i] = 0.98
                
            case "shrubbery":
                weightedGrid[gridRow][i] = 0.65
                
            case "tree_row":
                weightedGrid[gridRow][i] = 0.76
                
            case "tree_stump":
                weightedGrid[gridRow][i] = 1
                
            case "tundra":
                weightedGrid[gridRow][i] = 0.76
                
            case "wood":
                weightedGrid[gridRow][i] = 0.43
                
            case "bay":
                weightedGrid[gridRow][i] = 0
                
            case "beach":
                weightedGrid[gridRow][i] = 0
                
            case "blowhole":
                weightedGrid[gridRow][i] = 0
                
            case "cape":
                weightedGrid[gridRow][i] = 0
                
            case "crevasse":
                weightedGrid[gridRow][i] = 0
                
            case "geyser":
                weightedGrid[gridRow][i] = 0.1
                
            case "glacier":
                weightedGrid[gridRow][i] = 0.15
                
            case "hot_spring":
                weightedGrid[gridRow][i] = 0.1
                
            case "isthmus":
                weightedGrid[gridRow][i] = 0.2
                
            case "mud":
                weightedGrid[gridRow][i] = 0.05
                
            case "peninsula":
                weightedGrid[gridRow][i] = 0.87
                
            case "reef":
                weightedGrid[gridRow][i] = 0
                
            case "shingle":
                weightedGrid[gridRow][i] = 0.01
                
            case "shoal":
                weightedGrid[gridRow][i] = 0
                
            case "spring":
                weightedGrid[gridRow][i] = 0
                
            case "strait":
                weightedGrid[gridRow][i] = 0.002
                
            case "water":
                weightedGrid[gridRow][i] = 0
                
            case "wetland":
                weightedGrid[gridRow][i] = 0.20
                
            case "arch":
                weightedGrid[gridRow][i] = 0
                
            case "arete":
                weightedGrid[gridRow][i] = 0
                
            case "bare_rock":
                weightedGrid[gridRow][i] = 0
                
            case "cave_entrance":
                weightedGrid[gridRow][i] = 0.3
                
            case "cliff":
                weightedGrid[gridRow][i] = 0.54
                
            case "dune":
                weightedGrid[gridRow][i] = 0.34
                
            case "hill":
                weightedGrid[gridRow][i] = 0.45
                
            case _:
                weightedGrid[gridRow][i] = 0.5
                
        i = i+1



