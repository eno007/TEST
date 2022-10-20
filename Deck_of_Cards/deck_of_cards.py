#!/usr/bin/python3
import random

class Card:
    def __init__(self, suit, value):
        self.__suit = suit
        self.__value = value

    @property
    def suit(self):
        return self.__suit

    @property
    def value(self):
        return self.__value

    @suit.setter
    def suit(self, suit):
        self.__suit = suit

    @value.setter
    def value(self, value):
        self.__value = value

    def showCard(self):
        print("{} {}".format(self.value, self.suit))

    def evaluate_points(self):
        if self.value == "J" or self.value == "Q" or self.value == "K":
            return 10
        elif self.value == "A":
            return 11
        else:
            return int(self.value)


class Deck:
    cardRank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["\u2666", "\u2665", "\u2663", "\u2660"]

    def __init__(self):
        self.__deck = []
        self.build()

    @property
    def deck(self):
        return self.__deck

    @deck.setter
    def deck(self, deck):
        self.__deck = deck

    def build(self):
        for s in self.suits:
            for v in self.cardRank:
                self.deck.append(Card(s, v))

    def showDeck(self):
        for c in self.deck:
            c.showCard()

    def shuffle(self):
        random.shuffle(self.deck)

    def drawCard(self):
        return self.deck.pop()


class Player:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__hand = []

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def hand(self):
        return self.__hand

    @name.setter
    def name(self, name):
        self.__name = name

    @age.setter
    def age(self, age):
        self.__age = age

    @hand.setter
    def hand(self, hand):
        self.__hand == hand

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.showCard()

    def evaluate_points(self):
        points = [c.evaluate_points() for c in self.hand]
        total = sum(points)
        print("{} points".format(total))
        return total
