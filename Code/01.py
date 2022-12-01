import os

def inputSplit(inputText):
    elvList = inputText.split('\n\n')
    elves = []
    for elf in elvList:
        elves.append(elf.split('\n'))
    return elves

def getSum(elflist):
    elvSum = []
    for elv in elflist:
        sum = 0
        for cal in elv: 
            sum += int(cal)
        elvSum.append(sum)
    return elvSum

def getMax(elflist):
    sumList = getSum(elflist)
    return max(sumList)

def getMax3(elflist):
    sumList = getSum(elflist)
    sumList.sort(reverse=True)
    return sum(sumList[0:3])

##Main part##

filename = '01 Input.txt'
inputText = (open(os.getcwd() + '\Inputs\\' + filename, mode='r')).read()

elves = inputSplit(inputText)

print("Max calories on 1 elf: " + str(getMax(elves)))
print("Max calories on 3 elves: " + str(getMax3(elves)))
