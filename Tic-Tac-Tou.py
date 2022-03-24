'''
This is my simple Tic Tac Tou game created for my Udemy Bootcamp Milestone Project
'''

#fucntion to display the tic tac tou table
from ast import And


def display():
    num="O"
    print("\n")
    print("\t \t|\t \t|")
    print(f"\t{num}\t|\t{num}\t|\t{num}\t")
    print("_"*50)
    print("\t \t|\t \t|")
    print(f"\t{num}\t|\t{num}\t|\t{num}\t")
    print("_"*50)
    print("\t \t|\t \t|")
    print(f"\t{num}\t|\t{num}\t|\t{num}\t")
    print("\n")

#Function to decide which player goes first
def first():
    import random
    player={"White":0, "Black":0}
    for i in (player):
            player[i]=(random.randrange(0,10))
    if player["White"]>player["Black"]:
        return 1
    else:
        return 2

def game_run(func):
    if(func()==1):
        print("White will go first")
    else:
        print("Black will go first")

game_run(first)