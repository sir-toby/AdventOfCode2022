from utils import imports


def calculateValueFor(cycleList, instructions):
    x = 1
    cycle = 0
    valueListForCycles = []
    for instruction in instructions:
        if cycleList == []:
            return valueListForCycles
        match instruction[0]:
            case "noop":
                cycle += 1
                cycleList, valueListForCycles = checkIfInterestingCycle(cycle, x, cycleList, valueListForCycles)
            case "addx":
                cycle += 2
                cycleList, valueListForCycles = checkIfInterestingCycle(cycle, x, cycleList, valueListForCycles)
                x += int(instruction[1])
    print(valueListForCycles)
    return valueListForCycles


def checkIfInterestingCycle(cycle, x, cycleList, valueListForCycles):
    if cycle >= cycleList[0]:
        valueListForCycles.append(cycleList[0]*x)
        cycleList.pop(0)
    return cycleList, valueListForCycles


def buildDisplay(instructions, lineLength, totalLength):
    spritePos = 0
    cycle = 0
    display = []
    for instruction in instructions:
        match instruction[0]:
            case "noop":
                display.append(drawChar(spritePos, cycle, lineLength))
                cycle += 1
            case "addx":
                display.append(drawChar(spritePos, cycle, lineLength))
                cycle += 1
                display.append(drawChar(spritePos, cycle, lineLength))
                cycle += 1
                spritePos += int(instruction[1])

    finalDisplay = []
    line = ""
    for i in range(totalLength):
        line += display[i]
        if len(line) == lineLength:
            finalDisplay.append(line)
            line = ""

    return finalDisplay


def drawChar(spritePos, cycle, lineLength):
    if cycle % lineLength >= spritePos and cycle % lineLength <= spritePos+2:
        return "#"
    else:
        return "."


# Main
instructions = imports.genericImport("10 Input.txt", ["\n", " "])

# Part1:
interestingCycles = [20, 60, 100, 140, 180, 220]
print(sum(calculateValueFor(interestingCycles, instructions)))

# Part2:
lineLength = 40
totalLength = 240
lines = buildDisplay(instructions, lineLength, totalLength)
print("\n".join(lines))
