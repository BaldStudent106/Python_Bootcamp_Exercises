'''
A simple poker game called war as a warmup for my second milestone project
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

    #prints out card
    def __str__(self) :
        return f'{self.rank} of {self.suit}'
class Player:

    #define init method
    def __init__(self,name):
       self.name=name 
       self.allcards=[]

    #add card method
    def addcard(self,new_card):
        if type(new_card)==type([]):
            self.allcards.extend(new_card)
        else:
            self.allcards.append(new_card)

    #define deal card function
    def deal_card(self):
        self.allcards.pop(0)


#Main

#Create a deck of card
deck=[Card(suit,rank) for suit in suits for rank in ranks]

#initiate the players
john=Player('John')
jack=Player('Jack')

#split the cards
for x in range(int(len(deck)/2)):
   john.addcard(deck.pop(0)) 
   jack.addcard(deck.pop(0))

game_on=True
while game_on:


    if len(john.allcards)==52:
        print('John Wins!')
        game_on=False

    if len(jack.allcards)==52:
        print('Jack Wins!')
        game_on=False
