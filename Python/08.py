from utils import imports


def isVisible(y, x, treeMap):
    transposedTreeMap = list(zip(*treeMap))
    if (checkVisibility(transposedTreeMap[x][:y], treeMap[y][x]) or  # Up
        checkVisibility(transposedTreeMap[x][y+1:], treeMap[y][x]) or  # Down
        checkVisibility(treeMap[y][:x], treeMap[y][x]) or  # Left
            checkVisibility(treeMap[y][x+1:], treeMap[y][x])):  # right
        return True
    else:
        return False


def checkVisibility(treeList, tree):
    for compTree in treeList:
        if compTree >= tree:
            return False
    return True


# Main
treeMap = imports.genericImport("08 Input.txt", ["\n", ""])

visibleCount = 2*(len(treeMap) + len(treeMap[0]))-4

for y in range(1, len(treeMap)-1, 1):
    for x in range(1, len(treeMap[0])-1, 1):
        if isVisible(y, x, treeMap) == True:
            visibleCount += 1

print("Visible trees: " + str(visibleCount))
