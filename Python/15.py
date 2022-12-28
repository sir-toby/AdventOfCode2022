from utils import imports


def importAndTransform(file):
    rawInput = imports.genericImport(file, ['\n', ': closest beacon is at ', ', '])
    refinedInput = []
    for line in rawInput:
        beacon = getCoordinates(line[0])
        sensor = getCoordinates(line[1])
        refinedInput.append([beacon, sensor])
    transposedInput = list(zip(*refinedInput))
    beaconList = transposedInput[1]
    sensorList = transposedInput[0]
    return refinedInput, beaconList, sensorList


def getCoordinates(rawCoordinates):
    xValue = int(rawCoordinates[0][rawCoordinates[0].find('=')+1:])
    yValue = int(rawCoordinates[1][rawCoordinates[1].find('=')+1:])
    return [xValue, yValue]


def part1(sensorAndBeaconList, beaconList):
    yRow = []
    row = 2000000
    for combination in sensorAndBeaconList:
        distance = getDistanceBetween(combination[0], combination[1])
        areaInYWhereNoBeacon = interferesWith(row, combination[0], distance)
        if not areaInYWhereNoBeacon == []:
            yRow = addToRow(yRow, areaInYWhereNoBeacon)
    yRow = takeBeaconPositionsOut(yRow, beaconList, row)

    print(yRow, sumOfFreeSpaces(yRow))


def takeBeaconPositionsOut(yRow, beaconList, row):
    for beacon in beaconList:
        if beacon[1] != row:
            continue

        beaconOverlap = overlapsWith(yRow, [beacon[0], beacon[0]])
        if beaconOverlap != []:
            beaconOverlap = beaconOverlap[0]
            yRow.remove(beaconOverlap)
            yRow.append([beaconOverlap[0], beacon[0]-1])
            yRow.append([beacon[0]+1, beaconOverlap[1]])
    return yRow


def getDistanceBetween(sensor, beacon):
    distance = abs(sensor[0]-beacon[0])+abs(sensor[1]-beacon[1])
    return distance


def interferesWith(yCoord, sensor, distance):
    if abs(sensor[1]-yCoord) > distance:
        return []
    else:
        coveredArea = distance-abs(sensor[1]-yCoord)
        return [sensor[0]-coveredArea, sensor[0]+coveredArea]


def addToRow(yRow, area):
    overlappingRanges = overlapsWith(yRow, area)
    if overlappingRanges == []:
        yRow.append(area)
    else:
        for range in overlappingRanges:
            yRow.remove(range)
        overlappingRanges.append(area)
        transposed = list(zip(*overlappingRanges))
        newRange = [min(transposed[0]), max(transposed[1])]
        yRow.append(newRange)
    return yRow


def overlapsWith(yRow, area):
    overlapList = []
    for range in yRow:
        if range[1] < area[0] or range[0] > area[1]:
            continue
        else:
            overlapList.append(range)

    return overlapList


def sumOfFreeSpaces(yRow):
    sum = 0
    for range in yRow:
        sum += range[1]-range[0] + 1
    return sum


# Main
sensorAndBeaconList, beaconList, sensorList = (importAndTransform("15 Input.txt"))
part1(sensorAndBeaconList, beaconList)
