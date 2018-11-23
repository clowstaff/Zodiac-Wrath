#
#
#
#

from random import *

def dice():
    toss = randint(1, 6)

    return toss

# Prompting the user is not necessarily going to be in
# this one function, but its just the idea.
def main():
    print("DICE & CARD SIMULATOR . . .\n")

    roll = input("Roll the dice? (type roll): ")

    toss = dice()

    if toss == 1:
        print("\tYou have moved", toss, "space")
    else:
        print("\tYou have moved", toss, "spaces")

main()
