#
#   Hello! This is event(), which picks cards. 
#   Currently I have made only 14 cards, I was planning 
#   on making around 30 cards in total, with 17 negative
#   obstacles and 13 positive events.
#
#   I have set most of the cards in intervals of
#   two or three spaces. This can be changed, as we
#   need to agree on how many spaces we will have on
#   the board.
#

from random import *

def event():

    # if we do GUI, the user will pick an area on the
    # screen that says "card" or "pick a card"
    card = input("To pick a card, enter 'pick': ")

    fileNum = randint(1, 14)
    fileNum = "tc" + str(fileNum) + ".txt"
    print()

    fileOpen = open(fileNum, "r")
    desc = fileOpen.readline()
    print(desc)

    spaces = fileOpen.readline()

    if spaces[0] == '-':
        print("Retreat" + " " + spaces[1] + " " + "spaces")

    elif spaces[0] == '+':
        print("Advance" + " " + spaces[1] + " " + "spaces")

    #
    # FOR positionChange
    #
    # spaces[0] is supposed to indicate either '+' or '-"
    # i cant exactly convert it to a non-string type.
    # whoever would like to work on the accumulator function,
    # i would suggest using if/elif statements
    #
    # magitude is now an integer and can easily be used in
    # accumulator expressions
    #
    
    positionChange = spaces[0]

    magnitude = int(spaces[1])

    return positionChange, magnitude
    
event()
