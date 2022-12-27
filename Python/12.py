from utils import imports


class coordinate:
    visitableFrom = []
    distanceToTarget = 999999

    def __init__(self, xCoord, yCoord, height):
        self.x = xCoord
        self.y = yCoord
        self.height = height


def generateCoordList(importMap):
    coordList = []
    start = None
    end = None
    for y in range(len(importMap)):
        for x in range(len(importMap[y])):
            coordList.append(coordinate(x, y, ord(importMap[y][x])-97))
    for coord in coordList:
        if coord.height == ord("S")-97:
            start = coordinate(coord.x, coord.y, 0)
            coord.height = 0
        elif coord.height == ord("E")-97:
            end = coordinate(coord.x, coord.y, 25)
            coord.height = 25
    return coordList, start, end


## Main##
importMap = imports.genericImport("12 Test.txt", ["\n", ""])
coordList = generateCoordList(importMap)
#start, finish = findCoords("S", "E", importMap)
print(coordList)


def calculateDistanceToTarget(coord, start, end):
    if coord.x == end.x and coord.y == end.y:
        coord.distanceToTarget = 0

    reachableFrom(coord)


def reachableFrom(coord):
    heightDifference = 1
