from Namedtuple import gridValues,dictPointer
from grid import weightedGrid

dictPointer = 0

if dictPointer < 4:
    gridRow = 0
elif dictPointer > 4 < 8:
    gridRow = 1
elif dictPointer > 8 < 12:
    gridRow = 2
elif dictPointer > 12:
    gridRow = 3


for i in range(len(gridValues[dictPointer])):
    while i <= len(gridValues[dictPointer]):
        match gridValues[dictPointer]["natural"]:
            case "wetland":
                weightedGrid[gridRow] = 0.10
                print("wet")
                
            case "grassland":
                weightedGrid[gridRow] = 0.98
                
            case "moor":
                weightedGrid[gridRow] = 0.95
                
            case "scrub":
                weightedGrid[gridRow] = 0.87
                
            case "tree":
                weightedGrid[gridRow] = 0.98
                
            case "shrubbery":
                weightedGrid[gridRow] = 0.65
                
            case "tree_row":
                weightedGrid[gridRow] = 0.76
                
            case "tree_stump":
                weightedGrid[gridRow] = 1
                
            case "tundra":
                weightedGrid[gridRow] = 0.76
                
            case "wood":
                weightedGrid[gridRow] = 0.43
                
            case "bay":
                weightedGrid[gridRow] = 0
                
            case "beach":
                weightedGrid[gridRow] = 0
                
            case "blowhole":
                weightedGrid[gridRow] = 0
                
            case "cape":
                weightedGrid[gridRow] = 0
                
            case "crevasse":
                weightedGrid[gridRow] = 0
                
            case "geyser":
                weightedGrid[gridRow] = 0.1
                
            case "glacier":
                weightedGrid[gridRow] = 0.15
                
            case "hot_spring":
                weightedGrid[gridRow] = 0.1
                
            case "isthmus":
                weightedGrid[gridRow] = 0.2
                
            case "mud":
                weightedGrid[gridRow] = 0.05
                
            case "peninsula":
                weightedGrid[gridRow] = 0.87
                
            case "reef":
                weightedGrid[gridRow] = 0
                
            case "shingle":
                weightedGrid[gridRow] = 0.01
                
            case "shoal":
                weightedGrid[gridRow] = 0
                
            case "spring":
                weightedGrid[gridRow] = 0
                
            case "strait":
                weightedGrid[gridRow] = 0.002
                
            case "water":
                weightedGrid[gridRow] = 0
                
            case "wetland":
                weightedGrid[gridRow] = 0.20
                
            case "arch":
                weightedGrid[gridRow] = 0
                
            case "arete":
                weightedGrid[gridRow] = 0
                
            case "bare_rock":
                weightedGrid[gridRow] = 0
                
            case "cave_entrance":
                weightedGrid[gridRow] = 0.3
                
            case "cliff":
                weightedGrid[gridRow] = 0.54
                
            case "dune":
                weightedGrid[gridRow] = 0.34
                
            case "hill":
                weightedGrid[gridRow] = 0.45
                
            case _:
                weightedGrid[gridRow] = 0
                
        i = i+1
            
print(enumerate(weightedGrid))
print(range(len(gridValues[dictPointer])))

