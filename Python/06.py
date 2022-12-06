# Main
from utils import imports


def firstUniqueOccurence(datastream, numberOfUniqueChars):
    for i in range(numberOfUniqueChars, len(datastream), 1):
        searchString = datastream[i-(numberOfUniqueChars):i]
        duplicate = False
        for char in searchString:
            if searchString.count(char) > 1:
                duplicate = True
                break
        if duplicate == False:
            return i


input = imports.import1d("06 Input.txt", "\n")
for line in input:
    print("Part 1: Start-of-Package-Marker:", firstUniqueOccurence(line, 4))
    print("Part 2: Message-Marker:", firstUniqueOccurence(line, 14))
