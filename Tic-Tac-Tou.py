'''
This is my simple Tic Tac Tou game created for my Udemy Bootcamp Milestone Project
'''

#fucntion to display the tic tac tou table
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
    white=int
    black=int
    player=[white,black]
    for i in range(len(player)):
        while(True):
            player[i]=input("White will enter a number")
            if player[i].isdigit()==False:
                print("The number entered is not a digit. Please try again")
            else:
                break
    if player[0]>player[1]:
        return 1
    else:
        return 2
