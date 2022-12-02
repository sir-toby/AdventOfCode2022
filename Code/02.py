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
    #const who wins:
    #1:1 draw
    #1:2 right
    #1:3 left
    #2:1 left
    #2:2 draw
    #2:3 right
    #3:1 right
    #3:2 left
    #3:3 draw
    match (game[1]-game[0])%3:
        case 1: return 6+game[1] #win
        case 0: return 3+game[1]
        case 2: return game[1]

def result2(game):
    game = transformToNumbers(game)
    match game[1]:
        #modulo +1 at the end to keep "3" in there
        case 1: return (game[0]+1)%3+1 #lose --> 2 items down the list
        case 2: return 3+game[0] #draw
        case 3: return 6+(game[0])%3+1 #win --> 1 item down the list

#Main:
rpslist = imports.import2d('02 Input.txt', '\n', ' ')

points1=0
points2=0
for game in rpslist: 
    points1 += result(game)
    points2  += result2(game)
print('Part 1: ' + str(points1) + ', Part 2: ' + str(points2))