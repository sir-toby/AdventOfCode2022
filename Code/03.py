from utils import imports

def doubleLetter(rucksack):
    compartment1=rucksack[:int(len(rucksack)/2)]
    compartment2=rucksack[int(len(rucksack)/2):]
    for letter in compartment1: 
        if compartment2.count(letter) >= 1:
            return letter
    return None

#Main
rucksackList = imports.import1d('03 Input.txt', '\n')

sum = 0
for rucksack in rucksackList:
    duplicate=doubleLetter(rucksack)
    if duplicate.isupper(): 
        sum += (ord(duplicate)-64)+26
    elif duplicate.islower(): 
        sum += ord(duplicate)-96
    else: print('not a letter')

print(sum)