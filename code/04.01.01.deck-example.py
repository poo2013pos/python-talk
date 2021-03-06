#!/bin/env python
import random

def new_deck():
    """
    create a deck of cards
    suit: club=C, diamond=D, heart=H spade=S
    rank: ace=A, 10=T, jack=J, queen=Q, king=K, numbers=2..9
    ace of spade would be AS, 8 of heart would be 8H and so on
    return a list of a full deck of cards
    """
    rs = []
    rank = "A 2 3 4 5 6 7 8 9 T J Q K".split()
    # First way to debug
    #import pdb; pdb.set_trace()
    # Second way to debug
    import ipdb; ipdb.set_trace()
    # Third way to debug
    #import pudb; pudb.set_trace()
    suit = "C D H S".split()
    for r in rank:
        for s in suit:
	    rs = rs + [r + s]
    
    #rs = [rank + suit for rank in "A23456789TJQK" for suit in "CDHS"]
    
    return rs
    
def draw_cards(n, cards_list):
    """
    randomly draw n cards from the deck (cards_list)
    remove those cards from the deck
    since object cards_list is by reference, it will change too
    return a list of n cards
    """
    random.shuffle(cards_list)
    return [cards_list.pop() for k in range(n)]
    
# new deck
cards_list = new_deck()
print("New deck = %s cards" % len(cards_list)) # test

# draw n cards per hand
n = 5

# draw the hands
hand1 = draw_cards(n, cards_list)
hand2 = draw_cards(n, cards_list)
print('-' * 38)

# show the 2 hands
print("hand1 = %s" % hand1)
print("hand2 = %s" % hand2)
print('-' * 38)
print("New deck = %s cards" % len(cards_list)) # test
"""my random result -->
New deck = 52 cards
----------------------------------------
hand1 = ['4C', 'JH', '9H', 'TC', '4H']
hand2 = ['TH', 'KC', '5D', '6D', 'KD']
----------------------------------------
New deck = 42 cards
"""
