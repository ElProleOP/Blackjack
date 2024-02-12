"""
Blackjack game implementation. Defines Card, Deck, Hand classes 
and game logic functions like hit, hit_or_stand, show_some, etc.
Game loop allows user to play hands of Blackjack against a dealer.
"""
import random

ranks = [str(n) for n in range(2, 11)] + list('JQKA')
suits = '♣ ♦ ♥ ♠'.split()
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10,
          'Q':10, 'K':10, 'A':11}


playing = True
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + self.suit
    
class Deck:

    def __init__(self):
        self.cards = [Card(suit,rank) for suit in suits for rank in ranks]

    def deal(self):
        card_to_deal = self.cards[random.randint(0,len(self.cards) - 1)]
        self.cards.remove(card_to_deal)
        return card_to_deal
    

class Hand:

    def __init__(self):
        self.hand_cards = []
        self.values = 0
        self.aces = 0
    
    def add_card(self,card):
        self.hand_cards.append(card)
        self.values += values[card.rank]

    def adjust_for_ace(self):
        while self.values > 21 and self.aces:
            self.values -= 10
            self.aces -= 1


def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.hand_cards[1])
    print("\nPlayer's Hand:", *player.hand_cards, sep='\n ')

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.hand_cards, sep='\n ')
    print("Dealer's Hand =",dealer.values)
    print("\nPlayer's Hand:", *player.hand_cards, sep='\n ')
    print("Player's Hand =",player.values)

def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

def hit(deck,hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    choices = ["Hit", "Stand"]
    while True:
        print("Enter {} or {}".format(choices[0],choices[1]))
        user_input = input("")
        if user_input in choices:
            if user_input == "Hit":
                hit(deck,hand)
            else:
                print("Player stands, Dealer is playing")
                playing = False
        else:
            print("Please enter a valid value")
            continue
        break
    


while True:

    deck = Deck()
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    show_some(player_hand,dealer_hand)

    while playing:

        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        if player_hand.values > 21:
            print("Player busts!")
            break

    if player_hand.values <= 21:
        while dealer_hand.values < 17:
            hit(deck,dealer_hand)

            # Show all cards
        show_all(player_hand,dealer_hand)

        # Run different winning scenarios
        if dealer_hand.values > 21:
            print("Dealer busts! Player wins")
        elif dealer_hand.values > player_hand.values:
            print("Dealer wins :(")
        elif dealer_hand.values < player_hand.values:
            print("You Win!")

        else:
            push(player_hand,dealer_hand)
    
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break


