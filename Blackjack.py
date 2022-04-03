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

#Player Class
class Player:

    #define init
    def __init__(self):
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
        return sum(self.cards)==15
    
    #decide the value of ace
    def ace_value(self):
        for card in self.cards:
            print(f'You currently have a {card.rank}')
        print('What value you want ur ace to be?')
        print('1 - 1')
        print('2 - 11')
        choice=int(input('Which value do you want ur ace to be'))
        if choice==1:
            for card in self.cards:
                if self.rank=='Ace':
                    self.value=1        
        elif choice==2:
            for card in self.cards:
                if self.rank=='Ace':
                    self.value=11        

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
#created a whole new deck of poker
deck=[Card(suit,rank) for suit in suits for rank in ranks]

#shuffle the deck
random.shuffle(deck)

#Receive the player count
player_count=int(input('How many players are there?'))
players=[Player() for player_count in range(player_count)]

#Gives each player 2 cards
for player in players:
    player.addcard(deck.pop(-1))
    player.addcard(deck.pop(-1))

#Game main logic
for player in players:
    player_round=True
    while player_round:
        if len(player.cards)==2:

            if player.doublecheck==True:
                print('You got a double')
                player.win_value=1
                break

            if player.triplecheck==True:
                print('You got a triple')
                player.win_value=2
                break


            if player.pssycheck==True:
                print('Bye fker')
                player.win_value=-3
                break


        if len(player.cards)>5:
            if player.dragon_check==True:
                print('You got a dragon')
                player.win_value=3
                break

            if player.great_dragon_check==True:
                print('You got a great dragon')
                player.win_value=4
                break

            if player.great_boom==True:
                print('Boom!Boom!')
                player_round=False
                player.win_value=-2
                break

        if player.acecheck()==True:
            player.ace_value

        value=player.value_calculate 

        if value >21:
            print('Boom')
            player.win_value=-1
            player_round=False

        elif value<=21:
            print(f'Your current points is {value}')
            while not(choice=='hit' or choice=='stand'):
                choice=input('Woud you like to hit or stand:\n')
            if choice=='hit':
                player.addcard(deck.pop(-1))
            elif choice=='stand':
                player_round=False

for player in players[:-1]:
    if player.win_value==-3:
       print('Bye pssy') 
    elif player.win_value==-2:
        print('Great loss!')
    elif player.win_value==-1:
        print('Boom!')
    elif player.win_value==1 and player.win_value>players[-1].win_value:
        print('You win double!')
    elif player.win_value==1 and player.win_value==players[-1].win_value:
        print('Draw')
    elif player.win_value==1 and player.win_value<players[-1].win_value:
        print('U lose triple')
    elif player.win_value==2 and player.win_value>players[-1].win_value:
        print('You win triple')
    elif player.win_value==2 and player.win_value==players[-1].win_value:
        print('Draw')
    elif player.win_value==3:
        print('You win double')
    elif player.win_value==4:
        print('You win triple')
    else:
        if player.win_value==21 and players[-1].win_value<player.win_value:
            print('You win double')
        if player.win_value==21 and players[-1].win_value==player.win_value:
            print('Draw')
        if player.value_calculate>players[-1].value_calculate:
            print('You win')
        if player.value_calculate==players[-1].value_calculate:
            print('Draw')
        if player.value_calculate<players[-1].value_calculate:
            print('You lose')
    
    

