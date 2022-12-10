import os


def import1d(filename, sepLevel1):
    inputText = (open(os.getcwd() + '\\Inputs\\' + filename, mode='r')).read()
    if inputText[-1] == '\n':
        inputText = inputText[0:-1]
    return inputText.split(sepLevel1)


def import2d(filename, sepLevel1, sepLevel2):
    level1 = import1d(filename, sepLevel1)
    level2 = []
    for item in level1:
        level2.append(item.split(sepLevel2))
    return level2


def import3d(filename, sepLevel1, sepLevel2, sepLevel3):
    level1 = import1d(filename, sepLevel1)
    level2 = []
    for level1item in level1:
        level2split = level1item.split(sepLevel2)
        level3 = []
        for level3item in level2split:
            level3split = level3item.split(sepLevel3)
            level3.append(level3split)
        level2.append(level3)
    return level2


def genericImport(filename, listOfSeparators):
    inputText = (open(os.getcwd() + '\\Inputs\\' + filename, mode='r')).read()
    if inputText[-1] == '\n':
        inputText = inputText[0:-1]
    if len(listOfSeparators) == 1:
        return inputText.split(listOfSeparators[0])
    else:
        finalList = recursiveSplit(inputText.split(
            listOfSeparators[0]), listOfSeparators[1:], 0)
        # print(finalList)
        return finalList


def recursiveSplit(listToBeSplit, separatorList, i):
    returnList = []
    for item in listToBeSplit:
        if separatorList[i] == "":
            splitItem = [*item]
        else:
            splitItem = item.split(separatorList[i])
        if len(separatorList) > i+1:
            splitItem = recursiveSplit(splitItem, separatorList, i+1)
        returnList.append(splitItem)
    return returnList
