from utils import imports


def definePrio(letter):
    # returns the prio of a single letter
    if letter.isupper():
        return (ord(letter)-64)+26
    elif letter.islower():
        return ord(letter)-96
    else:
        print('not a letter')
        return None


def findDuplicate(rucksack):
    # find the single duplicate entry in both compartments of a rucksack
    compartment1 = rucksack[:int(len(rucksack)/2)]
    compartment2 = rucksack[int(len(rucksack)/2):]
    for letter in compartment1:
        if letter in compartment2:
            return letter
    return None


def sumOfDuplicates(rucksackList):
    # builds the sum of the prio of all duplicate Letters in compartments of a rucksack
    sum = 0
    for rucksack in rucksackList:
        sum += definePrio(findDuplicate(rucksack))
    return sum


def sumOfBadges(rucksackList):
    # builds the sum of the prio of badges of each 3 elves
    prioSum = 0
    for i in range(0, len(rucksackList), 3):
        prioSum += definePrio(findGroupBadge(rucksackList[i:i+3]))
    return prioSum


def findGroupBadge(group):
    # finds and returns the group badge of a group of 3 elves
    for letter in group[0]:
        if letter in group[1]:
            if letter in group[2]:
                return letter
    return None


# Main
rucksackList = imports.import1d('03 Input.txt', '\n')

# Part1:
print('Priority of Duplicate letters: ' + str(sumOfDuplicates(rucksackList)))

# Part2:
print('Priority of elf group badges: ' + str(sumOfBadges(rucksackList)))
