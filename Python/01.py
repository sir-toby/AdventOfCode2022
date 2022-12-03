from utils import imports

def getSum(elves):
    calorySum = []
    for elf in elves:
        sum = 0
        for calory in elf: 
            sum += int(calory)
        calorySum.append(sum)
    return calorySum

def getMax(elves, number):
    calorySum = getSum(elves)
    calorySum.sort(reverse=True)
    return sum(calorySum[0:number])

##Main part##
elves = imports.import2d('01 Input.txt', '\n\n', '\n')

print("Max calories on 1 elf: " + str(getMax(elves, 1)))
print("Max calories on 3 elves: " + str(getMax(elves, 3)))