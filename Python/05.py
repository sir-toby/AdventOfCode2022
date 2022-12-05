from utils import imports
import os


def import05(filename):
    inputText = (open(os.getcwd() + '\\Inputs\\' + filename, mode='r')).read()
    if inputText[-1] == '\n':
        inputText = inputText[0:-1]
    inputTextList = inputText.split("\n\n")
    return makeCrateList(inputTextList[0].split("\n")), makeTaskList(inputTextList[1].split("\n"))


def makeTaskList(taskInput):
    taskList = []
    for line in taskInput:
        lineList = []
        helperList = line.strip("move ").split(" from ")
        lineList.append(int(helperList[0]))
        helperList = helperList[1].split(" to ")
        lineList.append(int(helperList[0]))
        lineList.append(int(helperList[1]))
        taskList.append(lineList)
    return taskList


def makeCrateList(crateInput):

    crateInput = crateInput[:-1]
    crateInput.reverse()
    crateList = []
    for j in range(int((len(crateInput[0])+1)/4)):
        newLine = []
        for i in range(len(crateInput)):
            if crateInput[i][4*j+1] != " ":
                newLine.append(crateInput[i][4*j+1])
        crateList.append(newLine)
    return crateList


def rearrange(crateList, taskList, reverseWhileMoving):
    for task in taskList:
        count = task[0]
        fromCrate = task[1]-1
        toCrate = task[2]-1
# move 0 from 1 to 2
# define wich crates to be moved
        movedCrates = crateList[fromCrate][-count:]
        if reverseWhileMoving:
            movedCrates.reverse()
# move crates to new staple
        crateList[toCrate] = (crateList[toCrate] + movedCrates)
# remove crates from old staple
        crateList[fromCrate] = crateList[fromCrate][:-count]
    return crateList


def code(crateList):
    codeword = ""
    for col in crateList:
        codeword += col[-1]
    return codeword


# Main
crateList, taskList = import05("05 Input.txt")

# Perform rearrangement
print("CrateMover9000:", code(rearrange(crateList, taskList, True)),
      "\nCrateMover9001:", code(rearrange(crateList, taskList, True)))
