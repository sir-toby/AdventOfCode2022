import os

def inputSplit(inputText):
    elfList = inputText.split('\n\n')
    elves = []
    for elf in elfList:
        elves.append(elf.split('\n'))
    return elves

def getSum(elves):
    elfSum = []
    for elf in elves:
        sum = 0
        for cal in elf: 
            sum += int(cal)
        elfSum.append(sum)
    return elfSum

def getMax(elves, number):
    sumList = getSum(elves)
    sumList.sort(reverse=True)
    return sum(sumList[0:number])

##Main part##

filename = '01 Input.txt'
inputText = (open(os.getcwd() + '\Inputs\\' + filename, mode='r')).read()

elves = inputSplit(inputText)

print("Max calories on 1 elf: " + str(getMax(elves, 1)))
print("Max calories on 3 elves: " + str(getMax(elves, 3)))