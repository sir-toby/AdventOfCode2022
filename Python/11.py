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


def importMonkeyList(inputFileName):
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


def process(m):
    for item in m.items:
        item = calculateNewWorryLevel(item, m.operation)
        testNewMonkey(item, m.test, m.trueTarget, m.falseTarget)
        m.itemProcessCount += 1
    m.items = []
    return


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


def testNewMonkey(item, div, mTrue, mFalse):
    if item % div == 0:
        monkeyList[mTrue].items.append(item)
    else:
        monkeyList[mFalse].items.append(item)
    return

# get multiplication product of highest n item counts:


def productOfHighest(n, monkeyList):
    ipcList = []
    for j in range(len(monkeyList)):
        ipcList.append(monkeyList[j].itemProcessCount)
    ipcList.sort(reverse=True)
    return (prod(ipcList[:n]))


# Main
numberOfRounds = 20
monkeyList = importMonkeyList("11 Input.txt")

for i in range(numberOfRounds):
    for j in range(len(monkeyList)):
        process(monkeyList[j])

print(productOfHighest(2, monkeyList))
