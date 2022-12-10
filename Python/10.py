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


# Main
instructions = imports.genericImport("10 Input.txt", ["\n", " "])
interestingCycles = [20, 60, 100, 140, 180, 220]

# Part1:
print(sum(calculateValueFor(interestingCycles, instructions)))
