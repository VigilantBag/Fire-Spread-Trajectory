# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from typing import NamedTuple

class gridValues1(dict):
    groundCover: str
    natural: str
    landUse: str
    elevation: int
    isRoad: bool
    isBuilding: bool
    isHouse: bool
    foliageType: str
dictPointer = 0
gridValues = []


gridValues.append({"groundCover": 'none', "natural":'none', "landuse": 'none',
                         "ele": 0, "isRoad": "False", "isBuilding": False,
                         "isHouse": False, "foliageType": 'none'})

#print (simulation1)
print(gridValues[0]["groundCover"])
print(range(len(gridValues[0])))
