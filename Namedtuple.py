# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from typing import NamedTuple

class gridValues(NamedTuple):
    groundCover: str
    natural: str
    landUse: str
    elevation: int
    isRoad: bool
    isBuilding: bool
    isHouse: bool
    foliageType: str


simulation1 = gridValues(groundCover= 'none', natural = 'scrub', landUse= 'wild life',
                         elevation= 44000, isRoad= False, isBuilding= False,
                         isHouse= False, foliageType= 'grass')

print (simulation1)
