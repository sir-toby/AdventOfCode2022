import os 

def import1d(filename, sep1):
    inputText = (open(os.getcwd() + '\Inputs\\' + filename, mode='r')).read()
    if inputText[-1]=='\n': inputText = inputText[0:-1]
    return inputText.split(sep1)


def import2d(filename, sep1, sep2):
    inputText = (open(os.getcwd() + '\Inputs\\' + filename, mode='r')).read()
    if inputText[-1]=='\n': inputText = inputText[0:-1]
    level1 = inputText.split(sep1)
    level2 = []
    for item in level1:
        level2.append(item.split(sep2))
    return level2

