from utils import imports


def importAndConvert(file: str) -> list:
    pairList = imports.genericImport(file, ['\n\n', '\n'])
    for pair in pairList:
        pair[0], waste = convertToList(pair[0])
        pair[1], waste = convertToList(pair[1])
    return pairList


def importAndConvert2(file: str) -> list:
    itemList = imports.genericImport(file, ['\n\n', '\n'])
    for item in itemList:
        item[0], waste = convertToList(item[0])
        item[1], waste = convertToList(item[1])
    itemList = sum(itemList, [])
    return itemList


# Process the stupid input into a handelable list
def convertToList(inputString: str, charPos: int = 1) -> tuple[list, int]:
    outputList = []
    lastSpecial = charPos-1
    sub = None

    if inputString == '[]':
        return outputList, charPos+1

    while charPos <= len(inputString):
        match inputString[charPos]:
            case '[':
                sub, charPos = convertToList(inputString, charPos+1)
            case ']':
                if sub == None and inputString[charPos-1] != '[':
                    sub = int(inputString[lastSpecial+1:charPos])
                if sub != None:
                    outputList.append(sub)
                return outputList, charPos
            case ',':
                if sub == None:
                    sub = int(inputString[lastSpecial+1:charPos])
                outputList.append(sub)
                sub = None
                lastSpecial = charPos
            case _:
                pass
        charPos += 1
    return outputList, charPos
###############

#


def isLeftListSmaller(list1: list, list2: list):

    for itemToCompare in range(len(list1)):
        left = list1[itemToCompare]

        # When right list is empty:
        try:
            right = list2[itemToCompare]
        except:
            return False

        # Compare left and right and determine how to compare and handle:
        if type(left) == int and type(right) == int:
            result = compareNumerics(left, right)
        elif type(left) == list and type(right) == list:
            result = isLeftListSmaller(left, right)
        elif type(left) == int and type(right) == list:
            result = isLeftListSmaller([left], right)
        elif type(left) == list and type(right) == int:
            result = isLeftListSmaller(left, [right])
        else:
            print("Error while determining the correct way to compare")

        if not result == 'Draw':
            return result

    # If left list ran out of items:
    if len(list1) == len(list2):
        return 'Draw'
    else:
        return True


def compareNumerics(left, right):
    if int(left) > int(right):
        return False
    elif int(left) < int(right):
        return True
    else:
        return 'Draw'


def part1():
    correctPairs = 0
    listOfPairs = importAndConvert('13 Input.txt')
    for pair in listOfPairs:
        if isLeftListSmaller(pair[0], pair[1]):
            #print(pair, listOfPairs.index(pair)+1)
            correctPairs += listOfPairs.index(pair)+1
        else:
            print(pair, listOfPairs.index(pair)+1)
    print(correctPairs)


def part2():
    listOfItems = importAndConvert2('13 Input.txt')
    sortedListOfItems = [[[2]], [[6]]]
    for item in listOfItems:
        for sortedItem in sortedListOfItems:
            if isLeftListSmaller(item, sortedItem) == True:
                sortedListOfItems.insert(sortedListOfItems.index(sortedItem), item)
                break
        if item not in sortedListOfItems:
            sortedListOfItems.append(item)
    print(sortedListOfItems)
    print((sortedListOfItems.index([[2]])+1)*(sortedListOfItems.index([[6]])+1))


# Main
# part1()
part2()
