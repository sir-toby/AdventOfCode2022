from utils import imports
from math import sqrt


def move(line, posHead, posTail, visitedPlaces):
    for i in range(int(line[1])):
        posHead = moveHead(line[0], posHead)
        posTail = moveTail(posHead, posTail)
        if posTail not in visitedPlaces:
            visitedPlaces.append(posTail)
    return posHead, posTail, visitedPlaces


def moveHead(direction, posHead):
    match direction:
        case "U":
            posHead = [posHead[0], posHead[1]+1]
        case "D":
            posHead = [posHead[0], posHead[1]-1]
        case "L":
            posHead = [posHead[0]-1, posHead[1]]
        case "R":
            posHead = [posHead[0]+1, posHead[1]]
    return posHead


def moveTail(posHead, posTail):
    difVector = [posHead[0]-posTail[0], posHead[1]-posTail[1]]
    absDifVector = sqrt(difVector[0]**2 + difVector[1]**2)
    if absDifVector < 2:
        return posTail
    else:
        posTail = [posTail[0]+sign(difVector[0]), posTail[1]+sign(difVector[1])]
        return posTail


def sign(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0


# Main
instructions = imports.genericImport("09 Input.txt", ["\n", " "])

posHead = [0, 0]  # [x, y]
posTail = [0, 0]  # [x, y]
visitedPlaces = []

for line in instructions:
    posHead, posTail, visitedPlaces = move(line, posHead, posTail, visitedPlaces)
print(posHead, posTail, len(visitedPlaces))
