from utils import imports


def importAndConvert(filename: str):
    rockList = imports.genericImport(filename, ['\n', ' -> ', ','])
    rockList, sandSpawnPosition = shiftToMinimum(rockList)

    emptyMap = generateEmptyMap(rockList)
    filledMap = fillMap(emptyMap, rockList)
    printNice(filledMap)

    return filledMap, sandSpawnPosition


def shiftToMinimum(rockList: list) -> tuple[list, int]:
    transformedRockList = list(zip(*sum(rockList, [])))
    minX = min(list(map(int, transformedRockList[0])))

    for row in rockList:
        for coord in row:
            coord[0] = int(coord[0])-minX
            coord[1] = int(coord[1])
    return rockList, 500-minX


def generateEmptyMap(rockList: list):
    transformedRockList = list(zip(*sum(rockList, [])))
    maxX = max(transformedRockList[0])+1
    minX = 0
    maxY = max(transformedRockList[1])+1
    minY = 0

    emptyMap = []
    for y in range(minY, maxY):
        emptyRow = []
        for x in range(minX, maxX):
            emptyRow.append('.')
        emptyMap.append(emptyRow)
    return emptyMap


def minMax(val1, val2):
    minVal = min(val1, val2)
    maxVal = max(val1, val2)+1
    return minVal, maxVal


def fillMap(emptyMap, rockList):
    for formation in rockList:
        for corner in range(len(formation)-1):
            if formation[corner][0] == formation[corner+1][0]:
                minY, maxY = minMax(formation[corner][1], formation[corner+1][1])
                for y in range(minY, maxY):
                    emptyMap[y][formation[corner][0]] = '#'
            elif formation[corner][1] == formation[corner+1][1]:
                minX, maxX = minMax(formation[corner][0], formation[corner+1][0])
                for x in range(minX, maxX):
                    emptyMap[formation[corner][1]][x] = '#'
            else:
                print('Error, invalid input')
    return emptyMap


def addEmptyLayer(caveMap, sandSpawnPosition):
    for row in caveMap:
        row.insert(0, '.')
        row.append('.')
    newLine = []
    for char in caveMap[0]:
        newLine.append('.')
    caveMap.append(newLine)
    return caveMap, sandSpawnPosition+1


def addEmptyLine(rockMap, sandSpawnPosition, where):
    if where == 'left':
        sandSpawnPosition += 1
        for line in rockMap:
            line.insert(0, '.')
    elif where == 'right':
        for line in rockMap:
            line.append('.')
    return rockMap, sandSpawnPosition


def spawnAndProcessSand(pos0, rockMap):
    y = 0
    x = pos0
    while True:
        if rockMap[y+1][x] == '.':
            y = y+1
        elif rockMap[y+1][x-1] == '.':
            y = y+1
            x = x-1
        elif rockMap[y+1][x+1] == '.':
            y = y+1
            x = x+1
        else:
            rockMap[y][x] = 'o'
            return rockMap, True
        if y > len(rockMap) or x < 0 or x > len(rockMap[0]):
            return rockMap, False


def spawnAndProcessSand2(pos0, rockMap):
    y = 0
    x = pos0
    while y < len(rockMap)-1:
        if rockMap[y+1][x] == '.':
            y = y+1
        elif rockMap[y+1][x-1] == '.':
            y = y+1
            x = x-1
        elif rockMap[y+1][x+1] == '.':
            y = y+1
            x = x+1
        else:
            break

    rockMap[y][x] = 'o'
    if x == 0:
        rockMap, pos0 = addEmptyLine(rockMap, pos0, 'left')
    elif x == len(rockMap[0])-1:
        rockMap, pos0 = addEmptyLine(rockMap, pos0, 'right')
    return pos0, rockMap


def printNice(caveMap):
    toPrint = []
    for row in caveMap:
        toPrint.append(''.join(row))
    print('\n'.join(toPrint), end='\n\n')


def part1():
    rockMap, sandSpawnPosition = importAndConvert("14 Input.txt")

    remainsInMap = True
    numberOfSpawns = 0
    while remainsInMap:
        rockMap, remainsInMap = spawnAndProcessSand(sandSpawnPosition, rockMap)
        if remainsInMap:
            numberOfSpawns += 1
    printNice(rockMap)
    print(numberOfSpawns)


def part2():
    rockMap, sandSpawnPosition = importAndConvert("14 Input.txt")
    rockMap, sandSpawnPosition = addEmptyLayer(rockMap, sandSpawnPosition)

    numberOfSpawns = 0
    while rockMap[0][sandSpawnPosition] == '.':
        sandSpawnPosition, rockMap = spawnAndProcessSand2(sandSpawnPosition, rockMap)
        numberOfSpawns += 1
    printNice(rockMap)
    print(numberOfSpawns)


# Main
# part1()
part2()
