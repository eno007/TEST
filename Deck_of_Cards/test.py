#!/usr/bin/python3
Card = __import__('deck_of_cards').Card
Deck = __import__('deck_of_cards').Deck
Player = __import__('deck_of_cards').Player


"""Tests"""
deck = Deck()
deck.shuffle()

bob = Player("Bob", 50)
ben = Player("Ben", 51)

for i in range(5):
    bob.draw(deck)
    ben.draw(deck)

print("Bob:")
bob.showHand()
bob_points = bob.evaluate_points()

print("\nBen:")
ben.showHand()
ben_points = ben.evaluate_points()

if bob_points > ben_points:
    print("\nBob wins")
elif ben_points > bob_points:
    print("\nBen wins")
else:
    print("\nDraw")
