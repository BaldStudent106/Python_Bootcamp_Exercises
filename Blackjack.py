'''
A simple Blackjack game created as my second milestone project

Steps
1. Create a deck
2. Deal each player 2 cards
3. Stand and Deal
4. Show hand

'''

#data required for a deck of poker cards
suits=['Diamonds','Clubs','Hearts','Spades']
ranks=['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

#Card Class
class Card:
    
    #init method of Card
    def __init__(self,suit,rank): 

        self.suit=suit
        self.rank=rank
        self.value=values[rank]

deck=[Card(suit,rank) for suit in suits for rank in ranks]