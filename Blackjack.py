'''
A simple Blackjack game created as my second milestone project

Steps
1. Create a deck
2. Deal each player 2 cards
3. Stand and Deal
4. Show hand

'''
#import random module from python standard library
import random

#import reduce function
from functools import reduce

#data required for a deck of poker cards
suits=['Diamonds','Clubs','Hearts','Spades']
ranks=['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':0}
#Card Class
class Card:
    
    #init method of Card
    def __init__(self,suit,rank): 

        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self) :
        return f'{self.suit} of {self.rank}'
#Player Class
class Player:

    #define init
    def __init__(self,player):
        self.player=player
        self.cards=[]
        self.win_value=0

    #method to add cards to player
    def addcard(self,new_card):
        self.cards.append(new_card)

    #check if theres a double
    def doublecheck(self):
       value_total=[card.value for card in self.cards]
       return any(map(lambda x:x.value==10,self.cards)) and sum(value_total)<=10  

    #check if there is a triple
    def triplecheck(self):
        value_total=[card.value for card in self.cards]
        return sum(value_total)==0

    #chech if there is an ace
    def acecheck(self):
        return any(map(lambda x:x.rank=='Ace',self.cards))

    #define pssycheck
    def pssycheck(self):
        value_list=[x.value for x in self.cards]
        return sum(value_list)==15
    
    #decide the value of ace
    def ace_value(self):
        print('What value you want ur ace to be?')
        print('1 - 1')
        print('2 - 11')
        choice=int(input('Which value do you want ur ace to be'))
        if choice==1:
            for card in self.cards:
                if card.rank=='Ace':
                    card.value=1        
        elif choice==2:
            for card in self.cards:
                if card.rank=='Ace':
                    card.value=11        

    def value_calculate(self):
        total=0
        for card in self.cards:
            total+=card.value
        return total

    def dragon_check(self):
        return reduce(lambda x,y:x+y, self.cards)<21
        
    def great_dragon_check(self):
        return reduce(lambda x,y:x+y, self.cards)==21

    def great_boom(self):
        return reduce(lambda x,y:x+y, self.cards)>21

    def __str__(self):
        return f'The current player is {self.player}'

#created a whole new deck of poker
deck=[Card(suit,rank) for suit in suits for rank in ranks]

#shuffle the deck
random.shuffle(deck)

#Receive the player count
player_count=int(input('How many players are there?\n'))
players=[Player(f'player {player_count}') for player_count in range(player_count)]
players[-1].player='The Dealer'

#Gives each player 2 cards
for player in players:
    player.addcard(deck.pop(-1))
    player.addcard(deck.pop(-1))

#Game main logic
for player in players:
    player_round=True
    while player_round:

        print(f'\n {player} \n')

        for card in player.cards:
            print(card)

        if len(player.cards)==2:

            if player.doublecheck()==True:
                print('You got a double\n')
                player.win_value=1
                break

            if player.triplecheck()==True:
                print('You got a triple\n')
                player.win_value=2
                break


            if player.pssycheck()==True:
                pssychoice=input('You got a 15. Would you like to be a pssy?\n')
                if pssychoice=='y':
                    print('Bye fker\n')
                    player.win_value=-3
                    break
                else:
                    pass


        if len(player.cards)>5:
            if player.dragon_check==True:
                print('You got a dragon \n')
                player.win_value=3
                break

            if player.great_dragon_check()==True:
                print('You got a great dragon\n')
                player.win_value=4
                break

            if player.great_boom()==True:
                print('Boom!Boom!\n')
                player_round=False
                player.win_value=-2
                break

        if player.acecheck()==True:
            player.ace_value()

        value=player.value_calculate()

        if player==players[-1]:
            if value<17:
                print('You dont have enough points\n')
                continue

        if value >21:
            print('Boom\n')
            player.win_value=-1
            player_round=False

        elif value<=21:
            print(f'Your current points is {value}\n')
            choice=' '
            while not(choice=='hit' or choice=='stand'):
                choice=input('Woud you like to hit or stand:\n')
            if choice=='hit':
                player.addcard(deck.pop(-1))
            elif choice=='stand':
                player_round=False


for player in players[:-1]:
    print(f'\n{player}\n')
    if player.win_value==-3:
       print('Bye pssy\n') 

    elif player.win_value==-2:
        print('Great loss!\n')

    elif player.win_value==-1:
        print('Boom!\n')

    elif player.win_value==1 and player.win_value>players[-1].win_value:
        print('You win double!\n')

    elif player.win_value==1 and player.win_value==players[-1].win_value:
        print('Draw\n')

    elif player.win_value==1 and player.win_value<players[-1].win_value:
        print('U lose triple\n')

    elif player.win_value==2 and player.win_value>players[-1].win_value:
        print('You win triple\n')

    elif player.win_value==2 and player.win_value==players[-1].win_value:
        print('Draw\n')

    elif player.win_value==3:
        print('You win double\n')

    elif player.win_value==4:
        print('You win triple\n')
    else:

        if player.win_value==21 and players[-1].win_value<player.win_value:
            print('You win double\n')

        if player.win_value==21 and players[-1].win_value==player.win_value:
            print('Draw\n')

        if player.value_calculate()>players[-1].value_calculate():
            print('You win\n')

        if player.value_calculate()==players[-1].value_calculate():
            print('Draw\n')

        if player.value_calculate()<players[-1].value_calculate():
            print('You lose\n')
    
    

