from utils import imports
from math import sqrt


def moveRope(instruction, rope, visitedPlaces):
    for i in range(int(instruction[1])):
        rope[0] = moveHead(instruction[0], rope[0])
        for j in range(1, len(rope), 1):
            rope[j] = moveKnot(rope[j-1], rope[j])
        if rope[-1] not in visitedPlaces:
            visitedPlaces.append(rope[-1])
    return rope, visitedPlaces


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


def moveKnot(posHead, posTail):
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


def executeInstructionsForRope(instructions, numberOfKnots):
    rope = []
    visitedPlaces = []
    for i in range(numberOfKnots+1):
        rope.append([0, 0])

    for instruction in instructions:
        rope, visitedPlaces = moveRope(instruction, rope, visitedPlaces)

    return rope, visitedPlaces


# Main
instructions = imports.genericImport("09 Input.txt", ["\n", " "])

# Part1:
rope, visitedPlaces = executeInstructionsForRope(instructions, 1)
print("Part 1: Final rope position: ", rope, ", number of visitedPlaces: ", len(visitedPlaces))

rope, visitedPlaces = executeInstructionsForRope(instructions, 9)
print("Part 2: Final rope position: ", rope,  ", number of visitedPlaces: ", len(visitedPlaces))
