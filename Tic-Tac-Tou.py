'''
This is my simple Tic Tac Tou game created for my Udemy Bootcamp Milestone Project
'''

#fucntion to display the tic tac tou table
def display(num):

    #Prints Out the table
    print("\n")
    print("\t \t|\t \t|")
    print(f"\t{num['Top Left']}\t|\t{num['Top Middle']}\t|\t{num['Top Right']}\t")
    print("_"*50)
    print("\t \t|\t \t|")
    print(f"\t{num['Middle Left']}\t|\t{num['Middle']}\t|\t{num['Middle Right']}\t")
    print("_"*50)
    print("\t \t|\t \t|")
    print(f"\t{num['Bottom Left']}\t|\t{num['Bottom Middle']}\t|\t{num['Bottom Right']}\t")
    print("\n")

#Function to decide which player goes first
def first():

    #Import ramdom module from the python library
    import random

    #Player dictionary to decide who goes first
    player={"White":0, "Black":0}

    #Uses random to decide which player goes first
    for i in (player):
            player[i]=(random.randrange(0,10))

    #Check who goes first
    if player["White"]>player["Black"]:
        return 1
    else:
        return 2


#Function to check whether if a player has won
def win_check(dict,turn):

    #if statement to check if someone wins
    if(dict['Top Left']==dict['Top Middle']==dict['Top Right'] and dict['Top Left']!= " "
    or dict['Middle Left']==dict['Middle']==dict['Middle Right'] and dict['Middle']!=" "
    or dict['Bottom Right']==dict['Bottom Middle']==dict['Bottom Right'] and dict['Bottom Right']!=" "
    or dict['Top Left']==dict['Middle Left']==dict['Bottom Left'] and dict['Top Left']!=" "
    or dict['Top Middle']==dict['Middle']==dict['Bottom Middle'] and dict['Middle']!=" "
    or dict['Top Right']==dict['Middle Right']==dict['Bottom Right'] and dict['Top Right']!=" "
    or dict['Top Right']==dict['Middle']==dict['Bottom Left'] and dict['Middle']!=" "
    or dict['Top Left']==dict['Middle']==dict['Bottom Right'] and dict['Middle']!=" "
    ):

        #Check which player wins
        if(turn%2!=0):
            print("White wins")
        else:
            print("Black wins")
        return False
    return True

#Main Function to run the game
def tic_tac_tou():

    #Dictionary to record the table
    game_record={"Top Left":" ","Top Middle":" ", "Top Right":" ", "Middle Left":" ", "Middle":" ", "Middle Right":" ", "Bottom Left":" ", "Bottom Middle":" ", "Bottom Right":" "}

    #Input to make sure the player is ready
    continuecheck=input("Are you ready to start the game? Enter Yes or No")
    if continuecheck.lower()=='y':
        game_on=True
    else:
        game_on=False

    #Decides who goes first
    if(first()==1):
        print("White will go first")
        turn=1
    else:
        print("Black will go first")
        turn=2


    #Prompt for user to press enter to continue
    input()

    #Print out the table
    display(game_record)

    #Prompt for user to press enter to continue
    input()

    while(game_on):

        #Print Out choices left for moves
        for i,j in enumerate(game_record):
            if game_record[j]==" ":
                print(f"{i}: {j}")

        #Prompt for the user for their move
        choice=input("Please enter your choice: \n")
        if(turn%2 != 0):
            game_record[choice]="O"
        else:
            game_record[choice]="X"

        #Call function to check if someone wins
        game_on=win_check(game_record,turn)

        #Print out the table once more
        display(game_record)
        turn+=1

#Running the main function to start the program
tic_tac_tou()