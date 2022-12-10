from utils import imports


def countVisibleTrees(treeMap):
    visibleCount = 2*(len(treeMap) + len(treeMap[0]))-4

    for y in range(1, len(treeMap)-1, 1):
        for x in range(1, len(treeMap[0])-1, 1):
            if isTreeVisible(y, x, treeMap) == True:
                visibleCount += 1
    return visibleCount


def isTreeVisible(y, x, treeMap):
    transposedTreeMap = list(zip(*treeMap))
    if (checkVisibilityInDirection(transposedTreeMap[x][:y], treeMap[y][x]) or  # Up
        checkVisibilityInDirection(transposedTreeMap[x][y+1:], treeMap[y][x]) or  # Down
        checkVisibilityInDirection(treeMap[y][:x], treeMap[y][x]) or  # Left
            checkVisibilityInDirection(treeMap[y][x+1:], treeMap[y][x])):  # right
        return True
    else:
        return False


def checkVisibilityInDirection(treeList, tree):
    for compTree in treeList:
        if compTree >= tree:
            return False
    return True


def determineMaxScenicScore(treeMap):
    maxScore = 0
    for y in range(1, len(treeMap)-1, 1):
        for x in range(1, len(treeMap[0])-1, 1):
            score = scenicScore(y, x, treeMap)
            if score > maxScore:
                maxScore = score
    return maxScore


def scenicScore(y, x, treeMap):
    transposedTreeMap = list(zip(*treeMap))
    up = scoreInDirection(transposedTreeMap[x][:y], treeMap[y][x], True)
    down = scoreInDirection(transposedTreeMap[x][y+1:], treeMap[y][x], False)
    left = scoreInDirection(treeMap[y][:x], treeMap[y][x], True)
    right = scoreInDirection(treeMap[y][x+1:], treeMap[y][x], False)
    score = up*down*left*right
    return score


def scoreInDirection(treeList, tree, reversed):
    if reversed:
        treeList = list(treeList)
        treeList.reverse()
    i = 0
    for i in range(len(treeList)):
        if tree <= treeList[i]:
            return i+1
    return i+1


# Main
treeMap = imports.genericImport("08 Input.txt", ["\n", ""])

# Part1
print("Visible trees: " + str(countVisibleTrees(treeMap)))

# Part 2
print("Highest scenic score: " + str(determineMaxScenicScore(treeMap)))
