from utils import imports


def transformToNumbers(game):
    game2 = [0,0]
    match game[0]:
        case 'A': game2[0] = 1
        case 'B': game2[0] = 2
        case 'C': game2[0] = 3

    match game[1]:
        case 'X': game2[1] = 1
        case 'Y': game2[1] = 2
        case 'Z': game2[1] = 3

    return game2

def result(game):
    game = transformToNumbers(game)
    #1:1 draw
    #1:2 right
    #1:3 left
    #2:1 left
    #2:2 draw
    #2:3 right
    #3:1 right
    #3:2 left
    #3:3 draw
    difference = (game[1]-game[0])%3
    if difference == 1: return 6+game[1]
    if difference == 0: return 3+game[1]
    if difference == 2: return game[1]

#Main:
rpslist = imports.import2d('02 Input.txt', '\n', ' ')
#Part1:
points=0
for game in rpslist: 
    points += result(game)
print(points)