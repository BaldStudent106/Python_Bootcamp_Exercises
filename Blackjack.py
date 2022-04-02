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

    #method to add cards to player
    def addcard(self,new_card):
        self.cards.append(new_card)

    #check if theres a double
    def doublecheck(self):
       value_total=[card.value for card in self.cards]
       value_tuple=tuple(value_total)
       return any(map(lambda x:x.value==10,self.cards)) and sum(value_tuple)<=21  

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

draw_round=True
while draw_round:
    for player in players:
        if len(player.cards)==2:
            player.doublecheck
