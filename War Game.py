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

    #Checks if player 1 wins the game
    if len(john.allcards)==52:
        print('John Wins!')
        game_on=False
        break

    #Checks if player 2 wins the game
    if len(jack.allcards)==52:
        print('Jack Wins!')
        game_on=False
        break

    #places on card on the table
    john_cards_on_hand=[]
    john_cards_on_hand.append(john.deal_card)

    #places on card on the table
    jack_cards_on_hand=[]
    jack_cards_on_hand.append(jack_cards_on_hand)

    at_war=True

    while at_war:
        if john_cards_on_hand[-1].value>jack_cards_on_hand[-1].value:
            print('John Wins!')
            john.addcard(john_cards_on_hand)
            john.addcard(jack_cards_on_hand)

        elif jack_cards_on_hand[0].value>john_cards_on_hand[0].value:
            print('Jack Wins!')
            jack.addcard(john_cards_on_hand)
            jack.addcard(jack_cards_on_hand)

        else:
            print('War')
            if len(jack.allcards)<5:
                print('John Wins') 
                game_on=False

            elif len(john.allcards<5):
                print('Jack wins')
                game_on=False

            else:
                for num in range(5):
                    john_cards_on_hand.append(john.deal_card) 
                    jack_cards_on_hand.append(jack.deal_card)
