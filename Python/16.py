from utils import imports
import random


class valve:
    overallFlowRate = 0

    def __init__(self, name, flowRate, connectingValves):
        self.name = name
        self.flowRate = int(flowRate)
        self.connectingValves = connectingValves
        self.isOpen = False

    def openValve(self):
        self.isOpen = True
        valve.overallFlowRate += self.flowRate

    def closeValve(self):
        self.isOpen = False
        valve.overallFlowRate -= self.flowRate


def importAndProcess(filename):
    rawInput = imports.genericImport(filename, ['\n'])
    valveList = {}
    for line in rawInput:
        name = line[6:8]
        flowRate = line[line.find('=')+1:line.find(';')]
        if line.find('valves') == -1:
            connectingValves = [line[-2:]]
        else:
            connectingValves = line[line.find('valves ')+7:].split(', ')
        valveList[name] = valve(name, flowRate, connectingValves)
    # print(valveList)
    return valveList


def part1(valveList, startValve, minutes):
    allPaths = []
    noChange = 0
    maxRelease = 0
    bestPath = []

    while noChange < 10000:
        testPath = tryWay(valveList, startValve, minutes)
        if testPath not in allPaths:
            allPaths.append(testPath)
            noChange = 0
            if testPath[1] > maxRelease:
                maxRelease = testPath[1]
                bestPath = testPath[0]
        else:
            noChange += 1
        if noChange == 100:
            print(len(allPaths))
    print(maxRelease, bestPath)


def tryWay(valveList, startValve, minutes):
    currentPosition = startValve
    path = []
    releasedPressure = 0
    for minute in range(minutes):
        action = determineAction(valveList[currentPosition])
        path.append([minute, action, currentPosition])
        if action == 'openValve':
            valveList[currentPosition].openValve()
        elif action == 'move':
            currentPosition = moveTo(valveList[currentPosition])
        else:
            print('error')
        releasedPressure += valve.overallFlowRate
    for val in valveList.values():
        val.closeValve()
    return [path, releasedPressure]


def determineAction(currentValve: valve):
    if currentValve.isOpen or currentValve.flowRate == 0:
        return 'move'
    else:
        return random.choice(['openValve', 'move'])


def moveTo(currentValve):
    return random.choice(currentValve.connectingValves)


def part2():
    pass


# Main
valveList = importAndProcess("16 Test.txt")

part1(valveList, 'AA', 30)
