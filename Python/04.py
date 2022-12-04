from utils import imports


def fullOverlap(pair):
    if (fullyContainedIn(pair[0], pair[1]) or fullyContainedIn(pair[1], pair[0])):
        return True
    else:
        return False


def fullyContainedIn(tested, compared):
    if ((int(tested[0]) >= int(compared[0])) and (int(tested[1]) <= int(compared[1]))):
        return True
    else:
        return False


def partialOverlap(pair):
    if partialContainedIn(pair[0], pair[1]):
        return True
    else:
        return False


def partialContainedIn(tested, compared):
    if (max(int(tested[0]), int(compared[0])) <= min(int(tested[1]), int(compared[1]))):
        return True
    else:
        return False


# Main
listOfElfPairs = imports.genericImport("04 Input.txt", ["\n", ",", "-"])
fullOverlapCount = 0
partialOverlapCount = 0
for pair in listOfElfPairs:
    if fullOverlap(pair):
        fullOverlapCount += 1
    if partialOverlap(pair):
        partialOverlapCount += 1
print(fullOverlapCount, partialOverlapCount)
