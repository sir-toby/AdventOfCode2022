from utils import imports


def definePrio(letter):
    if letter.isupper():
        return (ord(letter)-64)+26
    elif letter.islower():
        return ord(letter)-96
    else:
        print('not a letter')
        return None


def doubleLetter(rucksack):
    compartment1 = rucksack[:int(len(rucksack)/2)]
    compartment2 = rucksack[int(len(rucksack)/2):]
    for letter in compartment1:
        if compartment2.count(letter) >= 1:
            return letter
    return None


def findDuplicates(rucksackList):
    sum = 0
    for rucksack in rucksackList:
        sum += definePrio(doubleLetter(rucksack))
    return sum


def badges(rucksackList):
    prioSum = 0
    for i in range(0, len(rucksackList), 3):
        prioSum += definePrio(findGroupBadge(rucksackList[i:i+3]))
    return prioSum


def findGroupBadge(group):
    for letter in group[0]:
        if letter in group[1]:
            if letter in group[2]:
                return letter
    return None


# Main
rucksackList = imports.import1d('03 Input.txt', '\n')

# Part1:
print('Priority of Duplicate letters: ' + str(findDuplicates(rucksackList)))

# Part2:
print('Priority of elf group badges: ' + str(badges(rucksackList)))
