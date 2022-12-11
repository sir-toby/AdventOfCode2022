from utils import imports
from math import prod


# monkeyClass = [[items], operation, test, trueTarget, falseTarget]


class monkey:
    def __init__(self, index, itemList, operation, test, trueTarget, falseTarget):
        self.index = index
        self.items = itemList
        self.operation = operation
        self.test = test
        self.trueTarget = trueTarget
        self.falseTarget = falseTarget
        self.itemProcessCount = 0

    def __str__(self):
        return f"{self.index}, {self.items}, {self.operation}, {self.test}, {self.trueTarget}, {self.falseTarget}, {self.itemProcessCount}"


def importMonkeyListPt1(inputFileName):
    input = imports.genericImport(inputFileName, ["\n\n", "\n", ": "])
    monkeyList = {}
    for monk in input:
        index = int(monk[0][0][-2])
        items = list(map(int, monk[1][1].split(", ")))
        operation = monk[2][1][6:].split(" ")
        testDivisor = int((monk[3][1].split(" "))[2])
        trueMonkey = int(monk[4][1][-1])
        falseMonkey = int(monk[5][1][-1])

        monkeyList[index] = monkey(index, items, operation, testDivisor, trueMonkey, falseMonkey)
    return monkeyList


def importMonkeyListPt2(inputFileName):
    input = imports.genericImport(inputFileName, ["\n\n", "\n", ": "])
    monkeyList = {}
    allItems = []
    allDivisors = []

    for monk in input:
        index = int(monk[0][0][-2])
        items = list(map(int, monk[1][1].split(", ")))
        operation = monk[2][1][6:].split(" ")
        testDivisor = int((monk[3][1].split(" "))[2])
        trueMonkey = int(monk[4][1][-1])
        falseMonkey = int(monk[5][1][-1])

        monkeyList[index] = monkey(index, items, operation, testDivisor, trueMonkey, falseMonkey)
        allItems.append(items)
        allDivisors.append(testDivisor)

    for itemList in allItems:
        itemDivisorList = {}
        for i in itemList:
            newLine = {}
            for div in allDivisors:
                newLine[div] = i % div
            itemDivisorList[i] = newLine
        monkeyList[allItems.index(itemList)].items = itemDivisorList
        print(itemDivisorList)

    return monkeyList


def processPt1(m, monkeyList):
    for item in m.items:
        item = calculateNewWorryLevel(item, m.operation)
        monkeyList = testNewMonkey(item, m.test, m.trueTarget, m.falseTarget, monkeyList)
        m.itemProcessCount += 1
    m.items = []
    return monkeyList


def processPt2(m, monkeyList):
    for item in m.items:
        item = calculateNewWorryLevel(item, m.operation)
        monkeyList = testNewMonkey(item, m.test, m.trueTarget, m.falseTarget, monkeyList)
        m.itemProcessCount += 1
    m.items = []
    return monkeyList


def calculateNewWorryLevel(item, operation):
    if operation[0] != "old":
        print("error while processing, skipping...")
        return item
    else:
        a = item

    if operation[2] == "old":
        b = item
    else:
        b = int(operation[2])
    # Perform monkey operation
    match operation[1]:
        case "+":
            result = a+b
        case "*":
            result = a*b
        case __:
            result = 0
            print("Error during operation")
    # Reduce worry level
    result = int(result/3)

    return result


def testNewMonkey(item, div, mTrue, mFalse, monkeyList):
    if item % div == 0:
        monkeyList[mTrue].items.append(item)
    else:
        monkeyList[mFalse].items.append(item)
    return monkeyList


def productOfHighest(n, monkeyList):
    ipcList = []
    for j in range(len(monkeyList)):
        ipcList.append(monkeyList[j].itemProcessCount)
    ipcList.sort(reverse=True)
    return (prod(ipcList[:n]))


def part1(fileName, numberOfCycles):
    monkeyList = importMonkeyListPt1(fileName)
    for i in range(numberOfCycles):
        for j in range(len(monkeyList)):
            monkeyList = processPt1(monkeyList[j], monkeyList)
    print(productOfHighest(2, monkeyList))
    return

 def part2(fileName, numberOfCycles):
    monkeyList = importMonkeyListPt2(fileName)
    for i in range(numberOfCycles):
        for j in range(len(monkeyList)):
            monkeyList = processPt2(monkeyList[j], monkeyList)
    print(productOfHighest(2, monkeyList))

# Main
part1("11 Input.txt", 20)
part2("11 Input.txt", 10000)
# 6 --> *3 --> 18
# 18 --> +5 --> 23
# 23 --> *2 --> 46
# 46 --> +6 --> 52
## div13 = true

# 6 --> *3 --> 5
# 18 --> +5 --> 10
# 23 --> *2 --> 7
# 46 --> +6 --> 13


# calculatePerDivisor

# 1. when read: add each divisor to each monkey ( items = [item1 {17: 26, 13:24, etc.}])
# 2. when calculating: calculate for every divisor and modulo
# 3. when checking: check only for current divisor
